from pytest import fixture
from threading import Thread
from mm_ide import ide


@fixture(scope="function")
def start_ui():
    Thread(target=ide.main).start()
