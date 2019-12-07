# Win32 Invisible Cursor

# LATEST RELEASE: [1.0](!https://github.com/FilippoLeone/win32-invisible-cursor/releases/tag/1.0)
Win32 Invisible Cursor is a script that enables the user to quickly make their idle cursor invisible and visible with key shortcuts.

  - Press `CTRL + SHIFT + a` to make your cursor invisible
  - Press `CTRL + SHIFT + b` to make your cursor visible
  - Press `ESC + f` to exit the script.

# Compiling the script with cx_Freeze
If you don't want to use the pre-packaged version in my relase, build your own from the source with the following command:
  - Run: `python setup.py build`

NOTE: The extra-lib folder contains a 32-bit version of `libffi-7.dll` (needed for `_ctypes` in `Python 3.8`). 
You can download it from the official python FTP mirror selecting the embedded version. 
