import typing


from .account import Account, StorageAccount, MapData
from .auth import AuthKey, AuthKeyType
from .mtp import MTP
from .storage import Storage, Serialize
from .tdesktop import TDesktop
from . import configs

from .. import exception as excpt

from ..api import APIData, API

from typing import Optional

import struct
import os
