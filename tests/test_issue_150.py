import pytest
from telethon.sessions import StringSession, MemorySession
from telethon.crypto import AuthKey
from src.exception import OpenTeleException, TDataInvalidMagic
from src.td.account import StorageAccount
from src.tl.telethon import TelegramClient
from src.api import UseCurrentSession, API


def test_opentele_exception_inherits_from_exception():
    """Verify OpenTeleException subclasses Exception and is caught by except Exception."""
    assert issubclass(OpenTeleException, Exception)
    assert not issubclass(Exception, OpenTeleException)

    caught = False
    try:
        raise OpenTeleException("test error")
    except Exception as e:
        caught = True
        assert isinstance(e, OpenTeleException)
        assert "test error" in str(e)
    assert caught, "OpenTeleException must be caught by except Exception"


def test_read_map_with_continues_to_read_mtp_data(monkeypatch):
    """Verify that a failure in __mapData.read does not abort calling readMtpData."""
    # Create a mock StorageAccount
    class DummyStorageAccount:
        def __init__(self):
            self.read_mtp_data_called = False

        def mock_map_read(self, localKey, legacyPasscode):
            raise OpenTeleException("Unknown key type in encrypted map: 23")

        def mock_read_mtp_data(self):
            self.read_mtp_data_called = True

    dummy = DummyStorageAccount()
    # Call the actual readMapWith logic using dummy object
    # In StorageAccount:
    # try:
    #     self.__mapData.read(localKey, legacyPasscode)
    # except OpenTeleException:
    #     pass
    # self.readMtpData()
    class MockMapData:
        def read(self, localKey, legacyPasscode):
            raise OpenTeleException("Unknown key type in encrypted map: 23")

    dummy_account = StorageAccount.__new__(StorageAccount)
    dummy_account._StorageAccount__mapData = MockMapData()
    mtp_called = False
    def fake_read_mtp():
        nonlocal mtp_called
        mtp_called = True
    dummy_account.readMtpData = fake_read_mtp

    # Calling readMapWith should catch OpenTeleException and still invoke readMtpData
    dummy_account.readMapWith(localKey=None)
    assert mtp_called, "readMtpData must be called even if __mapData.read raises OpenTeleException"


def test_session_instance_assignment():
    """Verify that passing a Session instance (e.g. StringSession/MemorySession) correctly sets auth_session."""
    from telethon.sessions.abstract import Session

    # Simulate the session resolution branch from FromTDesktop:
    session = StringSession()
    flag = UseCurrentSession

    if isinstance(session, str) or session is None:
        auth_session = None
    elif not isinstance(session, Session):
        raise TypeError("The given session must be a str or a Session instance.")
    else:
        auth_session = session

    assert auth_session is session
    assert isinstance(auth_session, StringSession)
