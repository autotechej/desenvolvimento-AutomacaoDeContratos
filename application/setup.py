import sys

from cx_Freeze import Executable, setup

build_exe_options = {"packages": ["os"], "includes": ["tkinter", "PyQt5"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Matheus",
    version = "0.1",
    description = "My GUI application",
    options = {"build_exe": build_exe_options},
    executables = {Executable("AutoTech_AutoContract.py", base=base)}
)