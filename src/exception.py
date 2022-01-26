from __future__ import annotations
import inspect
import types
import typing
from PyQt5.QtCore import QDataStream


class OpenTeleException(BaseException):  # nocov
    """
    Base exception of the library.
    """

    def __init__(self, message: str = None, stack_index: int = 1) -> None:

        super().__init__(message if (message != None) else "")

        self.message = message
        self.desc = self.__class__.__name__

        self.frame = inspect.currentframe()
        for i in range(stack_index):
            self.frame = self.frame.f_back

        self._caller_class = (
            self.frame.f_locals["self"].__class__
            if "self" in self.frame.f_locals
            else None
        )
        self._caller_method = self.frame.f_code.co_name

        if self._caller_method != "<module>":
            args, _, _, locals = inspect.getargvalues(self.frame)
            parameters = {arg: locals[arg] for arg in args}
            self._caller_method_params = "".join(
                f"{i}={parameters[i]}, " for i in parameters
            )[:-2]
        else:
            self._caller_method = "__main__"
            self._caller_method_params = ""

        if self.desc == "OpenTeleException":
            self.desc = "Unexpected Exception"

    def __str__(self):
        reason = self.desc.__str__()

        if self.message != None:
            reason += f": {self.message}"

        reason += " [ Called by "
        if self._caller_class != None:

            parent_list = []
            base = self._caller_class
            while hasattr(base, "__name__"):
                parent_list.append(base.__name__)
                base = base.__base__

            parent_list.reverse()
            reason += "".join(f"{i}." for i in parent_list[1:])
            reason += self._caller_method + "() ]"
            # reason += f"\n>\t{self._caller_method}({self._caller_method_params})"
        else:
            reason += f"{self._caller_method}() ]"
            # reason += f"{self._caller_method}({self._caller_method_params}) ]"
        return reason


class TFileNotFound(OpenTeleException):
    """
    Could not find or open the file
    """


class TDataInvalidMagic(OpenTeleException):
    """
    TData file has an invalid magic data, which is the first 4 bytes of the file\n
    This usually mean that the file is corrupted or not in the supported formats
    """


class TDataInvalidCheckSum(OpenTeleException):
    """
    TData file has an invalid checksum\n
    This usually mean that the file is corrupted or not in the supported formats
    """


class TDataBadDecryptKey(OpenTeleException):
    """
    Could not decrypt the data with this key\n
    This usually mean that the file is password-encrypted
    """


class TDataWrongPasscode(OpenTeleException):
    """
    Wrong passcode to decrypt tdata folder\n
    """


class TDataBadEncryptedDataSize(OpenTeleException):
    """
    The encrypted data size part of the file is corrupted
    """


class TDataBadDecryptedDataSize(OpenTeleException):
    """
    The decrypted data size part of the file is corrupted
    """


class TDataBadConfigData(OpenTeleException):
    """
    TData contains bad config data that couldn't be parsed
    """


class QDataStreamFailed(OpenTeleException):
    """
    Could not stream data from QDataStream\n
    Please check the QDataStream.status() for more information
    """


class AccountAuthKeyNotFound(OpenTeleException):
    """
    Account.authKey is missing, something went wrong
    """


class TDataReadMapDataFailed(OpenTeleException):
    """
    Could not read map data
    """


class TDataReadMapDataIncorrectPasscode(OpenTeleException):
    """
    Could not read map data because of incorrect passcode
    """


class TDataAuthKeyNotFound(OpenTeleException):
    """
    Could not find authKey in TData
    """


class MaxAccountLimit(OpenTeleException):
    """
    Maxed out limit for accounts per tdesktop client
    """


class TDesktopUnauthorized(OpenTeleException):
    """
    TDesktop client is unauthorized
    """


class TelethonUnauthorized(OpenTeleException):
    """
    Telethon client is unauthorized
    """


class TDataSaveFailed(OpenTeleException):
    """
    Could not save TDesktop to tdata folder
    """


