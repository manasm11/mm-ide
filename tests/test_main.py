from mm_ide import ide
from mm_ide.ide import Tk
import pyautogui as pg


def test_ide(start_ui):
    pg.sleep(1)
    assert pg.locateOnScreen("tests/images/window_icon.png")
    assert pg.locateOnScreen("tests/images/title.png")
    width, height = pg.size()
    pg.click(width / 4, height / 4)
    pg.typewrite("print('HELLO')")
    run_menu = pg.locateCenterOnScreen("tests/images/run_main.png")
    assert run_menu
    pg.click(run_menu)
