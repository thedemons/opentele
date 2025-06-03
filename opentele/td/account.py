from __future__ import annotations

from .configs import *
from . import shared as td

from telethon.network.connection.connection import Connection
from telethon.network.connection.tcpfull import ConnectionTcpFull
from telethon.sessions.abstract import Session

import logging

# if TYPE_CHECKING:
#     from ..opentele import *


class MapData(BaseObject):  # nocov
    def __init__(self, basePath: str) -> None:

        self.basePath = basePath

        self._draftsMap: Dict[PeerId, FileKey] = {}
        self._draftCursorsMap: Dict[PeerId, FileKey] = {}
        self._draftsNotReadMap: Dict[PeerId, bool] = {}

        self._locationsKey = FileKey(0)
        self._trustedBotsKey = FileKey(0)
        self._installedStickersKey = FileKey(0)
        self._featuredStickersKey = FileKey(0)
        self._recentStickersKey = FileKey(0)
        self._favedStickersKey = FileKey(0)
        self._archivedStickersKey = FileKey(0)
        self._archivedMasksKey = FileKey(0)
        self._installedCustomEmojiKey = FileKey(0)
        self._featuredCustomEmojiKey = FileKey(0)
        self._archivedCustomEmojiKey = FileKey(0)
        self._searchSuggestionsKey = FileKey(0)
        self._webviewStorageTokenBots = FileKey(0)
        self._webviewStorageTokenOther = FileKey(0)
        self._savedGifsKey = FileKey(0)
        self._recentStickersKeyOld = FileKey(0)
        self._legacyBackgroundKeyDay = FileKey(0)
        self._legacyBackgroundKeyNight = FileKey(0)

        # self._settingsKey = FileKey(0)
        # ! TO BE ADDED
        self._settingsKey = FileKey(1851671142505648812)
        """MUST HAVE OR CAN'T WRITE MAPDATA, I'M WOKRING TO FIX THIS"""

        self._recentHashtagsAndBotsKey = FileKey(0)
        self._exportSettingsKey = FileKey(0)
        self._installedMasksKey = FileKey(0)
        self._recentMasksKey = FileKey(0)

    def read(self, localKey: td.AuthKey, legacyPasscode: QByteArray) -> None:

        try:
            mapData = td.Storage.ReadFile("map", self.basePath)
        except OpenTeleException as e:
            raise TDataReadMapDataFailed(
                "Could not read map data, find not found or couldn't be opened"
            ) from e

        legacySalt, legacyKeyEncrypted, mapEncrypted = (
            QByteArray(),
            QByteArray(),
            QByteArray(),
        )

        mapData.stream >> legacySalt >> legacyKeyEncrypted >> mapEncrypted

        ExpectStreamStatus(mapData.stream, "Could not stream data from mapData")

        if not localKey:

            # LocalEncryptSaltSize = 32
            Expects(
                legacySalt.size() == 32,
                TDataReadMapDataFailed(
                    f"Bad salt in map file, size: {legacySalt.size()}"
                ),
            )

            legacyPasscodeKey = td.Storage.CreateLegacyLocalKey(
                legacySalt, legacyPasscode
            )

            try:
                keyData = td.Storage.DecryptLocal(legacyKeyEncrypted, legacyPasscodeKey)
            except OpenTeleException as e:
                raise TDataReadMapDataIncorrectPasscode(
                    "Could not decrypt pass-protected key from map file, maybe bad password..."
                ) from e

            localKey = td.AuthKey.FromStream(keyData.stream)

        try:
            map = td.Storage.DecryptLocal(mapEncrypted, localKey)
        except OpenTeleException as e:
            raise TDataReadMapDataFailed("Could not decrypt map data") from e

        selfSerialized = QByteArray()
        draftsMap: typing.Dict[PeerId, FileKey] = {}
        draftCursorsMap: typing.Dict[PeerId, FileKey] = {}
        draftsNotReadMap: typing.Dict[PeerId, bool] = {}

        locationsKey = 0
        reportSpamStatusesKey = 0
        trustedBotsKey = 0
        recentStickersKeyOld = 0
        installedStickersKey = 0
        featuredStickersKey = 0
        recentStickersKey = 0
        favedStickersKey = 0
        archivedStickersKey = 0
        installedMasksKey = 0
        recentMasksKey = 0
        archivedMasksKey = 0
        installedCustomEmojiKey = 0
        featuredCustomEmojiKey = 0
        archivedCustomEmojiKey = 0
        searchSuggestionsKey = 0
        webviewStorageTokenBots = 0
        webviewStorageTokenOther = 0
        savedGifsKey = 0
        legacyBackgroundKeyDay = 0
        legacyBackgroundKeyNight = 0
        userSettingsKey = 0
        recentHashtagsAndBotsKey = 0
        exportSettingsKey = 0

        is_finished = False

        while not is_finished and not map.stream.atEnd():
            keyType = map.stream.readUInt32()

            if keyType == lskType.lskDraft:
                count = map.stream.readUInt32()
                for i in range(count):
                    key = FileKey(map.stream.readUInt64())
                    peerIdSerialized = map.stream.readUInt64()
                    peerId = PeerId.FromSerialized(peerIdSerialized)
                    draftsMap[peerId] = key
                    draftsNotReadMap[peerId] = True

            elif keyType == lskType.lskSelfSerialized:
                map.stream >> selfSerialized

            elif keyType == lskType.lskDraftPosition:
                count = map.stream.readUInt32()
                for i in range(count):
                    key = FileKey(map.stream.readUInt64())
                    peerIdSerialized = map.stream.readUInt64()
                    peerId = PeerId.FromSerialized(peerIdSerialized)
                    draftCursorsMap[peerId] = key

            elif (
                (keyType == lskType.lskLegacyImages)
                or (keyType == lskType.lskLegacyStickerImages)
                or (keyType == lskType.lskLegacyAudios)
            ):
                count = map.stream.readUInt32()
                for i in range(count):
                    filekey = map.stream.readUInt64()
                    first = map.stream.readUInt64()
                    second = map.stream.readUInt64()
                    size = map.stream.readInt32()

            elif keyType == lskType.lskLocations:
                locationsKey = map.stream.readUInt64()

            elif keyType == lskType.lskReportSpamStatusesOld:
                reportSpamStatusesKey = map.stream.readUInt64()
                # ClearKey(reportSpamStatusesKey, _basePath);

            elif keyType == lskType.lskTrustedBots:
                trustedBotsKey = map.stream.readUInt64()

            elif keyType == lskType.lskRecentStickersOld:
                recentStickersKeyOld = map.stream.readUInt64()

            elif keyType == lskType.lskBackgroundOldOld:
                # TO BE ADDED
                # map.stream >> (Window::Theme::IsNightMode()
                #     ? legacyBackgroundKeyNight
                #     : legacyBackgroundKeyDay);
                map.stream >> legacyBackgroundKeyDay

            elif keyType == lskType.lskBackgroundOld:
                legacyBackgroundKeyDay = map.stream.readUInt64()
                legacyBackgroundKeyNight = map.stream.readUInt64()

            elif keyType == lskType.lskUserSettings:
                userSettingsKey = map.stream.readUInt64()

            elif keyType == lskType.lskRecentHashtagsAndBots:
                recentHashtagsAndBotsKey = map.stream.readUInt64()

            elif keyType == lskType.lskStickersOld:
                installedStickersKey = map.stream.readUInt64()

            elif keyType == lskType.lskStickersKeys:
                installedStickersKey = map.stream.readUInt64()
                featuredStickersKey = map.stream.readUInt64()
                recentStickersKey = map.stream.readUInt64()
                archivedStickersKey = map.stream.readUInt64()

            elif keyType == lskType.lskFavedStickers:
                favedStickersKey = map.stream.readUInt64()

            elif keyType == lskType.lskSavedGifsOld:
                key = map.stream.readUInt64()

            elif keyType == lskType.lskSavedGifs:
                savedGifsKey = map.stream.readUInt64()

            elif keyType == lskType.lskSavedPeersOld:
                key = map.stream.readUInt64()

            elif keyType == lskType.lskExportSettings:
                exportSettingsKey = map.stream.readUInt64()

            elif keyType == lskType.lskMasksKeys:
                installedMasksKey = map.stream.readUInt64()
                recentMasksKey = map.stream.readUInt64()
                archivedMasksKey = map.stream.readUInt64()

            elif keyType == lskType.lskCustomEmojiKeys:
                installedCustomEmojiKey = map.stream.readUInt64()
                featuredCustomEmojiKey = map.stream.readUInt64()
                archivedCustomEmojiKey = map.stream.readUInt64()

            elif keyType == lskType.lskSearchSuggestions:
                searchSuggestionsKey = map.stream.readUInt64()

            elif keyType == lskType.lskWebviewTokens:
                is_finished = True

            else:
                logging.warning(f"Unknown key type in encrypted map: {keyType}")

            ExpectStreamStatus(map.stream, "Could not stream data from mapData ")

        self.__localKey = localKey

        self._draftsMap = draftsMap
        self._draftCursorsMap = draftCursorsMap
        self._draftsNotReadMap = draftsNotReadMap

        self._locationsKey = locationsKey
        self._trustedBotsKey = trustedBotsKey
        self._recentStickersKeyOld = recentStickersKeyOld
        self._installedStickersKey = installedStickersKey
        self._featuredStickersKey = featuredStickersKey
        self._recentStickersKey = recentStickersKey
        self._favedStickersKey = favedStickersKey
        self._archivedStickersKey = archivedStickersKey
        self._savedGifsKey = savedGifsKey
        self._installedMasksKey = installedMasksKey
        self._recentMasksKey = recentMasksKey
        self._archivedMasksKey = archivedMasksKey
        self._installedCustomEmojiKey = installedCustomEmojiKey
        self._featuredCustomEmojiKey = featuredCustomEmojiKey
        self._archivedCustomEmojiKey = archivedCustomEmojiKey
        self._searchSuggestionsKey = searchSuggestionsKey
        self._webviewStorageTokenBots = webviewStorageTokenBots
        self._webviewStorageTokenOther = webviewStorageTokenOther
        self._legacyBackgroundKeyDay = legacyBackgroundKeyDay
        self._legacyBackgroundKeyNight = legacyBackgroundKeyNight
        self._settingsKey = userSettingsKey
        self._recentHashtagsAndBotsKey = recentHashtagsAndBotsKey
        self._exportSettingsKey = exportSettingsKey
        self._oldMapVersion = mapData.version

    def prepareToWrite(self) -> td.Storage.EncryptedDescriptor:
        # Intended for internal usage only

        mapSize = 0

        # TO BE ADDED
        # if (!self.isEmpty()) mapSize += sizeof(uint32) + Serialize::bytearraySize(self);
        if len(self._draftsMap) > 0:
            mapSize += sizeof(uint32) * 2 + len(self._draftsMap) * sizeof(uint64) * 2
        if len(self._draftCursorsMap) > 0:
            mapSize += (
                sizeof(uint32) * 2 + len(self._draftCursorsMap) * sizeof(uint64) * 2
            )
        if self._locationsKey:
            mapSize += sizeof(uint32) + sizeof(uint64)
        if self._trustedBotsKey:
            mapSize += sizeof(uint32) + sizeof(uint64)
        if self._recentStickersKeyOld:
            mapSize += sizeof(uint32) + sizeof(uint64)
        if (
            self._installedStickersKey
            or self._featuredStickersKey
            or self._recentStickersKey
            or self._archivedStickersKey
        ):
            mapSize += sizeof(uint32) + 4 * sizeof(uint64)

        if self._favedStickersKey:
            mapSize += sizeof(uint32) + sizeof(uint64)
        if self._savedGifsKey:
            mapSize += sizeof(uint32) + sizeof(uint64)
        if self._settingsKey:
            mapSize += sizeof(uint32) + sizeof(uint64)
        if self._recentHashtagsAndBotsKey:
            mapSize += sizeof(uint32) + sizeof(uint64)
        if self._exportSettingsKey:
            mapSize += sizeof(uint32) + sizeof(uint64)
        if self._installedMasksKey or self._recentMasksKey or self._archivedMasksKey:
            mapSize += sizeof(uint32) + 3 * sizeof(uint64)
        if self._installedCustomEmojiKey or self._featuredCustomEmojiKey or self._archivedCustomEmojiKey:
            mapSize += sizeof(uint32) + 3 * sizeof(uint64)
        if self._searchSuggestionsKey:
            mapSize += sizeof(uint32) + sizeof(uint64)
        if self._webviewStorageTokenBots or self._webviewStorageTokenOther:
            mapSize += sizeof(uint32) + 2 * sizeof(uint64)

        mapData = td.Storage.EncryptedDescriptor(mapSize)
        stream = mapData.stream

        if len(self._draftsMap) > 0:
            stream.writeUInt32(lskType.lskDraft)
            stream.writeUInt32(len(self._draftsMap))
            for key, value in self._draftsMap.items():
                stream.writeUInt64(value)
                stream.writeUInt64(PeerId(key).Serialize())

        if len(self._draftCursorsMap) > 0:
            stream.writeUInt32(lskType.lskDraftPosition)
            stream.writeUInt32(len(self._draftCursorsMap))
            for key, value in self._draftCursorsMap.items():
                stream.writeUInt64(value)
                stream.writeUInt64(PeerId(key).Serialize())

        if self._locationsKey:
            stream.writeUInt32(lskType.lskLocations)
            stream.writeUInt64(self._locationsKey)

        if self._trustedBotsKey:
            stream.writeUInt32(lskType.lskTrustedBots)
            stream.writeUInt64(self._trustedBotsKey)

        if self._recentStickersKeyOld:
            stream.writeUInt32(lskType.lskRecentStickersOld)
            stream.writeUInt64(self._recentStickersKeyOld)

        if (
            self._installedStickersKey
            or self._featuredStickersKey
            or self._recentStickersKey
            or self._archivedStickersKey
        ):
            stream.writeUInt32(lskType.lskStickersKeys)
            stream.writeUInt64(self._installedStickersKey)
            stream.writeUInt64(self._featuredStickersKey)
            stream.writeUInt64(self._recentStickersKey)
            stream.writeUInt64(self._archivedStickersKey)

        if self._favedStickersKey:
            stream.writeUInt32(lskType.lskFavedStickers)
            stream.writeUInt64(self._favedStickersKey)

        if self._savedGifsKey:
            stream.writeUInt32(lskType.lskSavedGifs)
            stream.writeUInt64(self._savedGifsKey)

        if self._settingsKey:
            stream.writeUInt32(lskType.lskUserSettings)
            stream.writeUInt64(self._settingsKey)

        if self._recentHashtagsAndBotsKey:
            stream.writeUInt32(lskType.lskRecentHashtagsAndBots)
            stream.writeUInt64(self._recentHashtagsAndBotsKey)

        if self._exportSettingsKey:
            stream.writeUInt32(lskType.lskExportSettings)
            stream.writeUInt64(self._exportSettingsKey)

        if self._installedMasksKey or self._recentMasksKey or self._archivedMasksKey:
            stream.writeUInt32(lskType.lskMasksKeys)
            stream.writeUInt64(self._installedMasksKey)
            stream.writeUInt64(self._recentMasksKey)
            stream.writeUInt64(self._archivedMasksKey)

        if self._installedCustomEmojiKey or self._featuredCustomEmojiKey or self._archivedCustomEmojiKey:
            stream.writeUInt32(lskType.lskCustomEmojiKeys)
            stream.writeUInt64(self._installedCustomEmojiKey)
            stream.writeUInt64(self._featuredCustomEmojiKey)
            stream.writeUInt64(self._archivedCustomEmojiKey)
        
        if self._searchSuggestionsKey:
            stream.writeUInt32(lskType.lskSearchSuggestions)
            stream.writeUInt64(self._searchSuggestionsKey)

        if self._webviewStorageTokenBots or self._webviewStorageTokenOther:
            stream.writeUInt32(lskType.lskWebviewTokens)
            stream.writeUInt64(self._webviewStorageTokenBots)
            stream.writeUInt64(self._webviewStorageTokenOther)

        return mapData


