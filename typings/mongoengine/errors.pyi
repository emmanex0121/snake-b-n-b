"""
This type stub file was generated by pyright.
"""

__all__ = ("NotRegistered", "InvalidDocumentError", "LookUpError", "DoesNotExist", "MultipleObjectsReturned", "InvalidQueryError", "OperationError", "NotUniqueError", "BulkWriteError", "FieldDoesNotExist", "ValidationError", "SaveConditionError", "DeprecatedError")
class MongoEngineException(Exception):
    ...


class NotRegistered(MongoEngineException):
    ...


class InvalidDocumentError(MongoEngineException):
    ...


class LookUpError(AttributeError):
    ...


class DoesNotExist(MongoEngineException):
    ...


class MultipleObjectsReturned(MongoEngineException):
    ...


class InvalidQueryError(MongoEngineException):
    ...


class OperationError(MongoEngineException):
    ...


class NotUniqueError(OperationError):
    ...


class BulkWriteError(OperationError):
    ...


class SaveConditionError(OperationError):
    ...


class FieldDoesNotExist(MongoEngineException):
    """Raised when trying to set a field
    not declared in a :class:`~mongoengine.Document`
    or an :class:`~mongoengine.EmbeddedDocument`.

    To avoid this behavior on data loading,
    you should set the :attr:`strict` to ``False``
    in the :attr:`meta` dictionary.
    """
    ...


class ValidationError(AssertionError):
    """Validation exception.

    May represent an error validating a field or a
    document containing fields with validation errors.

    :ivar errors: A dictionary of errors for fields within this
        document or list, or None if the error is for an
        individual field.
    """
    errors = ...
    field_name = ...
    _message = ...
    def __init__(self, message=..., **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __getattribute__(self, name): # -> str | Any:
        ...
    
    message = ...
    def to_dict(self): # -> dict[Any, Any] | str:
        """Returns a dictionary of all errors within a document

        Keys are field names or list indices and values are the
        validation error messages, or a nested dictionary of
        errors for an embedded document or list.
        """
        ...
    


class DeprecatedError(MongoEngineException):
    """Raise when a user uses a feature that has been Deprecated"""
    ...


