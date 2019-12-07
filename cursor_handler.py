from ctypes import *
import win32api, win32con 
import time
from os import getcwd
import keyboard
import requests

def setTransparentCursor():
    SetSystemCursor = windll.user32.SetSystemCursor
    SetSystemCursor.restype = c_int
    SetSystemCursor.argtype = [c_int, c_int]
    LoadCursorFromFile = windll.user32.LoadCursorFromFileW
    LoadCursorFromFile.restype = c_int 
    LoadCursorFromFile.argtype = c_char_p
    r = requests.get('https://github.com/FilippoLeone/win32-invisible-cursor/blob/master/invisible_cursor.cur?raw=true')
    with open('invisible_cursor.cur', 'wb') as invcur:
        invcur.write(r.content)
    NewCursor = LoadCursorFromFile('invisible_cursor.cur')
    SetSystemCursor(NewCursor, win32con.OCR_NORMAL)
    
def setDefaultCursor():
    SetSystemCursor = windll.user32.SetSystemCursor
    SetSystemCursor.restype = c_int
    SetSystemCursor.argtype = [c_int, c_int]
    LoadCursorFromFile = windll.user32.LoadCursorFromFileW
    LoadCursorFromFile.restype = c_int 
    LoadCursorFromFile.argtype = c_char_p 
    r = requests.get('https://github.com/FilippoLeone/win32-invisible-cursor/blob/master/default_cursor.cur?raw=true')
    with open('default_cursor.cur', 'wb') as defaultcur:
        defaultcur.write(r.content)
    NewCursor = LoadCursorFromFile('default_cursor.cur')
    SetSystemCursor(NewCursor, win32con.OCR_NORMAL)

if __name__ == '__main__':
    keyboard.add_hotkey('ctrl+shift+a', lambda: setTransparentCursor())
    keyboard.add_hotkey('ctrl+shift+b', lambda: setDefaultCursor())
    keyboard.wait('esc+f')