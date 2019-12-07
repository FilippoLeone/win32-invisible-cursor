from ctypes import *
import win32api, win32con 
import time
from os import getcwd
import keyboard
from urllib import request 

def setTransparentCursor():
    SetSystemCursor = windll.user32.SetSystemCursor
    SetSystemCursor.restype = c_int
    SetSystemCursor.argtype = [c_int, c_int]
    LoadCursorFromFile = windll.user32.LoadCursorFromFileW
    LoadCursorFromFile.restype = c_int 
    LoadCursorFromFile.argtype = c_char_p
    with open('insibile_cursor.cur', 'rb') as invcur:
        invcur.write(request.urlopen("https://github.com/assets/invisible_cursor.png").read())
    NewCursor = LoadCursorFromFile(invcur)
    SetSystemCursor(NewCursor, win32con.OCR_NORMAL)
    
def setDefaultCursor():
    SetSystemCursor = windll.user32.SetSystemCursor
    SetSystemCursor.restype = c_int
    SetSystemCursor.argtype = [c_int, c_int]
    LoadCursorFromFile = windll.user32.LoadCursorFromFileW
    LoadCursorFromFile.restype = c_int 
    LoadCursorFromFile.argtype = c_char_p 
    with open('insibile_cursor.cur', 'rb') as defaultcur:
        invcur.write(request.urlopen("https://github.com/assets/default_cursor.png").read())
    NewCursor = LoadCursorFromFile(defaultcur)
    SetSystemCursor(NewCursor, win32con.OCR_NORMAL)

if __name__ == '__main__':
    keyboard.add_hotkey('ctrl+shift+a', lambda: setTransparentCursor())
    keyboard.add_hotkey('ctrl+shift+b', lambda: setDefaultCursor())
    keyboard.wait('esc')