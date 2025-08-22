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
    safe_hotkey("alt", "f4")
    return "windowClosed"

def rm5():
    safe_hotkey("alt", "tab")
    return "alt+tab"

def rm6():
    safe_hotkey("enter")
    return "enter"

def rm7():
    safe_hotkey("tab")
    return "tab"

def rm8():
    time.sleep(0.2)
    return "rm8done"

    def safe_hotkey(*keys, delay=0.2):
    """Helper function to execute hotkey with sleep delay to avoid conflicts"""
    time.sleep(delay)
    pyautogui.hotkey(*keys)