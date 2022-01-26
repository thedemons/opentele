import inspect
import os

import time
import atexit

import typing as t

IS_DEBUG_MODE = False
# IS_DEBUG_MODE = True

if IS_DEBUG_MODE:
    from rich import print  # pragma: no cover

    _F = t.TypeVar("_F")
    _T = t.TypeVar("_T")
    _R = t.TypeVar("_R")

    class DebugInfo(object):
        def __init__(self) -> None:
            self.list: t.List[t.List[str, int, int, int]] = []

        def add(self, name, total_called, total_time) -> None:
            self.list.append(
                (
                    name,
                    total_called,
                    total_time,
                    round(total_time / total_called * 1000, 4),
                )
            )

        def on_exit(self):
            self.list = sorted(self.list, key=lambda item: item[3])

            for item in self.list:

                name = item[0]
                total_called = item[1]
                total_time = item[2]
                avg_time = item[3]

                text = name.ljust(40)
                text += f"called {total_called}".ljust(15)
                text += f"average time: {avg_time} ms".ljust(25)
                print(text)

    dbgInfo = DebugInfo()
    atexit.register(dbgInfo.on_exit)

    class DebugMethod(type):  # pragma: no cover
        def __get__(self, obj, cls):
            self.__owner__ = obj if obj else cls
            return self

        def __call2__(self, *args, **kwargs):
            begin = time.perf_counter()
            result = self.__fget__(*args, **kwargs)  # type: ignore
            diff = time.perf_counter() - begin

            return result, diff

        def __call__(self, *args, **kwargs) -> t.Any:

            # stack = inspect.stack()[1]

            # location = f"{os.path.basename(stack.filename)[:-3]}"
            # lineno = f"{stack.lineno}."

            # if len(location) >= 15:
            #     location = ".." + location[-15:]

            # location = location.ljust(15) + "| " + lineno.ljust(6)

            # context = stack.code_context[0][:-1].strip()  # type: ignore
            # print(location + context, f"took {diff}ms")

            if hasattr(self, "__owner__"):
                result, diff = DebugMethod.__call2__(
                    self, self.__owner__, *args, **kwargs
                )
            else:
                result, diff = DebugMethod.__call2__(self, *args, **kwargs)

            self.__total_called += 1
            self.__total_time += diff

            return result

        def __getfullname(self):
            if hasattr(self, "__ownername__"):
                if self.__fname__ == "__init__":
                    return f"{self.__ownername__}()"

                return f"{self.__ownername__}.{self.__fname__}()"
            else:
                return f"{self.__fget__.__name__}()"

        def on_exit(self):
            if self.__total_called > 0:
                dbgInfo.add(
                    DebugMethod.__getfullname(self),
                    self.__total_called,
                    self.__total_time,
                )

        def __set_name__(self, owner, name):
            self.__owner__: str = owner
            self.__ownername__: str = owner.__name__
            self.__fname__: str = name
            if self.__fname__.startswith(f"_{self.__ownername__}__"):
                self.__fname__ = self.__fname__[len(self.__ownername__) + 1 :]

        def __new__(cls, decorated_func: _F) -> _F:

            firstdct = dict(decorated_func.__dict__)
            for i, x in cls.__dict__.items():
                firstdct[i] = x

            result = type.__new__(
                cls,
                decorated_func.__class__.__name__,
                decorated_func.__class__.__bases__,
                firstdct,
            )

            result.__fget__ = decorated_func
            result.__total_time = 0
            result.__total_called = 0
            atexit.register(result.on_exit, result)
            return result

    def parse_arg(value) -> str:  # pragma: no cover
        if isinstance(value, type):
            return value.__name__
        elif isinstance(value, str):
            return f"'{value}'"
        elif isinstance(value, int):
            return f"{value}"
        elif isinstance(value, object):
            return value.__class__.__name__ + "(...)"
        return value

    class runtime(type):  # pragma: no cover
        def __get__(self, obj, cls):
            self.__owner__ = obj if obj else cls
            return self

        def __call__(self, *args, **kwargs) -> t.Any:

            begin = time.perf_counter()
            result = self.__fget__(self.__owner__, *args, **kwargs)  # type: ignore
            diff = round((time.perf_counter() - begin) * 1000, 2)
            print(f"{self.__fname__} took {diff}ms")
            return result

        def __set_name__(self, owner, name):
            print("set_name")
            self.__owner__ = owner
            self.__ownername__ = owner.__name__
            self.__fname__ = name

        def __new__(cls, decorated_func):

            firstdct = dict(decorated_func.__dict__)
            for i, x in cls.__dict__.items():
                firstdct[i] = x

            result = type.__new__(
                cls,
                decorated_func.__name__,
                decorated_func.__class__.__bases__,
                firstdct,
            )
            result.__fget__ = decorated_func  # type: ignore
            return result
