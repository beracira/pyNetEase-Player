import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
        name = "pyNetEase Music",
        version = "0.0.4",
        description = "A third party player for NetEase Music",
        executables = [Executable("run_gui.py", base = base)])