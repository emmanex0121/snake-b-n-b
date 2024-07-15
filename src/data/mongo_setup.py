""" mongo engine connection """
import mongoengine


def global_init():
    """
        global init
    """
    mongoengine.register_connection(alias='core', name='snake_bnb') # type: ignore
