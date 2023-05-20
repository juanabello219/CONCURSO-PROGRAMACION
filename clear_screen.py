import platform, os

def system_clear_function():
    system_os = platform.system()
    if system_os == "Windows":
        os.system("cls")
    else:
        os.system("clear")