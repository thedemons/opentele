
# from opentele import TDesktop

from PyQt5.QtCore import QByteArray, QDataStream, QBuffer, QFile, QIODevice
from .exception import *
import hashlib

from .authkey import *
import tgcrypto

import typing
if typing.TYPE_CHECKING:
    from .opentele import *

class FileReadDescriptor:
    def __init__(self) -> None:
        self.__version = 0
        self.__data = QByteArray()
        self.__buffer = QBuffer()
        self.__stream = QDataStream()

    @property
    def data(self) -> QByteArray:
        return self.__data
    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def version(self) -> int:
        return self.__version
    @version.setter
    def version(self, value):
        self.__version = value

    @property
    def buffer(self) -> QBuffer:
        return self.__buffer

    @property
    def stream(self) -> QDataStream:
        return self.__stream

class EncryptedDescriptor:
    def __init__(self) -> None:
        self.__data = QByteArray()
        self.__buffer = QBuffer()
        self.__stream = QDataStream()

    @property
    def data(self) -> QByteArray:
        return self.__data
    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def buffer(self) -> QBuffer:
        return self.__buffer

    @property
    def stream(self) -> QDataStream:
        return self.__stream



def ReadFile(fileName : str, basePath : str) -> FileReadDescriptor:

    to_try = ['s', '1', '0']
    tries_exception = None
    for chr in to_try:
        try:

            file = QFile(basePath + fileName + chr)
            if (not file.open(QIODevice.OpenModeFlag.ReadOnly)):
                tries_exception = OpenTeleException(OpenTeleErrorCode.FileNotFound, f"Could not open {fileName}")
                continue

            
            
            magic = file.read(4)
            if magic != b"TDF$":
                tries_exception = OpenTeleException(OpenTeleErrorCode.FileInvalidMagic, f"Invalid magic {magic} in file {fileName}")
                file.close()
                continue
            
            version = int.from_bytes(file.read(4), 'little')

            bytesdata = QByteArray(file.read(file.size()))

            dataSize = bytesdata.size() - 16

            check_md5 = bytesdata.data()[:dataSize]
            check_md5 += int(dataSize).to_bytes(4, 'little')
            check_md5 += int(version).to_bytes(4, 'little')
            check_md5 += magic
            check_md5 = hashlib.md5(check_md5)
            
            md5 = bytesdata.data()[dataSize:]
            
            if (check_md5.hexdigest() != md5.hex()):
                tries_exception = OpenTeleException(OpenTeleErrorCode.FileInvalidCheckSum, f"Invalid checksum {check_md5.hexdigest()} in file {fileName}")
                file.close()
                continue


            result = FileReadDescriptor()
            result.version = version

            bytesdata.resize(dataSize)
            result.data = bytesdata
            bytesdata = QByteArray()

            result.buffer.setBuffer(result.data)

            result.buffer.open(QIODevice.OpenModeFlag.ReadOnly)
            result.stream.setDevice(result.buffer)
            result.stream.setVersion(QDataStream.Version.Qt_5_1)

            file.close()
            return result
        except IOError as e:
            pass
    
    raise tries_exception if tries_exception else OpenTeleException(OpenTeleErrorCode.FileNotFound, f"Could not open {fileName}")

def ReadEncryptedFile(fileName : str, basePath : str, authKey : AuthKey) -> FileReadDescriptor:

    result = ReadFile(fileName, basePath)
    encrypted = QByteArray()
    result.stream >> encrypted

    try:
        data = DecryptLocal(encrypted, authKey)
    except OpenTeleException as e:
        result.stream.setDevice(None)
        if result.buffer.isOpen(): result.buffer.close()
        result.buffer.setBuffer(None)
        result.data = QByteArray()
        result.version = 0
        raise e
    
    result.stream.setDevice(None)
    if result.buffer.isOpen(): result.buffer.close()
    result.buffer.setBuffer(None)
    result.data = data.data
    
    result.buffer.setBuffer(result.data)
    result.buffer.open(QIODevice.OpenModeFlag.ReadOnly)
    result.buffer.seek(data.buffer.pos())
    result.stream.setDevice(result.buffer)
    result.stream.setVersion(QDataStream.Version.Qt_5_1)

    return result

    


def CreateLocalKey(salt : QByteArray, passcode: QByteArray = QByteArray()) -> AuthKey:
    hashKey = hashlib.sha512(salt)
    hashKey.update(passcode)
    hashKey.update(salt)

    iterationsCount = 1 if passcode.isEmpty() else 100000
    return AuthKey(hashlib.pbkdf2_hmac("sha512", hashKey.digest(), salt, iterationsCount, 256))


def aesDecryptLocal(src : QByteArray, authKey : AuthKey, key128 : QByteArray) -> QByteArray:
    aesKey, aesIv = authKey.prepareAES_oldmtp(key128, False)
    decrypted = tgcrypto.ige256_decrypt(src, aesKey, aesIv)
    return QByteArray(decrypted)

def DecryptLocal(encrypted : QByteArray, authKey : AuthKey) -> EncryptedDescriptor:
    encryptedSize = encrypted.size()
    if (encryptedSize <= 16) or (encryptedSize & 0x0F):
        print(encrypted.data().hex())
        raise OpenTeleException(OpenTeleErrorCode.BadEncryptedDataSize, f"Bad encrypted part size: {encryptedSize}")

    fullLen = encryptedSize - 16
    encryptedKey = encrypted[:16]
    encryptedData = encrypted[16:]

    decrypted = aesDecryptLocal(encryptedData, authKey, encryptedKey)
    checkHash = hashlib.sha1(decrypted).digest()[:16]
    if (checkHash != encryptedKey):
        raise OpenTeleException(OpenTeleErrorCode.BadDecryptKey, "Bad decrypt key, data not decrypted - incorrect password?")

    dataLen = int.from_bytes(decrypted[:4], 'little') # *(const uint32*)decrypted.constData();
    if (dataLen > decrypted.size()) or (dataLen <= fullLen - 16) or (dataLen < 4):
        raise OpenTeleException(OpenTeleErrorCode.BadDecryptedDataSize, f"Bad decrypted part size: {encryptedSize}, fullLen: {fullLen}, decrypted size: {decrypted.__len__()}")

    decrypted.resize(dataLen)
    result = EncryptedDescriptor()
    result.data = decrypted

    decrypted = QByteArray()
    
    result.buffer.setBuffer(result.data)
    result.buffer.open(QIODevice.OpenModeFlag.ReadOnly)
    result.buffer.seek(4) # skip len
    result.stream.setDevice(result.buffer)
    result.stream.setVersion(QDataStream.Version.Qt_5_1)

    return result


def ComputeDataNameKey(dataName : str) -> int:
    md5 = hashlib.md5(dataName.encode("utf-8")).digest()
    return int.from_bytes(md5, 'little')

def ToFilePart(val : int):
    result = str()
    for i in range(0, 0x10):
        v = val & 0xF
        if v < 0x0A:
            result += chr(ord('0') + v)
        else:
            result += chr(ord('A') + (v - 0x0A))
        val >>= 4
    return result