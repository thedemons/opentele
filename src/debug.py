import inspect
import os

from typing import Any

IS_DEBUG_MODE = False

if IS_DEBUG_MODE:
    from rich import print


class HookClassMethod(type):
    def __get__(self, obj, cls):
        self.__owner__ = obj if obj else cls
        return self

    def __call__(self, *args, **kwargs) -> Any:

        stack = inspect.stack()[1]

        location = f"{os.path.basename(stack.filename)[:-3]}"
        lineno = f"{stack.lineno}."

        if len(location) >= 15:
            location = ".." + location[-15:]

        location = location.ljust(15) + "| " + lineno.ljust(6)

        context = stack.code_context[0][:-1].strip()  # type: ignore

        print(location + context)

        return self.__fget__(self.__owner__, *args, **kwargs)  # type: ignore

    def __set_name__(self, owner, name):
        self.__owner__ = owner
        self.__ownername__ = owner.__name__
        self.__fname__ = name
        pass

    def __new__(cls, decorated_func):

        firstdct = dict(decorated_func.__dict__)
        for i, x in cls.__dict__.items():
            firstdct[i] = x

        result = type.__new__(
            cls, decorated_func.__name__, decorated_func.__class__.__bases__, firstdct
        )
        result.__fget__ = decorated_func  # type: ignore
        return result


def parse_arg(value) -> str:
    if isinstance(value, type):
        return value.__name__
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, int):
        return f"{value}"
    elif isinstance(value, object):
        return value.__class__.__name__ + "(...)"
    return value
