
from enum import Enum, IntEnum
import hashlib
import typing

class AuthKey:

    class Type(Enum):
        Generated       : int = 0
        Temporary       : int = 1
        ReadFromFile    : int = 2
        Local           : int = 3

    def __init__(self, key : bytes, type : int = 0, dcId : int = 0) -> None:
        self.__type = type
        self.__dcId = dcId
        self.__key = key
        # if (type == self.Type.Generated) or (type == self.Type.Temporary):
            # self.__creationtime = ...
        self.__countKeyId()

    def __countKeyId(self) -> None:
        hash = hashlib.sha1(self.__key).digest()
        self.__keyId = int.from_bytes(hash[12:12+8], 'little')
    
    def prepareAES_oldmtp(self, msgKey : bytes, send : bool) -> typing.Tuple[bytes, bytes]:
        x = 0 if send else 8
        sha1_a = hashlib.sha1(msgKey[:16] + self.__key[x : x+32]).digest()
        sha1_b = hashlib.sha1(self.__key[x+32 : x+32+16] + msgKey[:16] + self.__key[x+48 : x+48+16]).digest()
        sha1_c = hashlib.sha1(self.__key[x+64 : x+64+32] + msgKey[:16]).digest()
        sha1_d = hashlib.sha1(msgKey[:16] + self.__key[x+96 : x+96+32]).digest()

        aesKey = sha1_a[:8] + sha1_b[8:8+12] + sha1_c[4:4+12]
        aesIv = sha1_a[8:8+12] + sha1_b[:8] + sha1_c[16:16+4] + sha1_d[:8]

        return aesKey, aesIv

    @property
    def key(self):
        return self.__key