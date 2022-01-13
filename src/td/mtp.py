from __future__ import annotations

from .configs import *
from . import shared as td




class MTP(BaseObject):
    '''
    MTProto Protocal
    https://core.telegram.org/mtproto
    '''


    class Environment(int):
        '''
        Enviroment flag for MTP.Config
        '''
        Production = 0
        Test = 1
    
    class RSAPublicKey(BaseObject):
        '''
        To be added
        '''
    
    class DcOptions(BaseObject):
        '''
        Data Center Options, providing information about DC ip, port,.. etc
        '''
        
        kVersion = 2

        def __init__(self, enviroment : MTP.Environment) -> None:
            self._enviroment = enviroment
            self._publicKeys : typing.Dict[DcId, MTP.RSAPublicKey] = {}
            self._cdnPublicKeys : typing.Dict[DcId, MTP.RSAPublicKey] = {}
            self._data : typing.Dict[DcId, typing.List[MTP.DcOptions.Endpoint]] = {}

            self.constructFromBuiltIn()

        def isTestMode(self):
            return self._enviroment != MTP.Environment.Production
        
        def constructAddOne(self, id : int, flags : MTP.DcOptions.Flag, ip : str, port : int, secret : bytes):
            self.applyOneGuarded(DcId.BareDcId(id), flags, ip, port, secret)

        def applyOneGuarded(self, id : int, flags : MTP.DcOptions.Flag, ip : str, port : int, secret : bytes):
    
            if not id in self._data:
                self._data[id] = []
            else:
                for endpoint in self._data[id]:
                    if (endpoint.ip == ip) and (endpoint.port == port):
                        # skip this endpoint because it's already exists in the self._data
                        continue

            endpoint = MTP.DcOptions.Endpoint(id, flags, ip, port, bytes())
            self._data[id].append(endpoint)
            
        def constructFromBuiltIn(self) -> None:

            # TO BE ADDED
            # self.readBuiltInPublicKeys()

            def addToData(dcs : typing.List[BuiltInDc], flags : MTP.DcOptions.Flag):

                for dc in dcs:
                    self.applyOneGuarded(dc.id, flags, dc.ip, dc.port, bytes())

            if self.isTestMode():
                addToData(BuiltInDc.kBuiltInDcsTest, MTP.DcOptions.Flag.f_static | 0)
                addToData(BuiltInDc.kBuiltInDcsIPv6Test, MTP.DcOptions.Flag.f_static | MTP.DcOptions.Flag.f_ipv6)
            else:
                addToData(BuiltInDc.kBuiltInDcs, MTP.DcOptions.Flag.f_static | 0)
                addToData(BuiltInDc.kBuiltInDcsIPv6, MTP.DcOptions.Flag.f_static | MTP.DcOptions.Flag.f_ipv6)
            
        def constructFromSerialized(self, serialized : QByteArray):
            stream = QDataStream(serialized)
            stream.setVersion(QDataStream.Version.Qt_5_1)

            minusVersion = stream.readInt32()
            version = (-minusVersion) if (minusVersion < 0) else 0
            
            count = stream.readInt32() if version > 0 else minusVersion

            self._data.clear()

            for i in range(0, count):
                id = stream.readInt32()
                flags = stream.readInt32()
                port = stream.readInt32()
                ipSize = stream.readInt32()

                kMaxIpSize = 45
                Expects(condition=((ipSize > 0) and (ipSize <= kMaxIpSize)),
                        exception=TDataBadConfigData("Bad ipSize data"))

                ip = stream.readRawData(ipSize).decode("ascii")

                kMaxSecretSize = 32
                secret = bytes()
                if (version > 0):
                    secretSize = stream.readInt32()
                    
                    Expects(condition=((secretSize >= 0) and (secretSize <= kMaxSecretSize)),
                            exception=TDataBadConfigData("Bad secretSize data"))
                    
                    if secretSize > 0:
                        secret = stream.readRawData(secretSize)

                ExpectStreamStatus(stream, "Could not stream config data")

                self.applyOneGuarded(id, flags, ip, port, secret)

            # TO BE ADDED
            # Read CDN config

        def Serialize(self) -> QByteArray:
            
            optionsCount = 0
            for dcId, endpoints in self._data.items():
                if DcId.BareDcId(dcId) > 1000:
                    continue
                optionsCount += len(endpoints)

            result = QByteArray()
            stream = QDataStream(result, QIODevice.OpenModeFlag.WriteOnly)
            stream.setVersion(QDataStream.Version.Qt_5_1)

            stream.writeInt32(-MTP.DcOptions.kVersion) # -2
            
		    # Dc options.
            stream.writeInt32(optionsCount)
            for dcId, endpoints in self._data.items():
                if DcId.BareDcId(dcId) > 1000:
                    continue

                # write endpoints
                for endpoint in endpoints:
                    stream.writeInt32(endpoint.id)
                    stream.writeInt32(endpoint.flags)

                    stream.writeInt32(len(endpoint.ip))
                    stream.writeRawData(endpoint.ip.encode("ascii"))

                    stream.writeInt32(len(endpoint.secret))
                    stream.writeRawData(endpoint.secret)
            
            # CDN public keys.
            # TO BE ADDED
            publicKeys = []
            stream.writeInt32(len(publicKeys))

            # for (auto &key : publicKeys) {
            #     stream << qint32(key.dcId)
            #         << Serialize::bytes(key.n)
            #         << Serialize::bytes(key.e);
            # }

            return result



        
        class Address(int):
            '''
            Flag used for MTP.DcOptions.Endpoint
            '''
            IPv4 = 0
            IPv6 = 1

        class Protocol(int):
            '''
            Flag used for MTP.DcOptions.Endpoint
            '''
            Tcp = 0
            Http = 1

        class Flag(int):
            '''
            Flag used for MTP.DcOptions.Endpoint
            '''
            f_ipv6 = 1 << 0
            f_media_only = 1 << 1
            f_tcpo_only = 1 << 2
            f_cdn = 1 << 3
            f_static = 1 << 4
            f_secret = 1 << 10
            MAX_FIELD = 1 << 10

        class Endpoint(BaseObject):
            '''
            Data center endpoint information
            '''
            def __init__(self, id : int, flags : MTP.DcOptions.Flag, ip : str, port : int, secret : bytes) -> None:
                self.id = id
                self.flags = flags
                self.ip = ip
                self.port = port
                self.secret = secret
                
                
    class ConfigFields(BaseObject):
        '''
        Configuration data for MTP.Config
        '''
        def __init__(self) -> None:
            self.chatSizeMax = 200
            self.megagroupSizeMax = 10000
            self.forwardedCountMax = 100
            self.onlineUpdatePeriod = 120000
            self.offlineBlurTimeout = 5000
            self.offlineIdleTimeout = 30000
            self.onlineFocusTimeout = 1000 # Not from the server config.
            self.onlineCloudTimeout = 300000
            self.notifyCloudDelay = 30000
            self.notifyDefaultDelay = 1500
            self.savedGifsLimit = 200
            self.editTimeLimit = 172800
            self.revokeTimeLimit = 172800
            self.revokePrivateTimeLimit = 172800
            self.revokePrivateInbox = False
            self.stickersRecentLimit = 30
            self.stickersFavedLimit = 5
            self.pinnedDialogsCountMax = 5
            self.pinnedDialogsInFolderMax = 100
            self.internalLinksDomain = "https://t.me/"
            self.channelsReadMediaPeriod = 86400 * 7
            self.callReceiveTimeoutMs = 20000
            self.callRingTimeoutMs = 90000
            self.callConnectTimeoutMs = 30000
            self.callPacketTimeoutMs = 10000
            self.webFileDcId = 4
            self.txtDomainString = str()
            self.phoneCallsEnabled = True
            self.blockedMode = False
            self.captionLengthMax = 1024
        
    class Config(BaseObject):
        '''
        Configuration of MTProto
        '''
        
        kVersion = 1

        def __init__(self, enviroment : MTP.Environment) -> None:
            self._dcOptions = MTP.DcOptions(enviroment)
            self._fields = MTP.ConfigFields()
            self._fields.webFileDcId = 2 if self._dcOptions.isTestMode() else 4
            self._fields.txtDomainString =  "tapv3.stel.com" if self._dcOptions.isTestMode() else "apv3.stel.com"

        def endpoints(self, dcId : DcId = 0) -> Dict[MTP.DcOptions.Address, Dict[MTP.DcOptions.Protocol, List[MTP.DcOptions.Endpoint]]]:

            endpoints = self._dcOptions._data[dcId]

            Address = MTP.DcOptions.Address
            Protocol = MTP.DcOptions.Protocol
            Flag = MTP.DcOptions.Flag
            Endpoint = MTP.DcOptions.Endpoint

            results : Dict[Address, Dict[Protocol, List[Endpoint]]] = {}
            results[Address.IPv4] = {Protocol.Tcp : [], Protocol.Http : []}
            results[Address.IPv6] = {Protocol.Tcp : [], Protocol.Http : []}

            for endpoint in endpoints:

                if dcId == 0 or endpoint.id == dcId:

                    flags = endpoint.flags
                    address = Address.IPv6 if (flags & Flag.f_ipv6) else Address.IPv4
                    results[address][Protocol.Tcp].append(endpoint)

                    if ( not (flags & (Flag.f_tcpo_only | Flag.f_secret))):
                        results[address][Protocol.Http].append(endpoint)
            
            return results

        def Serialize(self) -> QByteArray:
            options = self._dcOptions.Serialize()
            size = sizeof(int32) * 2
            size += td.Serialize.bytearraySize(options)
            size += 28 * sizeof(int32)
            size += td.Serialize.stringSize(self._fields.internalLinksDomain)
            size += td.Serialize.stringSize(self._fields.txtDomainString)

            result = QByteArray()
            stream = QDataStream(result, QIODevice.OpenModeFlag.WriteOnly)
            stream.setVersion(QDataStream.Version.Qt_5_1)

            stream.writeInt32(MTP.Config.kVersion)
            stream.writeInt32(MTP.Environment.Test if self._dcOptions.isTestMode() else MTP.Environment.Production)
            
            stream << options
            
            stream.writeInt32(self._fields.chatSizeMax)
            stream.writeInt32(self._fields.megagroupSizeMax)
            stream.writeInt32(self._fields.forwardedCountMax)
            stream.writeInt32(self._fields.onlineUpdatePeriod)
            stream.writeInt32(self._fields.offlineBlurTimeout)
            stream.writeInt32(self._fields.offlineIdleTimeout)
            stream.writeInt32(self._fields.onlineFocusTimeout)
            stream.writeInt32(self._fields.onlineCloudTimeout)
            stream.writeInt32(self._fields.notifyCloudDelay)
            stream.writeInt32(self._fields.notifyDefaultDelay)
            stream.writeInt32(self._fields.savedGifsLimit)
            stream.writeInt32(self._fields.editTimeLimit)
            stream.writeInt32(self._fields.revokeTimeLimit)
            stream.writeInt32(self._fields.revokePrivateTimeLimit)
            stream.writeInt32(1 if self._fields.revokePrivateInbox else 0)
            stream.writeInt32(self._fields.stickersRecentLimit)
            stream.writeInt32(self._fields.stickersFavedLimit)
            stream.writeInt32(self._fields.pinnedDialogsCountMax)
            stream.writeInt32(self._fields.pinnedDialogsInFolderMax)
            stream.writeQString(self._fields.internalLinksDomain)
            # stream << self._fields.internalLinksDomain
            stream.writeInt32(self._fields.channelsReadMediaPeriod)
            stream.writeInt32(self._fields.callReceiveTimeoutMs)
            stream.writeInt32(self._fields.callRingTimeoutMs)
            stream.writeInt32(self._fields.callConnectTimeoutMs)
            stream.writeInt32(self._fields.callPacketTimeoutMs)
            stream.writeInt32(self._fields.webFileDcId)
            stream.writeQString(self._fields.txtDomainString)
            # stream << self._fields.txtDomainString
            stream.writeInt32(1 if self._fields.phoneCallsEnabled else 0)
            stream.writeInt32(1 if self._fields.blockedMode else 0)
            stream.writeInt32(self._fields.captionLengthMax)

            return result



        @staticmethod
        def FromSerialized(serialized : QByteArray) -> MTP.Config:
            
            stream = QDataStream(serialized)
            stream.setVersion(QDataStream.Version.Qt_5_1)

            version = stream.readInt32()
            Expects(version == MTP.Config.kVersion, "version != kVersion, something went wrong")
            
            enviroment : DcId = stream.readInt32()
            result = MTP.Config(enviroment)

                        
            def read(field):
                vtype = type(field)
                if (vtype == int):
                    return stream.readInt32()
                elif (vtype == bool):
                    return stream.readInt32() == 1
                elif (vtype == str):
                    return stream.readQString()
                    
            dcOptionsSerialized = QByteArray()
            stream >> dcOptionsSerialized

            fileds = result._fields
            fileds.chatSizeMax              = read(fileds.chatSizeMax)
            fileds.megagroupSizeMax         = read(fileds.megagroupSizeMax)
            fileds.forwardedCountMax        = read(fileds.forwardedCountMax)
            fileds.onlineUpdatePeriod       = read(fileds.onlineUpdatePeriod)
            fileds.offlineBlurTimeout       = read(fileds.offlineBlurTimeout)
            fileds.offlineIdleTimeout       = read(fileds.offlineIdleTimeout)
            fileds.onlineFocusTimeout       = read(fileds.onlineFocusTimeout)
            fileds.onlineCloudTimeout       = read(fileds.onlineCloudTimeout)
            fileds.notifyCloudDelay         = read(fileds.notifyCloudDelay)
            fileds.notifyDefaultDelay       = read(fileds.notifyDefaultDelay)
            fileds.savedGifsLimit           = read(fileds.savedGifsLimit)
            fileds.editTimeLimit            = read(fileds.editTimeLimit)
            fileds.revokeTimeLimit          = read(fileds.revokeTimeLimit)
            fileds.revokePrivateTimeLimit   = read(fileds.revokePrivateTimeLimit)
            fileds.revokePrivateInbox       = read(fileds.revokePrivateInbox)
            fileds.stickersRecentLimit      = read(fileds.stickersRecentLimit)
            fileds.stickersFavedLimit       = read(fileds.stickersFavedLimit)
            fileds.pinnedDialogsCountMax    = read(fileds.pinnedDialogsCountMax)
            fileds.pinnedDialogsInFolderMax = read(fileds.pinnedDialogsInFolderMax)
            fileds.internalLinksDomain      = read(fileds.internalLinksDomain)
            fileds.channelsReadMediaPeriod  = read(fileds.channelsReadMediaPeriod)
            fileds.callReceiveTimeoutMs     = read(fileds.callReceiveTimeoutMs)
            fileds.callRingTimeoutMs        = read(fileds.callRingTimeoutMs)
            fileds.callConnectTimeoutMs     = read(fileds.callConnectTimeoutMs)
            fileds.callPacketTimeoutMs      = read(fileds.callPacketTimeoutMs)
            fileds.webFileDcId              = read(fileds.webFileDcId)
            fileds.txtDomainString          = read(fileds.txtDomainString)
            fileds.phoneCallsEnabled        = read(fileds.phoneCallsEnabled)
            fileds.blockedMode              = read(fileds.blockedMode)
            fileds.captionLengthMax         = read(fileds.captionLengthMax)

            # print(fileds.chatSizeMax)
            # print(fileds.megagroupSizeMax)
            # print(fileds.forwardedCountMax)
            # print(fileds.onlineUpdatePeriod)
            # print(fileds.offlineBlurTimeout)
            # print(fileds.offlineIdleTimeout)
            # print(fileds.onlineFocusTimeout)
            # print(fileds.onlineCloudTimeout)
            # print(fileds.notifyCloudDelay)
            # print(fileds.notifyDefaultDelay)
            # print(fileds.savedGifsLimit)
            # print(fileds.editTimeLimit)
            # print(fileds.revokeTimeLimit)
            # print(fileds.revokePrivateTimeLimit)
            # print(fileds.revokePrivateInbox)
            # print(fileds.stickersRecentLimit)
            # print(fileds.stickersFavedLimit)
            # print(fileds.pinnedDialogsCountMax)
            # print(fileds.pinnedDialogsInFolderMax)
            # print(fileds.internalLinksDomain)
            # print(fileds.channelsReadMediaPeriod)
            # print(fileds.callReceiveTimeoutMs)
            # print(fileds.callRingTimeoutMs)
            # print(fileds.callConnectTimeoutMs)
            # print(fileds.callPacketTimeoutMs)
            # print(fileds.webFileDcId)
            # print(fileds.txtDomainString)
            # print(fileds.phoneCallsEnabled)
            # print(fileds.blockedMode)
            # print(fileds.captionLengthMax)

            ExpectStreamStatus(stream, "Could not stream MtpData serialized")
            result._dcOptions.constructFromSerialized(dcOptionsSerialized)
            return result
        


