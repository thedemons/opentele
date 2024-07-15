from __future__ import annotations

from enum import IntEnum

from ..exception import *
from ..utils import *
from ..api import *
from .. import tl

from typing import (
    Union,
    Callable,
    TypeVar,
    Type,
    Optional,
    List,
    Dict,
    Any,
    TYPE_CHECKING,
)
from ctypes import (
    sizeof,
    c_int32 as int32,
    c_int64 as int64,
    c_uint32 as uint32,
    c_uint64 as uint64,
    c_short as short,
    c_ushort as ushort,
)
from PyQt5.QtCore import (
    QByteArray,
    QDataStream,
    QBuffer,
    QIODevice,
    QSysInfo,
    QDir,
    QFile,
)
from types import FunctionType

import asyncio


APP_VERSION = 3004000
TDF_MAGIC = b"TDF$"


_T = TypeVar("_T")
_T2 = TypeVar("_T2")
_TCLS = TypeVar("_TCLS", bound=type)
_RT = TypeVar("_RT")

_F = TypeVar("_F", bound=Callable[..., Any])


class BareId(int):  # nocov
    """
    BareId
    """


class ChatIdType(BaseObject):  # nocov
    """
    ChatIdType
    """

    bare = BareId(0)
    kShift = BareId(0)
    kReservedBit = BareId(0x80)

    def __init__(self, value: BareId) -> None:
        self.bare = value


class UserId(ChatIdType):  # nocov
    kShift = BareId(0)


class ChatId(ChatIdType):  # nocov
    kShift = BareId(1)


class ChannelId(ChatIdType):  # nocov
    kShift = BareId(2)


class FakeChatId(ChatIdType):  # nocov
    kShift = BareId(0x7F)


class PeerId(int):  # nocov
    """
    PeerId
    """

    kChatTypeMask = BareId(0xFFFFFFFFFFFF)

    def __init__(self, value) -> None:
        self.value = value

    def Serialize(self):
        Expects(not (self.value & (UserId.kReservedBit << 48)))
        return self.value | (UserId.kReservedBit << 48)

    @staticmethod
    def FromChatIdType(
        id: typing.Union[UserId, ChatId, ChannelId, FakeChatId]
    ) -> PeerId:
        return PeerId(id.bare | (BareId(id.kShift) << 48))

    @staticmethod
    def FromSerialized(serialized: int) -> PeerId:
        flag = UserId.kReservedBit << 48
        legacy = not (serialized & (UserId.kReservedBit << 48))

        if not legacy:
            return PeerId(serialized & (~flag))

        PeerIdMask = int(0xFFFFFFFF)
        PeerIdTypeMask = 0xF00000000
        PeerIdUserShift = 0x000000000
        PeerIdChatShift = 0x100000000
        PeerIdChannelShift = 0x200000000
        PeerIdFakeShift = 0xF00000000

        if (serialized & PeerIdTypeMask) == PeerIdUserShift:
            return PeerId.FromChatIdType(UserId(BareId(serialized & PeerIdMask)))

        elif (serialized & PeerIdTypeMask) == PeerIdChatShift:
            return PeerId.FromChatIdType(ChatId(BareId(serialized & PeerIdMask)))

        elif (serialized & PeerIdTypeMask) == PeerIdChannelShift:
            return PeerId.FromChatIdType(ChannelId(BareId(serialized & PeerIdMask)))

        elif (serialized & PeerIdTypeMask) == PeerIdFakeShift:
            return PeerId.FromChatIdType(FakeChatId(BareId(serialized & PeerIdMask)))

        return PeerId(0)


class FileKey(int):  # nocov
    pass


class DcId(int):  # nocov
    """
    Data Center ID
    """

    kDcShift: DcId = 10000  # type: ignore
    Invalid: DcId = 0  # type: ignore
    _0: DcId = 0  # type: ignore
    _1: DcId = 1  # type: ignore
    _2: DcId = 2  # type: ignore
    _3: DcId = 3  # type: ignore
    _4: DcId = 4  # type: ignore
    _5: DcId = 5  # type: ignore

    @staticmethod
    def BareDcId(shiftedDcId: Union[ShiftedDcId, DcId]) -> DcId:
        return DcId(shiftedDcId % DcId.kDcShift)


class ShiftedDcId(DcId):  # nocov
    """
    Shifted Data Center ID
    """

    @staticmethod
    def ShiftDcId(dcId: DcId, value: int) -> ShiftedDcId:
        return ShiftedDcId(dcId + DcId.kDcShift * value)


