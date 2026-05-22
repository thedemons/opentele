from __future__ import annotations
from typing import List, Dict, Tuple, TypeVar, Type
from .utils import *
import hashlib, os, json

_T = TypeVar("_T")


class DeviceInfo(object):
    def __init__(self, model, version) -> None:
        self.model = model
        self.version = version

    def __str__(self) -> str:
        return f"{self.model} {self.version}"

    def to_dict(self) -> Dict[str, str]:
        return {"device_model": self.model, "system_version": self.version}

    @classmethod
    def from_dict(cls, data: Dict[str, str]):
        if not isinstance(data, dict):
            return None
        model = data.get("device_model") or data.get("model")
        version = data.get("system_version") or data.get("version")
        if not model or not version:
            return None
        return cls(model, version)


class SystemInfo(BaseObject):

    deviceList: List[DeviceInfo] = []
    device_modesl: List[str] = []
    system_versions: List[str] = []

    def __init__(self) -> None:
        pass

    @classmethod
    def RandomDevice(cls: Type[SystemInfo], unique_id: str = None) -> DeviceInfo:
        hash_id = cls._strtohashid(unique_id)
        return cls._RandomDevice(hash_id)

    @classmethod
    def _RandomDevice(cls, hash_id: int):
        cls.__gen__()
        return cls._hashtovalue(hash_id, cls.deviceList)

    @classmethod
    def __gen__(cls):
        raise NotImplementedError(
            f"{cls.__name__} device not supported for randomize yet"
        )

    @classmethod
    def _strtohashid(cls, unique_id: str = None):

        if unique_id != None and not isinstance(unique_id, str):
            unique_id = str(unique_id)

        byteid = os.urandom(32) if unique_id == None else unique_id.encode("utf-8")

        return int(hashlib.sha1(byteid).hexdigest(), 16) % (10 ** 12)

    @classmethod
    def _hashtorange(cls, hash_id: int, max, min=0):
        return hash_id % (max - min) + min

    @classmethod
    def _hashtovalue(cls, hash_id: int, values: List[_T]) -> _T:
        return values[hash_id % len(values)]

    @classmethod
    def _CleanAndSimplify(cls, text: str) -> str:
        return " ".join(word for word in text.split(" ") if word)


class GeneralDesktopDevice(SystemInfo):

    # Total: 794 devices, update Jan 10th 2022
    # Real device models that I crawled myself from the internet
    #
    # This is the values in HKEY_LOCAL_MACHINE\HARDWARE\DESCRIPTION\System\BIOS
    # including SystemFamily, SystemProductName, BaseBoardProduct
    #
    # Filtered any models that exceed 15 characters
    # just like tdesktop does in lib_base https://github.com/desktop-app/lib_base/blob/master/base/platform/win/base_info_win.cpp#L173
    #
    # Feel free to use
    #
    # Sources: https://answers.microsoft.com/, https://www.techsupportforum.com/ and https://www.bleepingcomputer.com/

    device_models = [
        "VPCEB27FD",
        "VPCEE31FX",
        "VPCF11QFX",
        "VPCF1290X",
        "VPCF22C5E",
        "VPCF22J1E",
        "VPCS111FM",
        "Veriton E430",
        "VivoBook",
        "Vostro",
        "Vostro 1520",
        "Vostro 1720",
        "Vostro1510",
        "W35xSS_370SS",
        "W55xEU",
        "X421JQ",
        "X510UNR",
        "X550CA",
        "X550JX",
        "X555LAB",
        "X556UB",
        "X556UF",
        "X570 GAMING X",
        "X570 MB",
        "X58-USB3",
        "X58A-UD3R",
        "X58A-UD5",
        "X58A-UD7",
        "XPS",
        "XPS 13 9305",
        "XPS 13 9370",
        "XPS 15 9550",
        "XPS 15 9560",
        "XPS 630i",
        "XPS 730",
        "XPS 730X",
        "XPS 8300",
        "XPS 8700",
        "XPS 8940",
        "XPS A2420",
        "XPS L501X",
        "XPS L701X",
        "XPS M1530",
        "YOGA 530-14ARR",
        "YOGA 920-13IKB",
        "YOGATablet2",
        "Yoga2",
        "Z10PE-D8 WS",
        "Z170 PRO GAMING",
        "Z170-E",
        "Z170X-Gaming 5",
        "Z170X-UD3",
        "Z170X-UD3-CF",
        "Z370P D3",
        "Z370P D3-CF",
        "Z68 Pro3",
        "Z68A-D3-B3",
        "Z68A-D3H-B3",
        "Z68AP-D3",
        "Z68MA-D2H-B3",
        "Z68X-UD3H-B3",
        "Z68XP-UD3",
        "Z68XP-UD4",
        "Z77 Pro4",
        "Z77X-D3H",
        "Z87 Extreme6",
        "Z87-D3HP",
        "Z87-D3HP-CF",
        "Z87M Extreme4",
        "Z87N-WIFI",
        "Z87X-OC",
        "Z87X-OC-CF",
        "Z87X-UD4H",
        "Z97-A",
        "Z97-A-USB31",
        "Z97-AR",
        "Z97-C",
        "Z97-PRO GAMER",
        "Z97X-Gaming 7",
        "eMachines E725",
        "h8-1070t",
        "h8-1534",
        "imedia S3720",
        "ixtreme M5800",
        "p6654y",
        "p6710f",
    ]