class StorageAccount(BaseObject):  # nocov
    """
    Storage account for reading and writing to tdata
    """

    def __init__(self, owner: Account, basePath: str, keyFile: str) -> None:
        """
        Create an instance of StorageAccount

        ### Arguments
            1. owner (Account):\n
                owner

            2. basePath (str):\n
                basePath

            3. dataName (str):\n
                dataName
        """

        self.__owner = owner
        self.__keyFile = keyFile
        self.__dataNameKey = td.Storage.ComputeDataNameKey(self.__keyFile)
        self.__baseGlobalPath = td.Storage.GetAbsolutePath(basePath)
        self.__basePath = td.Storage.PathJoin(
            self.__baseGlobalPath, td.Storage.ToFilePart(self.__dataNameKey)
        )
        self.__localKey = None

        self.__mapData = MapData(self.basePath)
        self.__config = td.MTP.Config(td.MTP.Environment.Production)
        # self.mtpData = MtpData()

    @property
    def owner(self) -> Account:
        """
        The TDesktop client that own this account
        """
        return self.__owner

    @property
    def localKey(self) -> Optional[td.AuthKey]:
        """
        The key use to encrypt/decrypt data
        """
        return self.__localKey

    @localKey.setter
    def localKey(self, value):
        # localKey setter is intended for internal usage
        self.__localKey = value

    @property
    def keyFile(self) -> str:
        return self.__keyFile

    @keyFile.setter
    def keyFile(self, value):
        self.__keyFile = value
        self.__dataNameKey = td.Storage.ComputeDataNameKey(self.__keyFile)
        self.baseGlobalPath = self.baseGlobalPath

    @property
    def baseGlobalPath(self) -> str:
        return self.__baseGlobalPath

    @baseGlobalPath.setter
    def baseGlobalPath(self, basePath):
        self.__baseGlobalPath = td.Storage.GetAbsolutePath(basePath)
        self.__basePath = td.Storage.PathJoin(
            self.__baseGlobalPath, td.Storage.ToFilePart(self.__dataNameKey)
        )

    @property
    def basePath(self) -> str:
        return self.__basePath

    @property
    def config(self) -> td.MTP.Config:
        return self.__config

    @property
    def mapData(self) -> MapData:
        return self.__mapData

    def start(self, localKey: td.AuthKey) -> td.MTP.Config:
        # Intended for internal usage only

        self.__localKey = localKey
        self.readMapWith(localKey)

        return (
            self.__config if self.owner.owner.kPerformanceMode else self.readMtpConfig()
        )

    def readMtpData(self):
        # Intended for internal usage only

        # mtp = ReadEncryptedFile(ToFilePart(self.__dataNameKey), self.__basePath, self.localKey)
        mtp = td.Storage.ReadEncryptedFile(td.Storage.ToFilePart(self.__dataNameKey), self.__baseGlobalPath, self.localKey)  # type: ignore

        blockId = mtp.stream.readInt32()

        Expects(blockId == 75, TDataInvalidMagic("Not supported file version"))

        serialized = QByteArray()
        mtp.stream >> serialized
        self.owner._setMtpAuthorization(serialized)

    def readMtpConfig(self) -> td.MTP.Config:
        # Intended for internal usage only
        Expects(
            self.localKey != None,
            AccountAuthKeyNotFound("The localKey has not been initialized yet"),
        )

        try:
            file = td.Storage.ReadEncryptedFile("config", self.basePath, self.localKey)  # type: ignore
            serialized = QByteArray()
            file.stream >> serialized

            ExpectStreamStatus(file.stream, "Could not stream data from MtpConfig")

            self.__config = td.MTP.Config.FromSerialized(serialized)
            return self.__config
        except OpenTeleException as e:
            pass

        return td.MTP.Config(td.MTP.Environment.Production)

    def readMapWith(
        self, localKey: td.AuthKey, legacyPasscode: QByteArray = QByteArray()
    ):
        # Intended for internal usage only
        try:
            self.__mapData.read(localKey, legacyPasscode)
        except OpenTeleException:
            return False

        self.readMtpData()

    def writeMtpConfig(self, basePath: str) -> None:
        # Intended for internal usage only

        Expects(
            self.localKey != None,
            "localKey not found, have you initialized me correctly?",
        )
        Expects(basePath != None and basePath != "", "basePath can't be empty")

        serialized = self.owner.MtpConfig.Serialize()
        size = td.Serialize.bytearraySize(serialized)
        file = td.Storage.FileWriteDescriptor("config", basePath)
        data = td.Storage.EncryptedDescriptor(size)
        data.stream << serialized
        file.writeEncrypted(data, self.localKey)  # type: ignore
        file.finish()

    def writeMap(self, basePath: str) -> None:
        # Intended for internal usage only

        Expects(
            self.localKey != None,
            "localKey not found, have you initialized me correctly?",
        )
        Expects(basePath != None and basePath != "", "basePath can't be empty")

        map = td.Storage.FileWriteDescriptor("map", basePath)

        # i don't know what's the purpose of this, but it's in tdesktop source code
        map.writeData(QByteArray())
        map.writeData(QByteArray())

        mapDataEncrypted = self.mapData.prepareToWrite()
        map.writeEncrypted(mapDataEncrypted, self.localKey)  # type: ignore
        map.finish()

    def writeMtpData(self, baseGlobalPath: str, dataNameKey: int) -> None:
        # Intended for internal usage only

        Expects(
            self.localKey != None,
            "localKey not found, have you initialized me correctly?",
        )
        Expects(
            baseGlobalPath != None and baseGlobalPath != "",
            "baseGlobalPath can't be empty",
        )

        serialized = self.owner.serializeMtpAuthorization()
        size = sizeof(uint32) + td.Serialize.bytearraySize(serialized)
        mtp = td.Storage.FileWriteDescriptor(
            td.Storage.ToFilePart(dataNameKey), baseGlobalPath
        )
        data = td.Storage.EncryptedDescriptor(size)
        data.stream.writeInt32(dbi.MtpAuthorization)
        data.stream << serialized
        mtp.writeEncrypted(data, self.localKey)  # type: ignore
        mtp.finish()

    def _writeData(self, baseGlobalPath: str, keyFile: str = None) -> None:
        # Intended for internal usage only

        Expects(
            baseGlobalPath != None and baseGlobalPath != "",
            "baseGlobalPath can't be empty",
        )

        if keyFile != None and self.keyFile != keyFile:
            self.__keyFile = keyFile
            dataNameKey = td.Storage.ComputeDataNameKey(self.__keyFile)
        else:
            dataNameKey = self.__dataNameKey

        basePath = td.Storage.PathJoin(
            baseGlobalPath, td.Storage.ToFilePart(dataNameKey)
        )
        self.writeMap(basePath)

        if not self.owner.owner.kPerformanceMode:
            self.writeMtpConfig(basePath)

        self.writeMtpData(baseGlobalPath, dataNameKey)


