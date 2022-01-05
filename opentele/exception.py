
from .tdesktop import *
from enum import Enum, IntEnum

class OpenTeleErrorCode(Enum):
    Success = ...
    FileNotFound = ...
    FileInvalidMagic = ...
    FileInvalidCheckSum = ...
    QDataStreamFailed = ...
    BadDecryptKey = ...
    BadEncryptedDataSize = ...
    BadDecryptedDataSize = ...

class OpenTeleError:


    def __init__(self, code : int) -> None:
        self._code = code
        
        error_dict = {
            OpenTeleErrorCode.Success                   : "Success without error",
            OpenTeleErrorCode.FileNotFound              : "File not found",
            OpenTeleErrorCode.FileInvalidMagic          : "File has invalid magic data",
            OpenTeleErrorCode.FileInvalidCheckSum       : "File has invalid checksum",
            OpenTeleErrorCode.QDataStreamFailed         : "QDataStream failed",
            OpenTeleErrorCode.BadDecryptKey             : "Bad decrypt key",
            OpenTeleErrorCode.BadEncryptedDataSize      : "Bad encrypted part size",
            OpenTeleErrorCode.BadDecryptedDataSize      : "Bad decrypted part size",
        }

        try:
            self._text = error_dict[code]
        except:
            raise BaseException(f"Error code is invalid: {code}")

    @property
    def text(self) -> str:
        return self._text
    
    def __str__(self) -> str:
        return self._text


class OpenTeleException(Exception):
    def __init__(self, code : OpenTeleErrorCode, *args: object) -> None:
        super().__init__(*args)
        self._error_code = OpenTeleError(code)
        self._message = args[0]

    @property
    def error_code(self) -> OpenTeleError:
        return self._error_code
    @property
    def message(self) -> OpenTeleError:
        return self._message
    
    def __str__(self):
        return f"{self._error_code.__str__()}: {self._message}"