class WindowsDevice(GeneralDesktopDevice):
    system_versions = ["Windows 10", "Windows 8", "Windows 8.1", "Windows 7"]

    deviceList: List[DeviceInfo] = []

    @classmethod
    def __gen__(cls: Type[WindowsDevice]) -> None:

        if len(cls.deviceList) == 0:

            results: List[DeviceInfo] = []

            for model in cls.device_models:
                model = cls._CleanAndSimplify(model.replace("_", ""))
                for version in cls.system_versions:
                    results.append(DeviceInfo(model, version))

            cls.deviceList = results


class LinuxDevice(GeneralDesktopDevice):

    system_versions: List[str] = []
    deviceList: List[DeviceInfo] = []

    @classmethod
    def __gen__(cls: Type[LinuxDevice]) -> None:

        if len(cls.system_versions) == 0:
            # https://github.com/desktop-app/lib_base/blob/master/base/platform/linux/base_info_linux.cpp#L129

            # ? Purposely reduce the amount of devices parameter to generate deviceList more quickly
            enviroments = [
                "GNOME",
                "MATE",
                "XFCE",
                "Cinnamon",
                "Unity",
                "ubuntu",
                "LXDE",
            ]

            wayland = ["Wayland", "XWayland", "X11"]

            libcNames = ["glibc"]
            libcVers = ["2.31", "2.32", "2.33", "2.34"]

            # enviroments = [
            #     "GNOME", "MATE", "XFCE", "Cinnamon", "X-Cinnamon",
            #     "Unity", "ubuntu", "GNOME-Classic", "LXDE"
            # ]

            # wayland = ["Wayland", "XWayland", "X11"]

            # libcNames = ["glibc", "libc"]
            # libcVers = [
            #     "2.20", "2.21", "2.22", "2.23", "2.24", "2.25", "2.26", "2.27",
            #     "2.28", "2.29", "2.30", "2.31", "2.32", "2.33", "2.34"
            # ]

            def getitem(group: List[List[str]], prefix: str = "") -> List[str]:

                prefix = "" if prefix == "" else prefix + " "
                results = []
                if len(group) == 1:
                    for item in group[0]:
                        results.append(prefix + item)
                    return results

                for item in group[0]:
                    results.extend(getitem(group[1:], prefix + item))

                return results

            libcFullNames = getitem([libcNames, libcVers], "")

            cls.system_versions = getitem(
                [enviroments, wayland, libcFullNames], "Linux"
            )

            results: List[DeviceInfo] = []

            for version in cls.system_versions:
                for model in cls.device_models:
                    results.append(DeviceInfo(model, version))

            cls.deviceList = results


