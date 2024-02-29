import platform, subprocess

class System:
    def information(self):
        iOS = platform.system()
        if iOS == "Windows":
            subprocess.run("cls", shell=True)
        elif iOS == "Linux":
            subprocess.run("clear", shell=True)
        elif iOS == "Darwin":
            subprocess.run("clear", shell=True)
        else:
            print("UNIDENTIFIED")

main = System()
main.information()