class TDesktopNotLoaded(OpenTeleException):
    """
    TDesktop instance has no account
    """


class TDesktopHasNoAccount(OpenTeleException):
    """
    TDesktop instance has no account
    """


class TDAccountNotLoaded(OpenTeleException):
    """
    TDesktop account hasn't been loaded yet
    """


class NoPasswordProvided(OpenTeleException):
    """
    You can't live without a password bro
    """


class PasswordIncorrect(OpenTeleException):
    """
    incorrect passwrd
    """


class LoginFlagInvalid(OpenTeleException):
    """
    Invalid login flag
    """


class NoInstanceMatched(OpenTeleException):
    """
    Invalid login flag
    """


@typing.overload
def Expects(
    condition: bool,
    message: str = None,
    done: typing.Callable[[], None] = None,
    fail: typing.Callable[[OpenTeleException], None] = None,
    silent: bool = False,
    stack_index: int = 1,
) -> bool:
    """Expect a condition to be `True`, raise an `OpenTeleException` if it's not.

    ### Arguments:
        condition (bool):
            Condition that you're expecting.

        message (str, default=None):
            Custom exception message

        done (`lambda`, default=None):
            lambda to execute when done without error

        fail (`lambda`, default=None):
            lambda to execute when the condition is False, the lambda will be execute before raising the exception.

        silent (`bool`, default=False):
            if True then it won't raise the exception, only execute fail lambda.

        stack_index (`int`, default=1):
            stack index to raise the exception with trace back to where it happens, intended for internal usage.

    ### Raises:
        `OpenTeleException`: exception
    """


@typing.overload
def Expects(
    condition: bool,
    exception: OpenTeleException = None,
    done: typing.Callable[[], None] = None,
    fail: typing.Callable[[OpenTeleException], None] = None,
    silent: bool = False,
    stack_index: int = 1,
) -> bool:

    """Expect a condition to be `True`, raise an `OpenTeleException` if it's not.

    ### Arguments:
        condition (bool):
            Condition that you're expecting.

        message (OpenTeleException, default=None):
            Custom exception.

        done (`lambda`, default=None):
            lambda to execute when done without error.

        fail (`lambda`, default=None):
            lambda to execute when the condition is False, the lambda will be execute before raising the exception.

        silent (`bool`, default=False):
            if True then it won't raise the exception, only execute fail lambda.

        stack_index (`int`, default=1):
            stack index to raise the exception with trace back to where it happens, intended for internal usage.

    ### Raises:
        `OpenTeleException`: exception
    """


def Expects(
    condition: bool,
    exception: typing.Union[OpenTeleException, str] = None,
    done: typing.Callable[[], None] = None,
    fail: typing.Callable[[OpenTeleException], None] = None,
    silent: bool = False,
    stack_index: int = 1,
) -> bool:  # nocov

    if condition:
        if done != None:
            done()
        return condition

    if isinstance(exception, str):
        exception = OpenTeleException(exception, 2)

    elif exception != None and not isinstance(exception, OpenTeleException):
        raise OpenTeleException("No instance of Expects() match the arguments given", 2)

    if exception == None:
        exception = OpenTeleException("Unexpected error", 2)

    # no raise exception
    if silent:
        if fail != None:
            fail(exception)
        return condition

    else:
        stack = inspect.stack()
        frame = stack[stack_index].frame
        tb = types.TracebackType(None, frame, frame.f_lasti, frame.f_lineno)  # type: ignore
        exception = exception.with_traceback(tb)

        if fail != None:
            fail(exception)

        raise exception


def ExpectStreamStatus(stream: QDataStream, message: str = "Could not stream data"):
    Expects(
        stream.status() == QDataStream.Status.Ok,
        stack_index=2,
        exception=QDataStreamFailed(
            "Could not read keys count from mtp authorization.", stack_index=2
        ),
    )