class BuiltInDc(BaseObject):  # type: ignore # nocov
    """
    Default DC that is hard-coded
    """

    def __init__(self, id: DcId, ip: str, port: int):
        self.id = id
        self.ip = ip
        self.port = port


class BuiltInDc(BuiltInDc):  # nocov
    kBuiltInDcs = [
        BuiltInDc(DcId._1, "149.154.175.50", 443),
        BuiltInDc(DcId._2, "149.154.167.51", 443),
        BuiltInDc(DcId._2, "95.161.76.100", 443),
        BuiltInDc(DcId._3, "149.154.175.100", 443),
        BuiltInDc(DcId._4, "149.154.167.91", 443),
        BuiltInDc(DcId._5, "149.154.171.5", 443),
    ]

    kBuiltInDcsIPv6 = [
        BuiltInDc(DcId._1, "2001:0b28:f23d:f001:0000:0000:0000:000a", 443),
        BuiltInDc(DcId._2, "2001:067c:04e8:f002:0000:0000:0000:000a", 443),
        BuiltInDc(DcId._3, "2001:0b28:f23d:f003:0000:0000:0000:000a", 443),
        BuiltInDc(DcId._4, "2001:067c:04e8:f004:0000:0000:0000:000a", 443),
        BuiltInDc(DcId._5, "2001:0b28:f23f:f005:0000:0000:0000:000a", 443),
    ]

    kBuiltInDcsTest = [
        BuiltInDc(DcId._1, "149.154.175.10", 443),
        BuiltInDc(DcId._2, "149.154.167.40", 443),
        BuiltInDc(DcId._3, "149.154.175.117", 443),
    ]

    kBuiltInDcsIPv6Test = [
        BuiltInDc(DcId._1, "2001:0b28:f23d:f001:0000:0000:0000:000e", 443),
        BuiltInDc(DcId._2, "2001:067c:04e8:f002:0000:0000:0000:000e", 443),
        BuiltInDc(DcId._3, "2001:0b28:f23d:f003:0000:0000:0000:000e", 443),
    ]


class dbi(int):  # nocov
    Key = 0x00
    User = 0x01
    DcOptionOldOld = 0x02
    ChatSizeMaxOld = 0x03
    MutePeerOld = 0x04
    SendKeyOld = 0x05
    AutoStart = 0x06
    StartMinimized = 0x07
    SoundFlashBounceNotifyOld = 0x08
    WorkModeOld = 0x09
    SeenTrayTooltip = 0x0A
    DesktopNotifyOld = 0x0B
    AutoUpdate = 0x0C
    LastUpdateCheck = 0x0D
    WindowPositionOld = 0x0E
    ConnectionTypeOldOld = 0x0F
    # 0x10 reserved
    DefaultAttach = 0x11
    CatsAndDogsOld = 0x12
    ReplaceEmojiOld = 0x13
    AskDownloadPathOld = 0x14
    DownloadPathOldOld = 0x15
    ScaleOld = 0x16
    EmojiTabOld = 0x17
    RecentEmojiOldOldOld = 0x18
    LoggedPhoneNumberOld = 0x19
    MutedPeersOld = 0x1A
    # 0x1b reserved
    NotifyViewOld = 0x1C
    SendToMenu = 0x1D
    CompressPastedImageOld = 0x1E
    LangOld = 0x1F
    LangFileOld = 0x20
    TileBackgroundOld = 0x21
    AutoLockOld = 0x22
    DialogLastPath = 0x23
    RecentEmojiOldOld = 0x24
    EmojiVariantsOldOld = 0x25
    RecentStickers = 0x26
    DcOptionOld = 0x27
    TryIPv6Old = 0x28
    SongVolumeOld = 0x29
    WindowsNotificationsOld = 0x30
    IncludeMutedOld = 0x31
    MegagroupSizeMaxOld = 0x32
    DownloadPathOld = 0x33
    AutoDownloadOld = 0x34
    SavedGifsLimitOld = 0x35
    ShowingSavedGifsOld = 0x36
    AutoPlayOld = 0x37
    AdaptiveForWideOld = 0x38
    HiddenPinnedMessagesOld = 0x39
    RecentEmojiOld = 0x3A
    EmojiVariantsOld = 0x3B
    DialogsModeOld = 0x40
    ModerateModeOld = 0x41
    VideoVolumeOld = 0x42
    StickersRecentLimitOld = 0x43
    NativeNotificationsOld = 0x44
    NotificationsCountOld = 0x45
    NotificationsCornerOld = 0x46
    ThemeKeyOld = 0x47
    DialogsWidthRatioOld = 0x48
    UseExternalVideoPlayer = 0x49
    DcOptionsOld = 0x4A
    MtpAuthorization = 0x4B
    LastSeenWarningSeenOld = 0x4C
    SessionSettings = 0x4D
    LangPackKey = 0x4E
    ConnectionTypeOld = 0x4F
    StickersFavedLimitOld = 0x50
    SuggestStickersByEmojiOld = 0x51
    SuggestEmojiOld = 0x52
    TxtDomainStringOldOld = 0x53
    ThemeKey = 0x54
    TileBackground = 0x55
    CacheSettingsOld = 0x56
    AnimationsDisabled = 0x57
    ScalePercent = 0x58
    PlaybackSpeedOld = 0x59
    LanguagesKey = 0x5A
    CallSettingsOld = 0x5B
    CacheSettings = 0x5C
    TxtDomainStringOld = 0x5D
    ApplicationSettings = 0x5E
    DialogsFiltersOld = 0x5F
    FallbackProductionConfig = 0x60
    BackgroundKey = 0x61

    EncryptedWithSalt = 333
    Encrypted = 444

    Version = 666


