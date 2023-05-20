import platform, os

def clear_screen():
    system_os = platform.system()
    if system_os == "Windows":
         os.system("cls")
    else:
        os.system("clear")