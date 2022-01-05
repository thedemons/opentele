
from .storage import *
from .exception import *
from .authkey import *

from PyQt5.QtCore import QByteArray, QDataStream, QBuffer, QFile, QIODevice

import typing
if typing.TYPE_CHECKING:
    from .opentele import *

import telethon
from telethon.crypto import AuthKey as TelethonAuthKey
from telethon.sessions.sqlite import SQLiteSession

class TDesktop:
    def __init__(self) -> None:
        pass
    
    @property
    def passcodeKey(self) -> AuthKey:
        return self.__passcodeKey

    @property
    def localKey(self) -> AuthKey:
        return self.__localKey
        
    @property
    def account_count(self) -> int:
        return self.__account_count

    @property
    def UserId(self) -> int:
        return self.__UserId

    @property
    def MainDcId(self) -> int:
        return self.__MainDcId

    @property
    def AppVersion(self) -> int:
        return self.__AppVersion
    @property
    def AppVersionString(self) -> int:
        return self.__AppVersion

    @property
    def authKey(self) -> AuthKey:
        return self.__authKey

    def GetDcIp(self, dcId : int):
        DcList = {
        	1 : "149.154.175.53",
            2 : "149.154.167.51",
            3 : "149.154.175.100",
            4 : "149.154.167.91",
            5 : "91.108.56.130",
        }
        return DcList[dcId]

    def ConvertToTelethon(self, filePath):
        ss = SQLiteSession("test")
        ss.set_dc(self.MainDcId, self.GetDcIp(self.MainDcId), 443)

        ss.auth_key = TelethonAuthKey(self.authKey.key)
        ss.save()

    def FromTData(self, basePath : str, passcode : str = "", keyFile : str = "data") -> None:
        
        if (basePath[-2:-1] != "\\"): basePath += "\\" 

        # READ KEY_DATA
        keyData = ReadFile("key_" + keyFile, basePath)

        salt, keyEncrypted, infoEncrypted = QByteArray(), QByteArray(), QByteArray()

        keyData.stream >> salt >> keyEncrypted >> infoEncrypted
        if keyData.stream.status() != 0:
            raise OpenTeleException(OpenTeleErrorCode.QDataStreamFailed, "Failed to stream keyData")

        
        self.__AppVersion = keyData.version
        self.__passcodeKey = CreateLocalKey(salt, QByteArray(passcode.encode("utf-8")))

        keyInnerData = DecryptLocal(keyEncrypted, self.__passcodeKey)
        self.__localKey = AuthKey(keyInnerData.stream.readRawData(256))

        info = DecryptLocal(infoEncrypted, self.__localKey)
        self.__account_count = info.stream.readInt32()

        mtp = ReadEncryptedFile(ToFilePart(ComputeDataNameKey(keyFile)), basePath, self.__localKey)

        blockId = mtp.stream.readInt32()
        if blockId != 75:
            raise OpenTeleException(OpenTeleErrorCode.FileInvalidMagic, "Not supported file version")

        serialized = QByteArray()
        mtp.stream >> serialized

        stream = QDataStream(serialized)
        stream.setVersion(QDataStream.Version.Qt_5_1)

        self.__UserId = stream.readInt32()
        self.__MainDcId = stream.readInt32()
        
        if ((self.__UserId << 32) | self.__MainDcId) == ~0:
            self.__UserId = stream.readUInt64()
            self.__MainDcId = stream.readInt32()

        if stream.status() != 0:
            raise OpenTeleException(OpenTeleErrorCode.QDataStreamFailed, "Could not read main fields from mtp authorization.")
        
        key_count = stream.readInt32()
        if stream.status() != 0:
            raise OpenTeleException(OpenTeleErrorCode.QDataStreamFailed, "Could not read keys count from mtp authorization.")
        
        for i in range(0, key_count):
            dcId = stream.readInt32()
            keyData = stream.readRawData(256)
            if dcId == self.__MainDcId:
                self.__authKey = AuthKey(keyData, AuthKey.Type.ReadFromFile, dcId)
                break
        

        # while (not mtp.stream.atEnd()):
        #     blockId = mtp.stream.readInt32()
        #     if mtp.stream.status() != 0:
        #         raise OpenTeleException(OpenTeleErrorCode.QDataStreamFailed, "Failed to stream mtpData")
        #     print(blockId)
    
