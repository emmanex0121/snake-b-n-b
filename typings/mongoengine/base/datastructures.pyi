"""
This type stub file was generated by pyright.
"""

from bson import DBRef

__all__ = ("BaseDict", "StrictDict", "BaseList", "EmbeddedDocumentList", "LazyReference")
def mark_as_changed_wrapper(parent_method): # -> Callable[..., Any]:
    """Decorator that ensures _mark_as_changed method gets called."""
    ...

def mark_key_as_changed_wrapper(parent_method): # -> Callable[..., Any]:
    """Decorator that ensures _mark_as_changed method gets called with the key argument"""
    ...

class BaseDict(dict):
    """A special dict so we can watch any changes."""
    _dereferenced = ...
    _instance = ...
    _name = ...
    def __init__(self, dict_items, instance, name) -> None:
        ...
    
    def get(self, key, default=...): # -> BaseDict | BaseList | None:
        ...
    
    def __getitem__(self, key): # -> BaseDict | BaseList:
        ...
    
    def __getstate__(self): # -> Self:
        ...
    
    def __setstate__(self, state):
        ...
    
    __setitem__ = ...
    __delattr__ = ...
    __delitem__ = ...
    pop = ...
    clear = ...
    update = ...
    popitem = ...
    setdefault = ...


class BaseList(list):
    """A special list so we can watch any changes."""
    _dereferenced = ...
    _instance = ...
    _name = ...
    def __init__(self, list_items, instance, name) -> None:
        ...
    
    def __getitem__(self, key): # -> BaseDict | BaseList:
        ...
    
    def __iter__(self): # -> Generator[Any, Any, None]:
        ...
    
    def __getstate__(self): # -> Self:
        ...
    
    def __setstate__(self, state):
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    append = ...
    extend = ...
    insert = ...
    pop = ...
    remove = ...
    reverse = ...
    sort = ...
    __delitem__ = ...
    __iadd__ = ...
    __imul__ = ...


class EmbeddedDocumentList(BaseList):
    def __init__(self, list_items, instance, name) -> None:
        ...
    
    def filter(self, **kwargs): # -> EmbeddedDocumentList:
        """
        Filters the list by only including embedded documents with the
        given keyword arguments.

        This method only supports simple comparison (e.g. .filter(name='John Doe'))
        and does not support operators like __gte, __lte, __icontains like queryset.filter does

        :param kwargs: The keyword arguments corresponding to the fields to
         filter on. *Multiple arguments are treated as if they are ANDed
         together.*
        :return: A new ``EmbeddedDocumentList`` containing the matching
         embedded documents.

        Raises ``AttributeError`` if a given keyword is not a valid field for
        the embedded document class.
        """
        ...
    
    def exclude(self, **kwargs): # -> EmbeddedDocumentList:
        """
        Filters the list by excluding embedded documents with the given
        keyword arguments.

        :param kwargs: The keyword arguments corresponding to the fields to
         exclude on. *Multiple arguments are treated as if they are ANDed
         together.*
        :return: A new ``EmbeddedDocumentList`` containing the non-matching
         embedded documents.

        Raises ``AttributeError`` if a given keyword is not a valid field for
        the embedded document class.
        """
        ...
    
    def count(self): # -> int:
        """
        The number of embedded documents in the list.

        :return: The length of the list, equivalent to the result of ``len()``.
        """
        ...
    
    def get(self, **kwargs):
        """
        Retrieves an embedded document determined by the given keyword
        arguments.

        :param kwargs: The keyword arguments corresponding to the fields to
         search on. *Multiple arguments are treated as if they are ANDed
         together.*
        :return: The embedded document matched by the given keyword arguments.

        Raises ``DoesNotExist`` if the arguments used to query an embedded
        document returns no results. ``MultipleObjectsReturned`` if more
        than one result is returned.
        """
        ...
    
    def first(self): # -> BaseDict | BaseList | None:
        """Return the first embedded document in the list, or ``None``
        if empty.
        """
        ...
    
    def create(self, **values):
        """
        Creates a new instance of the EmbeddedDocument and appends it to this EmbeddedDocumentList.

        .. note::
            the instance of the EmbeddedDocument is not automatically saved to the database.
            You still need to call .save() on the parent Document.

        :param values: A dictionary of values for the embedded document.
        :return: The new embedded document instance.
        """
        ...
    
    def save(self, *args, **kwargs): # -> None:
        """
        Saves the ancestor document.

        :param args: Arguments passed up to the ancestor Document's save
         method.
        :param kwargs: Keyword arguments passed up to the ancestor Document's
         save method.
        """
        ...
    
    def delete(self): # -> int:
        """
        Deletes the embedded documents from the database.

        .. note::
            The embedded document changes are not automatically saved
            to the database after calling this method.

        :return: The number of entries deleted.
        """
        ...
    
    def update(self, **update): # -> int:
        """
        Updates the embedded documents with the given replacement values. This
        function does not support mongoDB update operators such as ``inc__``.

        .. note::
            The embedded document changes are not automatically saved
            to the database after calling this method.

        :param update: A dictionary of update values to apply to each
         embedded document.
        :return: The number of entries updated.
        """
        ...
    


class StrictDict:
    __slots__ = ...
    _special_fields = ...
    _classes = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def __getitem__(self, key): # -> Any:
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def __contains__(self, key): # -> bool:
        ...
    
    def get(self, key, default=...): # -> Any | None:
        ...
    
    def pop(self, key, default=...): # -> Any | None:
        ...
    
    def iteritems(self): # -> Generator[tuple[Any, Any], Any, None]:
        ...
    
    def items(self): # -> list[tuple[Any, Any]]:
        ...
    
    def iterkeys(self): # -> Generator[Never, None, None]:
        ...
    
    def keys(self): # -> list[Never]:
        ...
    
    def __iter__(self): # -> Generator[Never, None, None]:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    @classmethod
    def create(cls, allowed_keys):
        ...
    


class LazyReference(DBRef):
    __slots__ = ...
    def fetch(self, force=...):
        ...
    
    @property
    def pk(self): # -> Any:
        ...
    
    def __init__(self, document_type, pk, cached_doc=..., passthrough=...) -> None:
        ...
    
    def __getitem__(self, name):
        ...
    
    def __getattr__(self, name):
        ...
    
    def __repr__(self): # -> str:
        ...
    


