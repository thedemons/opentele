# Changelog
All notable changes to this project will be documented in this file.

## [v1.15.2] - 2026-04-03 (Fork)

- **Python 3.13 compatibility:**
  - Fixed `crossDelete` in `utils.py` to handle new dunder attributes (`__firstlineno__`, `__static_attributes__`, `__dict__`, `__weakref__`, `__qualname__`)
  - Fixed `_on_login` coroutine handling in `tl/telethon.py`
  - Removed deprecated TDesktop storage keys (`customEmoji`, `searchSuggestions`, `webviewTokens`)
  - Fixed `event_loop` deprecation in `tdata_test.py`
- **QR Code login:** Added session creation via QR code scan from the official Telegram app, no tdata or session conversion needed. Supports 2FA.
- **Redesigned device spoofing:** Replaced hardcoded device list with structured SDK-to-device mapping. Each Android version (Android 13/SDK 33, Android 14/SDK 34, Android 15/SDK 35) is mapped to real devices that were officially released or updated to that version. Updated app version to `12.5.1` to match current official Telegram Android.
- **New methods:** `DeviceInfo.to_dict()`, `DeviceInfo.from_dict()`, `ResolveDevice()`, `FindDevice()`, `GetDevices()`, `GetDevicesBySdk()`, `LoadDeviceConfig()`, `SaveDeviceConfig()`
- **Other:** Changed `isinstance` to `type()` in `APIData.__eq__`, added `qrcode` dependency.

## [v1.15](https://pypi.org/project/opentele/1.15/) - 2022-01-27

- Massive performance upgrade, UseCurrentSession is now 200x faster than before.
- `TDesktop` now has `PerformanceMode` which is enabled by default. It will now load and save tdata 200x faster.
- Huge performance boost when converting `TelegramClient` to `TDesktop`.
- Replace `inspect.stack()` with `inspect.currentframe()` in `OpenTeleException`. Using `inspect.stack()` is a stupid move, it's really slow.

## [v1.14](https://pypi.org/project/opentele/1.14/) - 2022-01-26

- `TelegramClient` will now use `TelegramDesktop` api by default.
- Fix a bug when saving tdata.

## [v1.13](https://pypi.org/project/opentele/1.13/) - 2022-01-21

- Fix `unique_id` not generated correctly in `API.Generate()`
- Added DC mismatched handling when authorizing a new client.

## [First Stable Release](https://pypi.org/project/opentele/1.13/) - 2022-01-20

- First stable release of opentele.