class macOSDevice(GeneralDesktopDevice):

    deviceList: List[DeviceInfo] = []

    # Total: 54 device models, update Jan 10th 2022
    # Only list device models since 2013
    #
    # Sources:
    # Thanks to: https://mrmacintosh.com/list-of-mac-boardid-deviceid-model-identifiers-machine-models/
    #       and: https://github.com/brunerd/jamfTools/blob/main/EAs/macOSCompatibility.sh
    #
    # Remark: https://www.innerfence.com/howto/apple-ios-devices-dates-versions-instruction-sets

    device_models = [
        "MacBookPro16,4",
        "MacBookPro16,3",
        "MacBookPro16,2",
        "MacBookPro16,1",
        "MacBookPro15,4",
        "MacBookPro15,3",
        "MacBookPro15,2",
        "MacBookPro15,1",
        "MacBookPro14,3",
        "MacBookPro14,2",
        "MacBookPro14,1",
        "MacBookPro13,3",
        "MacBookPro13,2",
        "MacBookPro13,1",
        "MacBookPro12,1",
        "MacBookPro11,5",
        "MacBookPro11,4",
        "MacBookPro11,3",
        "MacBookPro11,2",
        "MacBookPro11,1",
        "MacBookPro10,2",
        "MacBookPro10,1",
        "MacBookAir9,1",
        "MacBookAir8,2",
        "MacBookAir8,1",
        "MacBookAir7,2",
        "MacBookAir7,2",
        "MacBookAir7,1",
        "MacBookAir6,2",
        "MacBookAir6,1",
        "MacBookAir6,2",
        "MacBook10,1",
        "MacBook9,1",
        "MacBook8,2",
        "MacBook8,1",
        "MacPro7,1",
        "MacPro6,1",
        "iMac20,2",
        "iMac20,1",
        "iMac19,1",
        "iMac18,3",
        "iMac18,2",
        "iMac18,1",
        "iMac17,1",
        "iMac17,1",
        "iMac17,1",
        "iMac16,2",
        "iMac16,1",
        "iMac15,2",
        "iMac15,1",
        "iMac14,4",
        "iMac14,3",
        "iMac14,2",
        "iMac14,1",
        "iMacPro1,1",
    ]

    # Source: https://support.apple.com/en-us/HT201222
    system_versions = [
        "macOS 10.12",
        "macOS 10.12.1",
        "macOS 10.12.2",
        "macOS 10.12.3",
        "macOS 10.12.4",
        "macOS 10.12.5",
        "macOS 10.12.6",
        "macOS 10.13",
        "macOS 10.13.1",
        "macOS 10.13.2",
        "macOS 10.13.3",
        "macOS 10.13.4",
        "macOS 10.13.5",
        "macOS 10.13.6",
        "macOS 10.14",
        "macOS 10.14.1",
        "macOS 10.14.2",
        "macOS 10.14.3",
        "macOS 10.14.4",
        "macOS 10.14.5",
        "macOS 10.14.6",
        "macOS 10.15",
        "macOS 10.15.1",
        "macOS 10.15.2",
        "macOS 10.15.3",
        "macOS 10.15.4",
        "macOS 10.15.5",
        "macOS 10.15.6",
        "macOS 10.15.7",
        "macOS 11.0",
        "macOS 11.0.1",
        "macOS 11.1",
        "macOS 11.2",
        "macOS 11.2.1",
        "macOS 11.2.2",
        "macOS 11.2.3",
        "macOS 11.3",
        "macOS 11.3.1",
        "macOS 11.4",
        "macOS 11.5",
        "macOS 11.5.1",
        "macOS 11.5.2",
        "macOS 11.6",
        "macOS 11.6.1",
        "macOS 11.6.2",
        "macOS 12.0",
        "macOS 12.0.1",
        "macOS 12.1",
    ]

    deviceList: List[DeviceInfo] = []

    @classmethod
    def __gen__(cls: Type[macOSDevice]) -> None:

        if len(cls.deviceList) == 0:

            # https://github.com/desktop-app/lib_base/blob/master/base/platform/mac/base_info_mac.mm#L42

            def FromIdentifier(model: str):
                words = []
                word = ""

                for ch in model:
                    if not ch.isalpha():
                        continue
                    if ch.isupper():
                        if word != "":
                            words.append(word)
                            word = ""
                    word += ch

                if word != "":
                    words.append(word)
                result = ""
                for word in words:
                    if result != "" and word != "Mac" and word != "Book":
                        result += " "
                    result += word

                return result

            new_devices_models = []
            for model in cls.device_models:
                model = cls._CleanAndSimplify(FromIdentifier(model))
                if not model in new_devices_models:
                    new_devices_models.append(model)

            cls.device_models = new_devices_models

            results: List[DeviceInfo] = []

            for model in cls.device_models:
                for version in cls.system_versions:
                    results.append(DeviceInfo(model, version))

            cls.deviceList = results


