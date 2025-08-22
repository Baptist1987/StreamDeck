import subprocess
from pathlib import Path
import pyautogui
import time

def rm1():
    return "ok"

def rm2():
    return "realy_ok"

def rm3():
    subprocess.Popen(["notepad.exe"])
    return "openedNotepad"

def rm4():
    time.sleep(0.2)
    pyautogui.hotkey("alt", "f4")
    return "windowClosed"

def rm5():
    time.sleep(0.2)
    pyautogui.hotkey("alt","tab")
    return "alt+tab"

def rm6():
    time.sleep(0.2)
    pyautogui.hotkey("enter")
    return "enter"

def rm7():
    time.sleep(0.2)
    pyautogui.hotkey("tab")
    return "tab"

def rm8():
    time.sleep(0.2)
    return "rm8done"