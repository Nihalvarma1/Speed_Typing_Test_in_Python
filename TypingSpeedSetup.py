from cx_Freeze import *

includefiles = ['typingspeed.ico']
base =None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut", # shortcut
     "DesktopFolder", #Directory_
     "Typing Speed", #Name
     "TARGETDIR", #component_
     "[TARGETDIR]\TypingSpeed.exe", #target
     None, #argument
     None, #description
     None, #Hotkey
     None, #Icon
     None, #Iconindex
     None, #ShowCad
     "TARGETDIR", #WkDir
     )
]
msi_data = {"Shortcut": shortcut_table}

#Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}
setup(
    version="1.0",
    description="Typing Speed Tester Application",
    author="NihalVarma",
    name="Typing Tester",
    options={'build_exe':{'include_files': includefiles}, "bdist_msi": bdist_msi_options,},
    executables=[
        Executable(
            script="TypingSpeed.py",
            base=base,
            icon='logotype.ico',
        )
    ]
)