class AndroidDevice(SystemInfo):

    system_versions = ["SDK 33", "SDK 34", "SDK 35"]

    device_models_by_sdk = {
        "SDK 33": [
            "Samsung SM-A536B",  # Galaxy A53 5G
            "Samsung SM-A736B",  # Galaxy A73 5G
            "Samsung SM-G991B",  # Galaxy S21
            "Samsung SM-G998B",  # Galaxy S21 Ultra
            "Samsung SM-G990B",  # Galaxy S21 FE
            "Samsung SM-A336B",  # Galaxy A33 5G
            "Samsung SM-A137F",  # Galaxy A13
            "Samsung SM-M336B",  # Galaxy M33 5G
            "Xiaomi 2107113SG",  # Xiaomi 11T
            "Xiaomi 21081111RG", # Xiaomi 11T Pro
            "Xiaomi 2112123AG",  # Xiaomi 12
            "Redmi 2201116SG",   # Redmi Note 11 Pro+
            "Redmi 2201117TG",   # Redmi Note 11S
            "Redmi 2201116PG",   # Redmi Note 11 Pro 5G
            "POCO M2102J20SG",   # POCO X3 Pro
            "POCO 21091116AG",   # POCO M4 Pro 5G
            "POCO 2201116PG",    # POCO X4 Pro 5G
            "OPPO CPH2449",      # OPPO Find X5 Pro
            "OPPO CPH2525",      # OPPO Reno10
            "OPPO CPH2371",      # OPPO Reno7 5G
        ],
        "SDK 34": [
            "Samsung SM-A045F",  # Galaxy A04
            "Samsung SM-A135F",  # Galaxy A13
            "Samsung SM-A235F",  # Galaxy A23
            "Samsung SM-A245F",  # Galaxy A24
            "Samsung SM-A336B",  # Galaxy A33 5G
            "Samsung SM-A346B",  # Galaxy A34 5G
            "Samsung SM-A525F",  # Galaxy A52
            "Samsung SM-A526B",  # Galaxy A52 5G
            "Samsung SM-A528B",  # Galaxy A52s 5G
            "Samsung SM-A536B",  # Galaxy A53 5G
            "Samsung SM-A546B",  # Galaxy A54 5G
            "Samsung SM-A725F",  # Galaxy A72
            "Xiaomi 2211133G",   # Xiaomi 13
            "Xiaomi 2304FPN6DC", # Xiaomi 13 Ultra
            "Xiaomi 2210132G",   # Xiaomi 12T Pro
            "Xiaomi 23127PN0CG", # Xiaomi 14
            "Redmi 23090RA98G",  # Redmi Note 13 Pro 5G
            "Redmi 2312DRA50G",  # Redmi Note 13 Pro (4G)
            "Redmi 23117RA68G",  # Redmi Note 13 5G
            "Redmi 23124RA7EO",  # Redmi Note 13 (4G)
            "POCO 22021211RG",   # POCO F4
            "POCO 22101320G",    # POCO X5 Pro 5G
            "POCO 23049PCD8G",   # POCO F5
            "POCO 23013PC75G",   # POCO F5 Pro
            "OPPO CPH2607",      # OPPO Reno11 Pro
            "OPPO CPH2599",      # OPPO Find N3 Flip
            "OPPO CPH2581",      # OPPO Reno11
            "Motorola moto g13",
            "Motorola moto g23",
            "Motorola moto g53 5G",
            "Motorola moto g73 5G",
        ],
        "SDK 35": [
            "Xiaomi 24030PN60G", # Xiaomi 14 (Update)
            "Xiaomi 23113RKC6G", # Xiaomi 14 Pro
            "Xiaomi 2407FPN8EG", # Xiaomi 14T Pro
            "Redmi 24094RAD4G",  # Redmi Note 14 Pro
            "Redmi 24053PY09I",  # Redmi Note 13 Pro+ (HyperOS 2)
            "POCO 2311DRK48G",   # POCO X6 Pro
            "POCO 2407FPN8EG",   # POCO F6 Pro
            "POCO 24069PC21G",   # POCO F6
            "OPPO CPH2621",      # OPPO Reno12 Pro
            "OPPO CPH2631",      # OPPO Reno12
            "OPPO CPH2651",      # OPPO Find X7 Ultra
            "Motorola moto g34 5G", # Moto Edge 50 Fusion
            "Motorola moto g85 5G", # Moto G85 5G
            "Motorola moto g55 5G", # Moto G55 5G
            "Motorola moto g45 5G", # Moto G45 5G
            "Motorola moto g86 5G",
            "Samsung SM-S928B",  # Galaxy S24 Ultra
            "Samsung SM-S926B",  # Galaxy S24+
            "Samsung SM-S921B",  # Galaxy S24
            "Samsung SM-S918B",  # Galaxy S23 Ultra
            "Samsung SM-S916B",  # Galaxy S23+
            "Samsung SM-S911B",  # Galaxy S23
            "Samsung SM-S711B",  # Galaxy S23 FE
            "Samsung SM-S908B",  # Galaxy S22 Ultra
            "Samsung SM-S906B",  # Galaxy S22+
            "Samsung SM-S901B",  # Galaxy S22
            "Samsung SM-G998B",  # Galaxy S21 Ultra
            "Samsung SM-G996B",  # Galaxy S21+
            "Samsung SM-G991B",  # Galaxy S21
            "Samsung SM-G990B",  # Galaxy S21 FE
            "Samsung SM-A736B",  # Galaxy A73 5G
            "Samsung SM-A725F",  # Galaxy A72
            "Samsung SM-A556B",  # Galaxy A55 5G
            "Samsung SM-A546B",  # Galaxy A54 5G
            "Samsung SM-A536B",  # Galaxy A53 5G
            "Samsung SM-A356B",  # Galaxy A35 5G
            "Samsung SM-A346B",  # Galaxy A34 5G
            "Samsung SM-A336B",  # Galaxy A33 5G
            "Samsung SM-A256B",  # Galaxy A25 5G
            "Samsung SM-A245F",  # Galaxy A24
            "Samsung SM-A156B",  # Galaxy A15 5G
        ],
    }

    device_models = []
    deviceList: List[DeviceInfo] = []
    deviceList_by_sdk: Dict[str, List[DeviceInfo]] = {}

    @classmethod
    def _RandomDevice(cls, hash_id: int):
        cls.__gen__()

        sdk_order = [sdk for sdk in cls.system_versions if cls.deviceList_by_sdk.get(sdk)]
        sdk_version = cls._hashtovalue(hash_id, sdk_order)
        sdk_devices = cls.deviceList_by_sdk[sdk_version]

        # mismo unique_id -> mismo SDK -> mismo dispositivo dentro de ese SDK
        device_index = (hash_id // max(1, len(sdk_order))) % len(sdk_devices)
        return sdk_devices[device_index]

    @classmethod
    def __gen__(cls: Type["AndroidDevice"]) -> None:

        if len(cls.deviceList) == 0:
            cls.device_models = []
            cls.deviceList = []
            cls.deviceList_by_sdk = {}

            for version in cls.system_versions:
                modelos = cls.device_models_by_sdk.get(version, [])
                sdk_list: List[DeviceInfo] = []

                for model in modelos:
                    cls.device_models.append(model)
                    info = DeviceInfo(model, version)
                    sdk_list.append(info)
                    cls.deviceList.append(info)

                cls.deviceList_by_sdk[version] = sdk_list


    @classmethod
    def GetDevices(cls) -> List[DeviceInfo]:
        cls.__gen__()
        return cls.deviceList.copy()

    @classmethod
    def GetDevicesBySdk(cls) -> Dict[str, List[DeviceInfo]]:
        cls.__gen__()
        return {sdk: devices.copy() for sdk, devices in cls.deviceList_by_sdk.items()}

    @classmethod
    def FindDevice(cls, device_model: str, system_version: str = None):
        cls.__gen__()
        if not device_model:
            return None

        for item in cls.deviceList:
            if item.model == device_model and (system_version is None or item.version == system_version):
                return item

        return None

    @classmethod
    def _device_config_path(cls, unique_id: str = None):
        if unique_id is None:
            return None
        if not isinstance(unique_id, str):
            unique_id = str(unique_id)
        return f"{unique_id}.device.json"

    @classmethod
    def LoadDeviceConfig(cls, unique_id: str = None):
        path = cls._device_config_path(unique_id)
        if not path or not os.path.exists(path):
            return None

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            return None

        info = DeviceInfo.from_dict(data)
        if info is None:
            return None

        return cls.FindDevice(info.model, info.version)

    @classmethod
    def SaveDeviceConfig(cls, unique_id: str, device_info: DeviceInfo):
        path = cls._device_config_path(unique_id)
        if not path or device_info is None:
            return None

        folder = os.path.dirname(path)
        if folder:
            os.makedirs(folder, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(device_info.to_dict(), f, ensure_ascii=False, indent=4)

        return path

    @classmethod
    def ResolveDevice(cls, unique_id: str = None, device_info: DeviceInfo = None):
        if device_info is not None:
            if not isinstance(device_info, DeviceInfo):
                if isinstance(device_info, dict):
                    device_info = DeviceInfo.from_dict(device_info)
                elif isinstance(device_info, (tuple, list)) and len(device_info) >= 2:
                    device_info = DeviceInfo(device_info[0], device_info[1])
                else:
                    device_info = None

            if device_info is not None:
                found = cls.FindDevice(device_info.model, device_info.version)
                if found is not None:
                    if unique_id is not None:
                        cls.SaveDeviceConfig(unique_id, found)
                    return found

        stored = cls.LoadDeviceConfig(unique_id)
        if stored is not None:
            return stored

        return cls.RandomDevice(unique_id)


class iOSDeivce(SystemInfo):

    device_models = {
        5: ["S"],
        6: [" Plus", "", "S", "S Plus"],
        7: ["", " Plus"],
        8: ["", " Plus"],
        10: ["", "S", "S Max", "R"],
        11: ["", " Pro", " Pro Max"],
        12: [" mini", "", " Pro", " Pro Max"],
        13: [" Pro", " Pro Max", " Mini", ""],
    }

    system_versions: Dict[int, Dict[int, List[int]]] = {
        15: {2: [], 1: [1], 0: [2, 1]},
        14: {8: [1], 7: [1], 6: [], 5: [1], 4: [2, 1], 3: [], 2: [1], 1: [], 0: [1]},
        13: {7: [], 6: [1], 5: [1], 4: [1], 3: [1], 2: [3, 2], 1: [3, 2, 1]},
        12: {
            5: [5, 4, 3, 2, 1],
            4: [9, 8, 7, 6, 5, 4, 3, 2, 1],
            3: [2, 1],
            11: [0],
            2: [],
            1: [4, 3, 2, 1],
            0: [1],
        },
    }

    deviceList: List[DeviceInfo] = []

    @classmethod
    def __gen__(cls: Type[iOSDeivce]) -> None:

        if len(cls.deviceList) == 0:
            results: List[DeviceInfo] = []

            # ! SHITTY CODE BECAUSE I HAD TO CHECK FOR THE RIGHT VERSION
            for id_model in cls.device_models:
                if id_model == 13:
                    available_versions = [15]
                elif id_model == 12:
                    available_versions = [14, 15]
                elif id_model == 11:
                    available_versions = [13, 14, 15]
                elif id_model == 5:
                    available_versions = [12]
                else:
                    available_versions = [12, 13, 14, 15]

                for model_name in cls.device_models[id_model]:

                    if id_model == 10:
                        id_model = "X"
                    device_model = f"iPhone {id_model}{model_name}"

                    for major in available_versions:
                        for minor, patches in cls.system_versions[major].items():

                            if len(patches) == 0:
                                results.append(
                                    DeviceInfo(device_model, f"{major}.{minor}")
                                )
                            else:
                                for patch in patches:
                                    results.append(
                                        DeviceInfo(
                                            device_model, f"{major}.{minor}.{patch}"
                                        )
                                    )

            cls.deviceList = results
