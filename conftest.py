import pytest

from browser_manager import BrowserManager


@pytest.fixture(scope="module")
def runner():
    BrowserManager().open()
    yield
    BrowserManager().close()