class lskType(int):  # nocov
    lskUserMap = 0x00
    lskDraft = 0x01  # data: PeerId peer
    lskDraftPosition = 0x02  # data: PeerId peer
    lskLegacyImages = 0x03  # legacy
    lskLocations = 0x04  # no data
    lskLegacyStickerImages = 0x05  # legacy
    lskLegacyAudios = 0x06  # legacy
    lskRecentStickersOld = 0x07  # no data
    lskBackgroundOldOld = 0x08  # no data
    lskUserSettings = 0x09  # no data
    lskRecentHashtagsAndBots = 0x0A  # no data
    lskStickersOld = 0x0B  # no data
    lskSavedPeersOld = 0x0C  # no data
    lskReportSpamStatusesOld = 0x0D  # no data
    lskSavedGifsOld = 0x0E  # no data
    lskSavedGifs = 0x0F  # no data
    lskStickersKeys = 0x10  # no data
    lskTrustedBots = 0x11  # no data
    lskFavedStickers = 0x12  # no data
    lskExportSettings = 0x13  # no data
    lskBackgroundOld = 0x14  # no data
    lskSelfSerialized = 0x15  # serialized self
    lskMasksKeys = 0x16  # no data
    lskCustomEmojiKeys = 0x17  # no data
    lskSearchSuggestions = 0x18  # no data
    lskWebviewTokens = 0x19  # data: QByteArray bots, QByteArray other


class BotTrustFlag(int):  # nocov
    NoOpenGame = 1 << 0
    Payment = 1 << 1


# class QByteArray(QByteArray):
#     def dump(self):

#         print(f"  ---- hexdump ----: [0x{hex(self.size())}:{self.size()}] ({id(self)})")

#         size = self.size()
#         data = self.data()
#         out = ""
#         asc = ""

#         for i in range(size):

#             if i % 16 == 0:
#                 if i != 0:
#                     out += " |  "
#                     out += asc + "\n"
#                     asc = ""

#                 out += "  %0.4x " % i

#             out += " %0.2x" % data[i]

#             if (i > 0) and ((i % 8) == 7) and ((i % 16) != 15):
#                 out += " "

#             if (data[i] < 0x20) or (data[i] > 0x7E):
#                 asc += "."
#             else:
#                 asc += chr(data[i])

#         i = size - 1
#         if ((i % 16) != 0) and ((i % 16) == (i % 8)):
#             out += " "

#         while (i % 16) != 0:
#             out += "   "
#             i += 1

#         out += " |  "
#         print(out)


# def hexdump(byte: bytes):

#     if isinstance(byte, QByteArray):
#         byte = byte.data()

#     print(
#         f"  ---- hexdump ----: [0x{hex(byte.__len__())}:{byte.__len__()}] ({id(byte)})"
#     )

#     size = byte.__len__()
#     data = byte
#     out = ""
#     asc = ""

#     for i in range(size):

#         if i % 16 == 0:
#             if i != 0:
#                 out += " |  "
#                 out += asc + "\n"
#                 asc = ""

#             out += "  %0.4x " % i

#         out += " %0.2x" % data[i]

#         if (i > 0) and ((i % 8) == 7) and ((i % 16) != 15):
#             out += " "

#         if (data[i] < 0x20) or (data[i] > 0x7E):
#             asc += "."
#         else:
#             asc += chr(data[i])

#     i = size - 1
#     if ((i % 16) != 0) and ((i % 16) == (i % 8)):
#         out += " "

#     while (i % 16) != 0:
#         out += "   "
#         i += 1

#     out += " |  "
#     print(out)
