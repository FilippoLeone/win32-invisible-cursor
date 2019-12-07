import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "win32api", "win32con", "time", "keyboard", "requests"], "include_files" : ['extra-lib/libffi-7.dll']}
datafile = []
setup(  name = "InvisibleCursor",
        version = "0.1",
        description = "Invisible cursor maker",
        options = {"build_exe": build_exe_options},
        executables = [Executable("cursor_handler.py", base=None)])