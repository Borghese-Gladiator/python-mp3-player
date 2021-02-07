import cx_Freeze
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("app.py", base=base, icon="clienticon.ico")]

cx_Freeze.setup(
    name = "Basic-Music-Player-Client",
    options = {"build_exe": {"packages":["tkinter","pygame"], "include_files":["clienticon.ico"]}},
    version = "0.01",
    description = "music player application",
    executables = executables
    )