class Account(BaseObject):
    """
    Telegram Desktop account

    ### Attributes:
        api (`API`):
            The API this acount is using.

        authKey (`AuthKey`):
            The authorization key used to authorize this acocunt.

        UserId (`int`):
            User ID of this account.

        MainDcId (`DcId`):
            The main Data Center ID this account connects to.

        basePath (`str`):
            The folder where tdata is stored.

        localKey (`AuthKey`):
            Key used to encrypt and decrypt tdata.

        owner (`TDesktop`):
            `td.TDesktop` client owner of this account.

        keyFile (`str`):
            See `td.TDesktop.keyFile`.

    """

    kWideIdsTag: int = int(~0)

    def __init__(
        self,
        owner: td.TDesktop,
        basePath: str = None,
        api: Union[Type[APIData], APIData] = API.TelegramDesktop,
        keyFile: str = None,
        index: int = 0,
    ) -> None:
        """
        Initialized a `TDesktop` account.

        You should use `TDesktop()` or `TDesktop.FromTelethon()` instead.
        Manually using `Account()` is not recommended. But this is here for your need anyway.

        ### Arguments:
            owner (`TDesktop`):
                `TDesktop` client owner of this account.

            basePath (`str`, default=None):
                The folder where `tdata` is stored.

            api (`API`, default=`TelegramDesktop`):
                Which API to use. Read more `[here](API)`.

            keyFile (`str`, default=None):
                See `TDesktop.keyFile`.

            index (`int`, default=0):
                Index of this account in the `TDesktop` client.

        ### Notes:
            TODO: `prepareToStart()` must be call after initalizing the object.

        """
        self.__owner = owner
        self.__localKey = None
        self.__authKey = None
        self.__telethonClient = None
        self.__isLoaded = False
        self.__isAuthorized = False
        self.__UserId = 0
        self.__MainDcId = DcId(0)

        self.__basePath = td.Storage.GetAbsolutePath(basePath)
        self.__keyFile = keyFile if (keyFile != None) else td.TDesktop.kDefaultKeyFile

        self.__mtpKeys: typing.List[td.AuthKey] = []
        self.__mtpKeysToDestroy: typing.List[td.AuthKey] = []
        self.api = api

        self._local = StorageAccount(
            self, self.basePath, td.Storage.ComposeDataString(self.__keyFile, index)
        )
        self.index = index

    @property
    def api(self) -> APIData:
        """
        The API this acount is using.
        """
        return self.__api

    @api.setter
    def api(self, value) -> None:
        self.__api = value
        if self.owner.api != self.api:
            self.owner.api = self.api

    @property
    def owner(self) -> td.TDesktop:
        """
        TDesktop client owner of this account.
        """
        return self.__owner

    @property
    def basePath(self) -> str:
        """
        The folder where tdata is stored.
        """
        return self.__basePath

    @property
    def keyFile(self) -> str:
        """
        See `TDesktop.keyFile`
        """
        return self.__keyFile

    @keyFile.setter
    def keyFile(self, value):
        self.__keyFile = value
        self._local.keyFile = td.Storage.ComposeDataString(value, self.index)

    @property
    def localKey(self) -> Optional[td.AuthKey]:
        """
        Key used to encrypt and decrypt tdata.
        """
        return self.__localKey

    @localKey.setter
    def localKey(self, value):
        self.__localKey = value
        self._local.localKey = value

    @property
    def authKey(self) -> Optional[td.AuthKey]:
        """
        The authorization key used to authorize this acocunt.
        """
        return self.__authKey

    @property
    def UserId(self) -> int:
        """
        User ID of this account.
        """
        return self.__UserId

    @property
    def MainDcId(self) -> DcId:
        """
        The main Data Center ID this account connects to.
        """
        return self.__MainDcId

    @property
    def MtpConfig(self) -> td.MTP.Config:
        return self._local.config

    @property
    def MapData(self) -> MapData:
        return self._local.mapData

    def isAuthorized(self) -> bool:
        return self.__isAuthorized

    def isLoaded(self) -> bool:
        return self.__isLoaded

    def start(self) -> bool:
        raise NotImplementedError()
        return self.isAuthorized()

    def prepareToStart(self, localKey: td.AuthKey) -> td.MTP.Config:
        """
        Prepare the account before starting it

        ### Arguments:
            localKey (`AuthKey`):
                `API`

        ### Returns:
            `MTP.Config`: [description]
        """

        self.__localKey = localKey
        self.__MtpConfig = self._local.start(localKey)
        return self.__MtpConfig

    def _setMtpAuthorizationCustom(
        self,
        dcId: DcId,
        userId: int,
        mtpKeys: List[td.AuthKey],
        mtpKeysToDestroy: List[td.AuthKey] = [],
    ):
        # Intended for internal usage only

        self.__MainDcId = dcId
        self.__UserId = userId
        self.__mtpKeys = mtpKeys

        for key in self.__mtpKeys:
            if key.dcId == self.MainDcId:
                self.__authKey = key
                break

        Expects(
            self.authKey != None,
            exception=TDataAuthKeyNotFound(
                "Could not find the main authKey, are you sure the data is correct?"
            ),
        )

        self.__isLoaded = True

    def _setMtpAuthorization(self, serialized: QByteArray):
        # Intended for internal usage only
        stream = QDataStream(serialized)
        stream.setVersion(QDataStream.Version.Qt_5_1)

        self.__UserId = stream.readInt32()
        self.__MainDcId = DcId(stream.readInt32())

        if ((self.__UserId << 32) | self.__MainDcId) == Account.kWideIdsTag:
            self.__UserId = stream.readUInt64()
            self.__MainDcId = DcId(stream.readInt32())

        Expects(
            stream.status() == QDataStream.Status.Ok,
            QDataStreamFailed("Could not read main fields from mtp authorization."),
        )

        def readKeys(keys: typing.List[td.AuthKey]):

            key_count = stream.readInt32()
            Expects(
                stream.status() == QDataStream.Status.Ok,
                QDataStreamFailed("Could not read keys count from mtp authorization."),
            )

            for i in range(key_count):
                dcId = DcId(stream.readInt32())
                keys.append(
                    td.AuthKey.FromStream(stream, td.AuthKeyType.ReadFromFile, dcId)
                )

        self.__mtpKeys.clear()
        self.__mtpKeysToDestroy.clear()

        readKeys(self.__mtpKeys)
        readKeys(self.__mtpKeysToDestroy)

        for key in self.__mtpKeys:
            if key.dcId == self.MainDcId:
                self.__authKey = key
                break

        Expects(
            self.__authKey != None,
            exception=TDataAuthKeyNotFound(
                "Could not find authKey, the data might has been corrupted"
            ),
        )

        self.__isLoaded = True
        # TO BE ADDED
        # while (not mtp.stream.atEnd()):
        #     blockId = mtp.stream.readInt32()
        #     if mtp.stream.status() != 0:
        #         raise OpenTeleException(OpenTeleErrorCode.QDataStreamFailed, "Failed to stream mtpData")
        #     print(blockId)

    def serializeMtpAuthorization(self) -> QByteArray:
        # Intended for internal usage only
        Expects(self.isLoaded(), "Account data not loaded yet")

        def keysSize(list: typing.List[td.AuthKey]):
            return 4 + len(list) * (4 + td.AuthKey.kSize)

        def writeKeys(stream: QDataStream, keys: typing.List[td.AuthKey]):

            stream.writeInt32(len(keys))
            for key in keys:
                stream.writeInt32(key.dcId)
                stream.writeRawData(key.key)

        result = QByteArray()
        stream = QDataStream(result, QIODevice.OpenModeFlag.WriteOnly)
        stream.setVersion(QDataStream.Version.Qt_5_1)

        stream.writeInt64(Account.kWideIdsTag)
        stream.writeInt64(self.UserId)
        stream.writeInt32(self.MainDcId)

        writeKeys(stream, self.__mtpKeys)
        writeKeys(stream, self.__mtpKeysToDestroy)
        return result

    def _writeData(self, baseGlobalPath: str, keyFile: str = None) -> None:
        # Intended for internal usage only

        self._local._writeData(baseGlobalPath, keyFile)

    def SaveTData(
        self, basePath: str = None, passcode: str = None, keyFile: str = None
    ) -> None:
        """
        Save this account to a folder

        ### Arguments:
            basePath (`str`, default=`None`):
                The path to the folder. Defaults to None.

            passcode (`str`, default=`None`):
                Lock the data with a passcode. Defaults to None.

            keyFile (`str`, default=`None`):
                See `TDesktop.keyFile`

        ### Examples
            Add an account to `TDesktop` and save it to `tdata`:
        ```python
            telethonClient = TelegramClient("sessionFile", API_ID, API_HASH)
            td = TDesktop("new_tdata")
            account = Account.FromTelethon(telethonClient, owner=td) # add this account to td
            td.SaveTData()
        ```
        """

        if basePath == None:
            basePath = self.basePath

        basePath = td.Storage.GetAbsolutePath(basePath)

        if self.basePath == None:
            self.__basePath = basePath

        self.owner.SaveTData(basePath, passcode, keyFile)

    # @extend_class
    # class Account(Account):

    @typing.overload
    async def ToTelethon(
        self,
        session: Union[str, Session] = None,
        flag: Type[LoginFlag] = CreateNewSession,
        api: Union[Type[APIData], APIData] = API.TelegramDesktop,
        password: str = None,
    ) -> tl.TelegramClient:
        pass

    @typing.overload
    async def ToTelethon(
        self,
        session: Union[str, Session] = None,
        flag: Type[LoginFlag] = CreateNewSession,
        api: Union[Type[APIData], APIData] = API.TelegramDesktop,
        password: str = None,
        *,
        connection: typing.Type[Connection] = ConnectionTcpFull,
        use_ipv6: bool = False,
        proxy: Union[tuple, dict] = None,
        local_addr: Union[str, tuple] = None,
        timeout: int = 10,
        request_retries: int = 5,
        connection_retries: int = 5,
        retry_delay: int = 1,
        auto_reconnect: bool = True,
        sequential_updates: bool = False,
        flood_sleep_threshold: int = 60,
        raise_last_call_error: bool = False,
        loop: asyncio.AbstractEventLoop = None,
        base_logger: Union[str, logging.Logger] = None,
        receive_updates: bool = True,
    ) -> tl.TelegramClient:
        pass

    async def ToTelethon(
        self,
        session: Union[str, Session] = None,
        flag: Type[LoginFlag] = CreateNewSession,
        api: Union[Type[APIData], APIData] = API.TelegramDesktop,
        password: str = None,
        **kwargs,
    ) -> tl.TelegramClient:

        Expects(
            self.isLoaded(),
            TDAccountNotLoaded(
                "I'm not loaded yet, are you sure you're using me correctly?"
            ),
        )

        return await tl.TelegramClient.FromTDesktop(
            self, session=session, flag=flag, api=api, password=password, **kwargs
        )

    @staticmethod
    async def FromTelethon(
        telethonClient: tl.TelegramClient,
        flag: Type[LoginFlag] = CreateNewSession,
        api: Union[Type[APIData], APIData] = API.TelegramDesktop,
        password: str = None,
        owner: td.TDesktop = None,
    ):

        Expects(
            (flag == CreateNewSession) or (flag == UseCurrentSession),
            LoginFlagInvalid("LoginFlag invalid"),
        )

        if flag == CreateNewSession:
            if not telethonClient.is_connected():
                try:
                    await telethonClient.connect()
                except OSError as e:
                    raise TelethonUnauthorized(
                        "Could not connect telethon client to the server, please try to connect manually"
                    ) from e

                Expects(
                    await telethonClient.is_user_authorized(),
                    exception=TelethonUnauthorized(
                        "Telethon client is unauthorized, it need to be authorized first"
                    ),
                )

            copy = await telethonClient.QRLoginToNewClient(api=api, password=password)
            await copy.get_me()
        else:
            copy = telethonClient

        ss = copy.session
        authKey = ss.auth_key.key
        dcId = DcId(ss.dc_id)
        userId = copy.UserId
        authKey = td.AuthKey(authKey, td.AuthKeyType.ReadFromFile, dcId)
        
        if userId == None:
            await copy.connect()
            await copy.get_me()
            userId = copy.UserId
            
        newAccount = None

        if owner != None:

            Expects(
                owner.accountsCount < td.TDesktop.kMaxAccounts,
                exception=MaxAccountLimit(
                    "You can't have more than 3 accounts in one TDesktop clent.\n"
                    "Please create another instance of TDesktop or use Account.FromTelethon() to create an Account() independently"
                ),
            )

            index = owner.accountsCount
            newAccount = Account(
                owner=owner,
                basePath=owner.basePath,
                api=api,
                keyFile=owner.keyFile,
                index=index,
            )
            newAccount._setMtpAuthorizationCustom(dcId, userId, [authKey])  # type: ignore
            owner._addSingleAccount(newAccount)

        else:
            index = 0
            newOwner = td.TDesktop()
            newAccount = Account(owner=newOwner, api=api, index=index)
            newAccount._setMtpAuthorizationCustom(dcId, userId, [authKey])  # type: ignore
            newOwner._addSingleAccount(newAccount)

        return newAccount
