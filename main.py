import os, sys, termcolor, time, getpass, colorama, math, datetime, shutil, datetime, subprocess
from infoos import System as infoos


def __init__():
    infoos.information(infoos)
    termcolor.cprint("                    POLPIOTECH®                    ", "black", "on_white")
    termcolor.cprint("                -- THE MAIN MENU --                ", "white", "on_red")
    termcolor.cprint("░░░░░░░░░░░░░░░░░░░░░░░░░█                         ", "black", "on_white")
    termcolor.cprint("░░░░░░░░░░░░░░░░░░░░░░░▄▄█▄▄                       ", "black", "on_white")
    termcolor.cprint("░░░░░░░░░░░░░░░░░░░▀▀▀██▀▀▀██▀▀▀                   ", "black", "on_white")
    termcolor.cprint("░░░░░░░░░░░░░░░▄▄▄▄▄▄▄███████▄▄▄▄▄▄▄               ", "black", "on_white")
    termcolor.cprint("░░░░░░░░░░░░░░░░░█▄█░░▀██▄██▀░░█▄█                 ", "black", "on_white")
    termcolor.cprint("                  LET'S GO, BRO!                   ", "white", "on_red")
    print()
    print()
    termcolor.cprint(" [ P ] - PRESS KEY TO THE TURNOFF OPERATION SYSTEM. ", "black", "on_white")
    termcolor.cprint(" [ R ] - PRESS KEY TO THE REBOOT OPERATION SYSTEM.  ", "black", "on_white")
    print()
    print(" [1] - THE OPERATIONS ON FILES AND DIRECTORIES.")
    print(" [2] - THE UPDATE OPERATION SYSTEM.")
    print(" [3] - THE CLEAN OPERATION SYSTEM.")
    print(" [4] - THE BACKUP FILES FROM DESKTOP.") 
    print(" [5] - THE ANTIVIRUS PROGRAM.")
    print(" [6] - THE ROOTKIT PROGRAMS.")
    print(" [7] - THE ENCRYPYING FILES.")
    print(" [8] - THE ENCRIPTING TEXT.")
    print(" [0] - EXIT")
    print()
    opt = str(input("YOUR CHOOSE: "))
    if opt == str(1):
        change_path()
        alert_write()
    elif opt == str(2):
        system_update()
    elif opt == str(3):
        system_clean()
    elif opt == str(4):
        backup_desktop()
    elif opt == str(5):
        antivirus()
    elif opt == str(6):
        rootkit()
    elif opt == str(7):
        encryption_file()
    elif opt == str(8):
        encryption_text()        
    elif opt == str(0):
        system_exit()
    elif opt == "p" or opt == "P":
        return turnoff_system()
    elif opt == "r" or opt == "R":
        return restart_system()
    else:
        __init__()

def encryption_file():
    infoos.information(infoos)
    termcolor.cprint(" Funcion is creates... ", "white", "on_blue")
    time.sleep(6)
    return __init__()

def encryption_text():
    infoos.information(infoos)
    termcolor.cprint(" Funcion is creates... ", "white", "on_blue")
    time.sleep(6)
    return __init__()

def turnoff_system():
    infoos.information(infoos)
    termcolor.cprint(" DO YOU WANT TURN OFF OPERATION SYSTEM? (y/n) ", "white", "on_red")
    print()
    optionTOS = str(input("YOUR CHOOSE: "))
    if optionTOS == "y" or optionTOS == "Y":
        shutdown = subprocess.run("shutdown now", shell=True)
        return shutdown        
    elif optionTOS == "n" or optionTOS == "N":
        return __init__()
    else:
        return turnoff_system()
        
def restart_system():
    infoos.information(infoos)
    termcolor.cprint(" DO YOU WANT REBOOT OPERATION SYSTEM? (y/n) ", "white", "on_red")
    print()
    optionROS = str(input("YOUR CHOOSE: "))
    if optionROS == "y" or optionROS == "Y":
       reboot = subprocess.run("reboot", shell=True)
       return reboot
    elif optionROS == "n" or optionROS == "N":
        return __init__()
    else:
        return restart_system()

def change_path():
    while True:
        try:
            infoos.information(infoos)
            termcolor.cprint(" DO YOU WANT GO TO THE OPERATIONS ON FILES AND DIRECTORYES? (y/n) ", "white", "on_red")
            print()
            optionCHP = input("YOUR CHOOSE: ")
            if optionCHP == "y" or optionCHP == "Y":
                infoos.information(infoos)
                termcolor.cprint(" -- CHANGE A DIRECTORY -- ", "white", "on_red")
                print()
                termcolor.cprint(" [Q] - BACK TO MAIN MENU. ", "black", "on_white")
                print()
                path = str(input("ENTER PATH: "))
                print()
                if path == "q" or path == "Q":
                    infoos.information(infoos)
                    __init__()
                else:
                    os.chdir(path)
                    pathisdir = os.path.isdir(".")
                    termcolor.colored(print("DIRECTORY EXIST: ", pathisdir), "black", "on_white")
                    print()
                    termcolor.cprint(" -- CONTENTS DIRECTORY -- ", "white", "on_red")
                    for item in os.listdir("."):
                        if os.path.isdir(item):
                            termcolor.cprint("{} - [ D ]".format(item), "white", "on_light_green")
                        else:
                            termcolor.cprint("{} - [ F ]".format(item), "white", "on_green")
                    print()
                    print()
                    input(termcolor.colored(" PLEASE PRESS ANY KEY TO CONTINUE... ", "black", "on_white"))
                    return alert_write()
            elif optionCHP == "n" or optionCHP == "N":
                __init__()
            else:
                change_path()
        except Exception as otherExcepts:
            dt = str(datetime.datetime.now())[0:19]
            event = "[ SYSTEM: FILE OPERATIONS ]"
            print()
            print()
            termcolor.cprint(f" AN ERROR HAS OCCURED: {otherExcepts} ", "white", "on_red")
            time.sleep(3)
            infoos.information(infoos)
            with open("./logs/error/logs_error.txt", "a") as file:
                if file.writable():
                    error = otherExcepts
                    termcolor.cprint(" MORE INFORMATION ABOUT THE ERROR CAN BE FOUND IN THE 'LOGS_ERROR' FILE. ", "black", "on_white")
                    time.sleep(3)
                    file.write(dt + " " + event + " " + str(error) + "\n")
                file.close()
            __init__()

def write_file():
    infoos.information(infoos)
    termcolor.cprint("           -- THE CREATE A FILE --           ", "white", "on_red")
    print()
    fileW = str(input("ENTER FILE NAME: "))
    infoos.information(infoos)
    with open(fileW, "a") as f:
        if f.writable():
            termcolor.cprint("NAME FILE: " f"{fileW}", "black", "on_white")
            f.write(str(input("ENTER TEXT: ") + "\n"))
        f.close()
    alert_read()

def read_file():
    infoos.information(infoos)
    termcolor.cprint("           -- THE READ A TEXT FILE --           ", "white", "on_red")
    print()
    fileR = str(input("ENTER FILE NAME: "))
    infoos.information(infoos)
    with open(fileR, "r") as file:
        if file.readable():
            termcolor.cprint("    -- THE CONTENTS A FILE --    ", "black", "on_white")
            txt = file.read()
            print(txt)
        file.close()
    print()
    print()
    input(termcolor.colored(" PLEASE PRESS ANY KEY TO CONTINUE... ", "black", "on_white"))
    __init__()

def alert_write():
    infoos.information(infoos)
    termcolor.cprint("DO YOU WANT WRITE FILE? (y/n)", "white", "on_red")
    print()
    optionW = str(input("YOUR CHOOSE: "))
    if optionW == "y" or optionW == "Y":
        write_file()
    elif optionW == "n" or optionW == "N":
        alert_read()
    else:
        alert_write()

def alert_read():
    infoos.information(infoos)
    termcolor.cprint("DO YOU WANT READ FILE? (y/n)", "white", "on_red")
    print()
    optionR = str(input("YOUR CHOOSE: "))
    if optionR == "y" or optionR == "Y":
        read_file()
    elif optionR == "n" or optionR == "N":
        __init__()
    else:
        alert_read()

def loading_bar():
    infoos.information(infoos)
    def progress_bar(progress, total, color=colorama.Fore.WHITE):
        infoos.information(infoos)
        termcolor.cprint(" LOADING SYSTEM... ", "white", "on_red")
        percent = 100 * (progress / float(total))
        bar = termcolor.colored(" ", "white", "on_white") * int(percent) + " " * (100 - int(percent))
        print(color + f"\r|{bar}| {percent:.2f}%", end="\r")
    numbers = [x * 5 for x in range(2000, 3000)]
    results = []
    progress_bar(0, len(numbers))
    for i, x in enumerate(numbers):
        results.append(math.factorial(x))
        progress_bar(i + 1, len(numbers))
    print(colorama.Fore.RESET)
    __init__()

def system_exit():
    infoos.information(infoos)
    termcolor.cprint(" DO YOU WANT CLOSE THE PROGRAM (y/n) ", "white", "on_red")
    print()
    optionEP = input("YOUR CHOOSE: ")
    if optionEP == "y" or optionEP == "Y":
        infoos.information(infoos)
        termcolor.cprint("                        POLPIOTECH®                      ", "white", "on_red")
        termcolor.cprint("░░░░░░░░░░░░░░░░░░░░░░░░░░░░█                            ", "black", "on_white")
        termcolor.cprint("░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄█▄▄                          ", "black", "on_white")
        termcolor.cprint("░░░░░░░░░░░░░░░░░░░░░░▀▀▀██▀▀▀██▀▀▀                      ", "black", "on_white")
        termcolor.cprint("░░░░░░░░░░░░░░░░░░▄▄▄▄▄▄▄███████▄▄▄▄▄▄▄                  ", "black", "on_white")
        termcolor.cprint("░░░░░░░░░░░░░░░░░░░░█▄█░░▀██▄██▀░░█▄█                    ", "black", "on_white")
        termcolor.cprint("                -- THE PROGRAM CLOSED --                 ", "white", "on_red")
        sys.exit()
    elif optionEP == "n" or optionEP == "N":
        infoos.information(infoos)
        __init__()
    else:
        infoos.information(infoos)
        system_exit()

def login_panel():
    infoos.information(infoos)
    termcolor.cprint("                        POLPIOTECH®                      ", "white", "on_red")
    termcolor.cprint("░░░░░░░░░░░░░░░░░░░░░░░░░░░░█                            ", "black", "on_white")
    termcolor.cprint("░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄█▄▄                          ", "black", "on_white")
    termcolor.cprint("░░░░░░░░░░░░░░░░░░░░░░▀▀▀██▀▀▀██▀▀▀                      ", "black", "on_white")
    termcolor.cprint("░░░░░░░░░░░░░░░░░░▄▄▄▄▄▄▄███████▄▄▄▄▄▄▄                  ", "black", "on_white")
    termcolor.cprint("░░░░░░░░░░░░░░░░░░░░█▄█░░▀██▄██▀░░█▄█                    ", "black", "on_white")
    termcolor.cprint("                  -- THE LOGIN PANEL --                  ", "white", "on_red")
    print()
    login = getpass.getpass(str("LOGIN: "))
    password = getpass.getpass(str("PASSWORD: "))
    if login == str("polpiotech") and password == str("PL!"):
        print()
        termcolor.cprint("  LOGIN AND PASSWORD CORRECT!  ", "white", "on_green")
        time.sleep(3)
        loading_bar()
    else:
        print()
        termcolor.cprint("  LOGIN OR PASSWORD INCORECT!  ", "white", "on_red")
        time.sleep(3)

def system_update():
    while True:
        try:
            infoos.information(infoos)
            termcolor.cprint(" DO YOU WANT PERFORM TO THE UPDATE SYSTEM? (y/n) ", "white", "on_red")
            print()
            optionSU = input("YOUR CHOOSE: ")
            if optionSU == "y" or optionSU == "Y":
                infoos.information(infoos)
                termcolor.cprint("           -- THE OPERATION SYSTEM UPDATE --          ", "white", "on_red")
                termcolor.cprint("  ────────────────────────────▄▄───▐█──────────────   ", "black", "on_white")
                termcolor.cprint("  ────────────────▄▄▄───▄██▄──█▀───█─▄─────────────   ", "black", "on_white")
                termcolor.cprint("  ──────────────▄██▀█▌─██▄▄──▐█▀▄─▐█▀──────────────   ", "black", "on_white")
                termcolor.cprint("  ─────────────▐█▀▀▌───▄▀▌─▌─█─▌──▌─▌──────────────   ", "black", "on_white")
                termcolor.cprint("  ─────────────▌▀▄─▐──▀▄─▐▄─▐▄▐▄─▐▄─▐▄─────────────   ", "black", "on_white")
                termcolor.cprint("             I'M DEVELOPING TO MY SKILLS...           ", "white", "on_red")
                print()
                os.system("sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade -y | tee -a './logs/system/logs_system_update.txt'")
                print()
                termcolor.cprint("  THE PROCESS IS COMPLATED.  ", "white", "on_green")
                time.sleep(3)
                __init__()
            elif optionSU == "n" or optionSU == "N":
                __init__()
            else:
                system_update()
        except Exception as otherExcepts:
            dt = str(datetime.datetime.now())[0:19]
            event = "[ SYSTEM: UPDATE ]"
            print()
            print()
            termcolor.cprint(f" AN ERROR HAS OCCURED: {otherExcepts} ", "white", "on_red")
            time.sleep(3)
            infoos.information(infoos)
            with open("./logs/error/logs_error.txt", "a") as file:
                if file.writable():
                    error = otherExcepts
                    termcolor.cprint(" MORE INFORMATION ABOUT THE ERROR CAN BE FOUND IN THE 'LOGS_ERROR' FILE. ", "black", "on_white")
                    time.sleep(3)
                    file.write(dt + " " + event + " " + str(error) + "\n")
                file.close()
            __init__()

def system_clean():
    while True:
        try:
            infoos.information(infoos)
            termcolor.cprint(" DO YOU WANT PERFORM TO THE CLEAR OPERATION SYSTEM? (y/n) ", "white", "on_red")
            print()
            optionCS = input("YOUR CHOOSE: ")
            if optionCS == "y" or optionCS == "Y":
                infoos.information(infoos)
                termcolor.cprint("            -- THE OPERATION SYSTEM CLEAN --          ", "white", "on_red")
                termcolor.cprint("  ────────────────────────────▄▄───▐█──────────────   ", "black", "on_white")
                termcolor.cprint("  ────────────────▄▄▄───▄██▄──█▀───█─▄─────────────   ", "black", "on_white")
                termcolor.cprint("  ──────────────▄██▀█▌─██▄▄──▐█▀▄─▐█▀──────────────   ", "black", "on_white")
                termcolor.cprint("  ─────────────▐█▀▀▌───▄▀▌─▌─█─▌──▌─▌──────────────   ", "black", "on_white")
                termcolor.cprint("  ─────────────▌▀▄─▐──▀▄─▐▄─▐▄▐▄─▐▄─▐▄─────────────   ", "black", "on_white")
                termcolor.cprint("                 I'M DOING CLEANING...                ", "white", "on_red")
                print()
                os.system("sudo apt clean && sudo apt autoclean && sudo apt autoremove | tee -a './logs/system/logs_clear_system.txt'")
                print()
                termcolor.cprint("  THE PROCESS IS COMPLATED.  ", "white", "on_green")
                time.sleep(3)
                __init__()
            elif optionCS == "n" or optionCS == "N":
                __init__()
            else:
                system_clean()
        except Exception as otherExcepts:
            dt = str(datetime.datetime.now())[0:19]
            event = "[ SYSTEM: CLEAR ]"
            print()
            print()
            termcolor.cprint(f" AN ERROR HAS OCCURED: {otherExcepts} ", "white", "on_red")
            time.sleep(3)
            infoos.information(infoos)
            with open("./logs/error/logs_error.txt", "a") as file:
                if file.writable():
                    error = otherExcepts
                    termcolor.cprint(" MORE INFORMATION ABOUT THE ERROR CAN BE FOUND IN THE 'LOGS_ERROR' FILE. ", "black", "on_white")
                    time.sleep(3)
                    file.write(dt + " " + event + " " + str(error) + "\n")
                file.close()
            __init__()

def backup_desktop(scr=str("/home/rekbod/Desktop/"), dst=str("/media/rekbod/F5AF-B248/Kubuntu/"), drc=str(datetime.datetime.now())[0:10]):
    while True:
        try:
            infoos.information(infoos)
            termcolor.cprint(" DO YOU WANT PERFORM TO THE PROCESS BACKUP? (y/n) ", "white", "on_red")
            print()
            optionBC = str(input("YOUR CHOOSE: "))
            if optionBC == "y" or optionBC == "Y":
                infoos.information(infoos)
                termcolor.cprint("         -- THE BACKUP DESKTOP --         ", "white", "on_red")
                termcolor.cprint("         █▓▒▓█▀██▀█▄░░▄█▀██▀█▓▒▓█         ", "black", "on_white")
                termcolor.cprint("         █▓▒░▀▄▄▄▄▄█░░█▄▄▄▄▄▀░▒▓█         ", "black", "on_white")
                termcolor.cprint("         █▓▓▒░░░░░▒▓░░▓▒░░░░░▒▓▓█         ", "black", "on_white")
                termcolor.cprint("            I CAN REMEMBER...             ", "white", "on_red")
                print()
                nd = dst + drc
                termcolor.cprint(" THE COPYING IN PROGRESS. PLEASE WAIT... ", "black", "on_white")
                shutil.copytree(scr, nd, dirs_exist_ok=True)
                print()
                termcolor.cprint("  THE PROCESS IS COMPLATED.  ", "white", "on_green")
                time.sleep(3)
                infoos.information(infoos)
                termcolor.cprint("  -- THE BACKUP FILES AND DIRECTORY FROM DESKTOP --  ", "black", "on_white")
                print()
                os.chdir(dst + drc)
                pathisdir = os.path.isdir(".")
                termcolor.colored(print("DIRECTORY EXIST: ", pathisdir), "white", "on_blue")
                print()
                termcolor.cprint(" -- THE BACKUP CONTENT IN DIRECTORY -- ", "black", "on_white")
                for item in os.listdir("."):
                    if os.path.isdir(item):
                        termcolor.cprint("{} - [ D ]".format(item), "white", "on_light_green")
                    else:
                        termcolor.cprint("{} - [ F ]".format(item), "white", "on_green")
                print()
                print()
                input(termcolor.colored(" PLEASE PRESS ANY KEY TO CONTINUE... ", "black", "on_white"))
                __init__()
            elif optionBC == "n" or optionBC == "N":
                __init__()
            else:
                backup_desktop()
        except Exception as otherExcepts:
            dt = str(datetime.datetime.now())[0:19]
            event = "[ BACKUP: DESKTOP ]"
            print()
            print()
            termcolor.cprint(f" AN ERROR HAS OCCURED: {otherExcepts} ", "white", "on_red")
            time.sleep(3)
            infoos.information(infoos)
            with open("./logs/error/logs_error.txt", "a") as file:
                if file.writable():
                    error = otherExcepts
                    termcolor.cprint(" MORE INFORMATION ABOUT THE ERROR CAN BE FOUND IN THE 'LOGS_ERROR' FILE. ", "black", "on_white")
                    time.sleep(3)
                    file.write(dt + " " + event + " " + str(error) + "\n")
                file.close()
            __init__()

def antivirus():
    infoos.information(infoos)
    termcolor.cprint("            -- THE SYSTEM ANTIVIRUS --            ", "black", "on_white")
    termcolor.cprint("                                                  ", "red", "on_red")
    termcolor.cprint("──────────────────█─▄▀█──█▀▄─█────────────────────", "black", "on_white")
    termcolor.cprint("─────────────────▐▌──────────▐▌───────────────────", "black", "on_white")
    termcolor.cprint("─────────────────█▌▀▄──▄▄──▄▀▐█───────────────────", "black", "on_white")
    termcolor.cprint("────────────────▐██──▀▀──▀▀──██▌──────────────────", "black", "on_white")
    termcolor.cprint("───────────────▄████▄──▐▌──▄████▄─────────────────", "black", "on_white")
    termcolor.cprint("             I'M LOOKING FOR THREAT...            ", "white", "on_red")
    print()
    print(" [1] - THE UPDATE SIGNATURE DATABASE.")
    print(" [2] - THE FILE SCAN.")
    print(" [3] - THE DIRECTORY SCAN.")
    print(" [4] - THE SCAN DIRECTORY AND SUBDIRECTORIES.")
    print(" [5] - THE SCAN OF THE USER DIRECTORY.")
    print(" [6] - THE SCAN LOGS.")
    print(" [0] - EXIT.")
    print()
    optionAV = str(input("YOUR CHOOSE: "))
    if optionAV == str(1):
        antivirus_update()
    elif optionAV == str(2):
        antivirus_scan_file()
    elif optionAV == str(3):
        antivirus_scan_directory()
    elif optionAV == str(4):
        antivirus_scan_directory_and_subdirectory()
    elif optionAV == str(5):
        antivirus_scan_of_the_user_directory()
    elif optionAV == str(6):
        antivirus_request_log()
    elif optionAV == str(0):
        antivirus_exit()
    else:
        infoos.information(infoos)
        antivirus()

def antivirus_exit():
    infoos.information(infoos)
    termcolor.cprint("  DO YOU WANT COME BACK TO THE MAIN MENU? (y/n)  ", "white", "on_red")
    print()
    optionAVE = str(input("YOUR CHOOSE: "))
    if optionAVE == "y" or optionAVE == "Y":
        infoos.information(infoos)
        __init__()
    elif optionAVE == "n" or optionAVE == "N":
        infoos.information(infoos)
        antivirus()
    else:
        infoos.information(infoos)
        antivirus_exit()

def antivirus_update():
    while True:
        try:
            infoos.information(infoos)
            termcolor.cprint(" DO YOU WANT PERFORM TO THE UPDATE SIGNATURE DATABASE? (y/n)", "white", "on_red")
            print()
            optionASU = str(input("YOUR CHOOSE: "))
            if optionASU == "y" or optionASU == "Y":
                infoos.information(infoos)
                termcolor.cprint("  -- THE SYSTEM ANTIVIRUS UPDATE --  ", "black", "on_white")
                print()
                termcolor.cprint("  SIGNATURE DATABASE UPDATE HAS STARTED, PLEASE WAIT.  ", "white", "on_red")
                print()
                os.system("sudo freshclam | tee -a './logs/clamav/logs_update_signature.txt'")
                print()
                termcolor.cprint("  THE PROCESS IS COMPLATED.  ", "white", "on_green")
                time.sleep(3)
                antivirus()
            elif optionASU == "n" or optionASU == "N":
                infoos.information(infoos)
                antivirus()
            else:
                infoos.information(infoos)
                antivirus_update()
        except Exception as otherExcepts:
            dt = str(datetime.datetime.now())[0:19]
            event = "[ CLAM: UPDATE ]"
            print()
            print()
            termcolor.cprint(f" AN ERROR HAS OCCURED: {otherExcepts} ", "white", "on_red")
            time.sleep(3)
            infoos.information(infoos)
            with open("./logs/error/logs_error.txt", "a") as file:
                if file.writable():
                    error = otherExcepts
                    termcolor.cprint(" MORE INFORMATION ABOUT THE ERROR CAN BE FOUND IN THE 'LOGS_ERROR' FILE. ", "black", "on_white")
                    time.sleep(3)
                    file.write(dt + " " + event + " " + str(error) + "\n")
                file.close()
            antivirus()

def antivirus_scan_file():
    while True:
        try:
            infoos.information(infoos)
            termcolor.cprint(" DO YOU WANT PERFORM TO THE SCAN FILE? (y/n)", "white", "on_red")
            print()
            optionASF = str(input("YOUR CHOOSE: "))
            if optionASF == "y" or optionASF == "Y":
                infoos.information(infoos)
                termcolor.cprint("  -- THE SYSTEM ANTIVIRUS SCAN FILE --  ", "black", "on_white")
                print()
                pathSF = str(input("ENTER THE PATH TO FILE: "))
                infoos.information(infoos)
                termcolor.cprint("  THE FILE SCAN PROCESS HAS STARTED, PLEASE WAIT.  ", "white", "on_red")
                print()
                os.system("sudo clamscan -v " + pathSF + " | tee -a './logs/clamav/logs_file_scan.txt'")
                print()
                termcolor.cprint("  THE FILE SCAN PROCESS DONE.  ", "white", "on_green")
                time.sleep(3)
                print()
                print()
                input(termcolor.colored(" PLEASE PRESS ANY KEY TO CONTINUE... ", "black", "on_white"))
                antivirus()
            elif optionASF == "n" or optionASF == "N":
                infoos.information(infoos)
                antivirus()
            else:
                infoos.information(infoos)
                antivirus_scan_file()
        except Exception as otherExcepts:
            dt = str(datetime.datetime.now())[0:19]
            event = "[ CLAM: SCAN FILE ]"
            print()
            print()
            termcolor.cprint(f" AN ERROR HAS OCCURED: {otherExcepts} ", "white", "on_red")
            time.sleep(3)
            infoos.information(infoos)
            with open("./logs/error/logs_error.txt", "a") as file:
                if file.writable():
                    error = otherExcepts
                    termcolor.cprint(" MORE INFORMATION ABOUT THE ERROR CAN BE FOUND IN THE 'LOGS_ERROR' FILE. ", "black", "on_white")
                    time.sleep(3)
                    file.write(dt + " " + event + " " + str(error) + "\n")
                file.close()
            antivirus()

def antivirus_scan_directory():
    while True:
        try:
            infoos.information(infoos)
            termcolor.cprint(" DO YOU WANT PERFORM TO THE SCAN DIRECTORY? (y/n)", "white", "on_red")
            print()
            optionASD = str(input("YOUR CHOOSE: "))
            if optionASD == "y" or optionASD == "Y":
                infoos.information(infoos)
                termcolor.cprint("  -- THE SYSTEM ANTIVIRUS SCAN DIRECTORY --  ", "black", "on_white")
                print()
                pathSD = str(input("ENTER THE PATH TO DIRECTORY: "))
                infoos.information(infoos)
                termcolor.cprint("  THE DIRECTORY SCAN PROCESS HAS STARTED, PLEASE WAIT...  ", "white", "on_red")
                print()
                os.system("sudo clamscan " + pathSD + " | tee -a './logs/clamav/logs_directory_scan.txt'")
                print()
                termcolor.cprint("  THE PROCESS IS COMPLATED.  ", "white", "on_green")
                time.sleep(3)
                print()
                print()
                input(termcolor.colored(" PLEASE PRESS ANY KEY TO CONTINUE... ", "black", "on_white"))
                antivirus()
            elif optionASD == "n" or optionASD == "N":
                infoos.information(infoos)
                antivirus()
            else:
                infoos.information(infoos)
                antivirus_scan_directory()
        except Exception as otherExcepts:
            dt = str(datetime.datetime.now())[0:19]
            event = "[ CLAM: SCAN DIR ]"
            print()
            print()
            termcolor.cprint(f" AN ERROR HAS OCCURED: {otherExcepts} ", "white", "on_red")
            time.sleep(3)
            infoos.information(infoos)
            with open("./logs/error/logs_error.txt", "a") as file:
                if file.writable():
                    error = otherExcepts
                    termcolor.cprint(" MORE INFORMATION ABOUT THE ERROR CAN BE FOUND IN THE 'LOGS_ERROR' FILE. ", "black", "on_white")
                    time.sleep(3)
                    file.write(dt + " " + event + " " + str(error) + "\n")
                file.close()
            antivirus()

def antivirus_scan_directory_and_subdirectory():
    while True:
        try:
            infoos.information(infoos)
            termcolor.cprint(" DO YOU WANT PERFORM TO THE SCAN DIRECTORY AND SUBDIRECTORY? (y/n)", "white", "on_red")
            print()
            optionASDAS = str(input("YOUR CHOOSE: "))
            if optionASDAS == "y" or optionASDAS == "Y":
                infoos.information(infoos)
                termcolor.cprint("  -- THE SYSTEM ANTIVIRUS SCAN DIRECTORY AND SUBDIRECTORY --  ", "black", "on_white")
                print()
                pathSDS = str(input("ENTER THE PATH TO DIRECTORY: "))
                infoos.information(infoos)
                termcolor.cprint("  THE DIRECTORY AND SUBDIRECTORY SCAN PROCESS HAS STARTED, PLEASE WAIT.  ", "white", "on_red")
                print()
                os.system("sudo clamscan -r " + pathSDS + " | tee -a './logs/clamav/logs_subdirectory_scan.txt'")
                print()
                termcolor.cprint("  THE PROCESS IS COMPLATED.  ", "white", "on_green")
                time.sleep(3)
                print()
                print()
                input(termcolor.colored(" PLEASE PRESS ANY KEY TO CONTINUE... ", "black", "on_white"))
                antivirus()
            elif optionASDAS == "n" or optionASDAS == "N":
                infoos.information(infoos)
                antivirus()
            else:
                infoos.information(infoos)
                antivirus_scan_directory_and_subdirectory()
        except Exception as otherExcepts:
            dt = str(datetime.datetime.now())[0:19]
            event = "[ CLAM: SCAN SUBDIR ]"
            print()
            print()
            termcolor.cprint(f" AN ERROR HAS OCCURED: {otherExcepts} ", "white", "on_red")
            time.sleep(3)
            infoos.information(infoos)
            with open("./logs/error/logs_error.txt", "a") as file:
                if file.writable():
                    error = otherExcepts
                    termcolor.cprint(" MORE INFORMATION ABOUT THE ERROR CAN BE FOUND IN THE 'LOGS_ERROR' FILE. ", "black", "on_white")
                    time.sleep(3)
                    file.write(dt + " " + event + " " + str(error) + "\n")
                file.close()
            antivirus()

def antivirus_scan_of_the_user_directory():
    while True:
        try:
            infoos.information(infoos)
            termcolor.cprint(" DO YOU WANT PERFORM TO THE SCAN OF THE USER DIRECTORY? (y/n)", "white", "on_red")
            print()
            optionASUD = str(input("YOUR CHOOSE: "))
            if optionASUD == "y" or optionASUD == "Y":
                infoos.information(infoos)
                termcolor.cprint("  -- THE SYSTEM ANTIVIRUS SCAN OF THE USER DIRECTORY --  ", "black", "on_white")
                print()
                infoos.information(infoos)
                termcolor.cprint("  THE USER DIRECTORY SCAN PROCESS HAS STARTED, PLEASE WAIT.  ", "white", "on_red")
                print()
                os.system("sudo clamscan -rv ~/ | tee -a './logs/clamav/logs_user_directory_scan.txt'")
                print()
                termcolor.cprint("  THE PROCESS IS COMPLATED.  ", "white", "on_green")
                time.sleep(3)
                print()
                print()
                input(termcolor.colored(" PLEASE PRESS ANY KEY TO CONTINUE... ", "black", "on_white"))
                antivirus()
            elif optionASUD == "n" or optionASUD == "N":
                infoos.information(infoos)
                antivirus()
            else:
                infoos.information(infoos)
                antivirus_scan_of_the_user_directory()
        except Exception as otherExcepts:
            dt = str(datetime.datetime.now())[0:19]
            event = "[ CLAM: SCAN USER DIR ]"
            print()
            print()
            termcolor.cprint(f" AN ERROR HAS OCCURED: {otherExcepts} ", "white", "on_red")
            time.sleep(3)
            infoos.information(infoos)
            with open("./logs/error/logs_error.txt", "a") as file:
                if file.writable():
                    error = otherExcepts
                    termcolor.cprint(" MORE INFORMATION ABOUT THE ERROR CAN BE FOUND IN THE 'LOGS_ERROR' FILE. ", "black", "on_white")
                    time.sleep(3)
                    file.write(dt + " " + event + " " + str(error) + "\n")
                file.close()
            antivirus()

def antivirus_request_log():
    infoos.information(infoos)
    termcolor.cprint(" DO YOU WANT VIEW TO THE SCAN LOG? (y/n) ", "white", "on_red")
    print()
    optionVL = input("YOUR CHOOSE: ")
    if optionVL == "y" or optionVL == "Y":
        antivirus_view_log()
    elif optionVL == "n" or optionVL == "N":
        antivirus()
    else:
        antivirus_request_log()

def antivirus_view_log():
    infoos.information(infoos)
    termcolor.cprint("         -- VIEW THE SCAN LOGS --           ", "white", "on_red")
    termcolor.cprint("───────────────█─▄▀█──█▀▄─█─────────────────", "black", "on_white")
    termcolor.cprint("──────────────▐▌──────────▐▌────────────────", "black", "on_white")
    termcolor.cprint("──────────────█▌▀▄──▄▄──▄▀▐█────────────────", "black", "on_white")
    termcolor.cprint("─────────────▐██──▀▀──▀▀──██▌───────────────", "black", "on_white")
    termcolor.cprint("────────────▄████▄──▐▌──▄████▄──────────────", "black", "on_white")
    termcolor.cprint("             LOOK WHAT I FOUND              ", "white", "on_red")
    print()
    print(" [1] - OPEN THE UPDATE LOGS. ")
    print(" [2] - OPEN THE FILE SCAN LOGS. ")
    print(" [3] - OPEN THE DIRECTORY SCAN LOGS. ")
    print(" [4] - OPEN THE SUBDIRECTORY SCAN LOGS. ")
    print(" [5] - OPEN THE USER OF DIRECTORY SCAN LOGS.")
    print(" [0] - EXIT. ")
    print()
    optionOL = input("YOUR CHOOSE: ")
    if optionOL == "1":
        open_update_log()
    elif optionOL == "2":
        open_file_scan_log()
    elif optionOL == "3":
        open_directory_scan_log()
    elif optionOL == "4":
        open_subdirectory_scan_log()
    elif optionOL == "5":
        open_user_directory_scan_log()
    elif optionOL == "0":
        antivirus_view_log_exit()
    else:
        antivirus_view_log()

def open_user_directory_scan_log():
    infoos.information(infoos)
    termcolor.cprint(" DO YOU WANT OPEN THE SCAN USER OF DIRECTORY LOGS? (y/n) ", "white", "on_red")
    print()
    optionOUDCL = input("YOUR CHOOSE: ")
    if optionOUDCL == "y" or optionOUDCL == "Y":
        infoos.information(infoos)
        termcolor.cprint("  -- THE SCAN USER OF DIRECTORY LOGS --  ", "black", "on_white")
        print()
        source = "./logs/clamav/logs_user_directory_scan.txt"
        with open(source, "r") as file:
            if file.readable():
                for i in range(101):
                    print("\rLOADING LOGS: {}%".format(i), end="")
                    time.sleep(0.03)
                infoos.information(infoos)
                termcolor.cprint("  -- THE SCAN USER OF DIRECTORY LOGS --  ", "black", "on_white")
                print()
                logSUD = file.read()
                print(logSUD)
            file.close()
        print()
        print()
        input(termcolor.colored(" PLEASE PRESS ANY KEY TO CONTINUE... ", "black", "on_white"))
        antivirus_view_log()
    elif optionOUDCL == "n" or optionOUDCL == "N":
        antivirus_view_log()
    else:
        open_user_directory_scan_log()

def open_subdirectory_scan_log():
    infoos.information(infoos)
    termcolor.cprint(" DO YOU WANT OPEN THE SCAN DIRECTORY AND SUBDIRECTORY LOGS? (y/n) ", "white", "on_red")
    print()
    optionOSDCL = input("YOUR CHOOSE: ")
    if optionOSDCL == "y" or optionOSDCL == "Y":
        infoos.information(infoos)
        termcolor.cprint("  -- THE SCAN DIRECTORY AND SUBDIRECTORY LOGS --  ", "black", "on_white")
        print()
        source = "./logs/clamav/logs_subdirectory_scan.txt"
        with open(source, "r") as file:
            if file.readable():
                for i in range(101):
                    print("\rLOADING LOGS: {}%".format(i), end="")
                    time.sleep(0.03)
                infoos.information(infoos)
                termcolor.cprint("  -- THE SCAN DIRECTORY AND SUBDIRECTORY LOGS --  ", "black", "on_white")
                print()
                logSSD = file.read()
                print(logSSD)
            file.close()
        print()
        print()
        input(termcolor.colored(" PLEASE PRESS ANY KEY TO CONTINUE... ", "black", "on_white"))
        antivirus_view_log()
    elif optionOSDCL == "n" or optionOSDCL == "N":
        antivirus_view_log()
    else:
        open_subdirectory_scan_log()

def open_directory_scan_log():
    infoos.information(infoos)
    termcolor.cprint(" DO YOU WANT OPEN THE SCAN DIRECTORY LOGS? (y/n) ", "white", "on_red")
    print()
    optionODCL = input("YOUR CHOOSE: ")
    if optionODCL == "y" or optionODCL == "Y":
        infoos.information(infoos)
        termcolor.cprint("  -- THE SCAN DIRECTORY LOGS --  ", "black", "on_white")
        print()
        source = "./logs/clamav/logs_directory_scan.txt"
        with open(source, "r") as file:
            if file.readable():
                for i in range(101):
                    print("\rLOADING LOGS: {}%".format(i), end="")
                    time.sleep(0.03)
                infoos.information(infoos)
                termcolor.cprint("  -- THE SCAN DIRECTORY LOGS --  ", "black", "on_white")
                print()
                logSD = file.read()
                print(logSD)
            file.close()
        print()
        print()
        input(termcolor.colored(" PLEASE PRESS ANY KEY TO CONTINUE... ", "black", "on_white"))
        antivirus_view_log()
    elif optionODCL == "n" or optionODCL == "N":
        antivirus_view_log()
    else:
        open_directory_scan_log()

def open_file_scan_log():
    infoos.information(infoos)
    termcolor.cprint(" DO YOU WANT OPEN THE SCAN FILE LOGS? (y/n) ", "white", "on_red")
    print()
    optionOFCL = input("YOUR CHOOSE: ")
    if optionOFCL == "y" or optionOFCL == "Y":
        infoos.information(infoos)
        termcolor.cprint("  -- THE SCAN FILE LOGS --  ", "black", "on_white")
        print()
        source = "./logs/clamav/logs_file_scan.txt"
        with open(source, "r") as file:
            if file.readable():
                for i in range(101):
                    print("\rLOADING LOGS: {}%".format(i), end="")
                    time.sleep(0.03)
                infoos.information(infoos)
                termcolor.cprint("  -- THE SCAN FILE LOGS --  ", "black", "on_white")
                print()
                logSF = file.read()
                print(logSF)
            file.close()
        print()
        print()
        input(termcolor.colored(" PLEASE PRESS ANY KEY TO CONTINUE... ", "black", "on_white"))
        antivirus_view_log()
    elif optionOFCL == "n" or optionOFCL == "N":
        antivirus_view_log()
    else:
        open_file_scan_log()

def open_update_log():
    infoos.information(infoos)
    termcolor.cprint(" DO YOU WANT OPEN THE UPDATE LOGS? (y/n) ", "white", "on_red")
    print()
    optionOUL = input("YOUR CHOOSE: ")
    if optionOUL == "y" or optionOUL == "Y":
        infoos.information(infoos)
        termcolor.cprint("  -- THE UPDATE LOGS --  ", "black", "on_white")
        print()
        source = "./logs/clamav/logs_update_signature.txt"
        with open(source, "r") as file:
            if file.readable():
                for i in range(101):
                    print("\rLOADING LOGS: {}%".format(i), end="")
                    time.sleep(0.03)
                infoos.information(infoos)
                termcolor.cprint("  -- THE UPDATE LOGS --  ", "black", "on_white")
                print()
                logU = file.read()
                print(logU)
            file.close()
        print()
        print()
        input(termcolor.colored(" PLEASE PRESS ANY KEY TO CONTINUE... ", "black", "on_white"))
        antivirus_view_log()
    elif optionOUL == "n" or optionOUL == "N":
        antivirus_view_log()
    else:
        open_update_log()

def antivirus_view_log_exit():
    infoos.information(infoos)
    termcolor.cprint(" DO YOU WANT COME BACK TO THE ANTIVIRUS MENU? (y/n) ", "white", "on_red")
    print()
    optionAVLE = input("YOUR CHOOSE: ")
    if optionAVLE == "y" or optionAVLE == "Y":
        infoos.information(infoos)
        antivirus()
    elif optionAVLE == "n" or optionAVLE == "N":
        infoos.information(infoos)
        antivirus_view_log()
    else:
        infoos.information(infoos)
        antivirus_view_log_exit()

def rootkit():
    infoos.information(infoos)
    termcolor.cprint("            -- THE SYSTEM ANTIROOTKIT --              ", "black", "on_white")
    termcolor.cprint("                                                      ", "red", "on_red")
    termcolor.cprint("───────────────────█─▄▀█──█▀▄─█───────────────────────", "black", "on_white")
    termcolor.cprint("──────────────────▐▌──────────▐▌──────────────────────", "black", "on_white")
    termcolor.cprint("──────────────────█▌▀▄──▄▄──▄▀▐█──────────────────────", "black", "on_white")
    termcolor.cprint("─────────────────▐██──▀▀──▀▀──██▌─────────────────────", "black", "on_white")
    termcolor.cprint("────────────────▄████▄──▐▌──▄████▄────────────────────", "black", "on_white")
    termcolor.cprint("                                                      ", "red", "on_red")
    print()
    termcolor.cprint("           [R] - INSTALL RKHUNTER.                    ", "black", "on_white")
    termcolor.cprint("          [RH] - Configuration information.           ", "black", "on_white")
    termcolor.cprint("           [C] - INSTALL CHKROOTKI.                   ", "black", "on_white")
    termcolor.cprint("          [CH] = Configuration information.           ", "black", "on_white")
    print()
    print(" [1] - [ RKROOTKIT ]: THE UPDATE SIGNATURES DATABASE.")
    print(" [2] - [ RKROOTKIT ]: THE SCAN OPERATION SYSTEM.")
    print(" [3] - [ RKROOTKIT ]: THE VIEW SCAN LOGS.")
    print(" [4] - [ CHKROOTKI ]: THE SCAN OPERATION SYSTEM.")
    print(" [0] - EXIT.")
    print()
    optionRK = str(input("YOUR CHOOSE: "))
    if optionRK == str(1):
        rkhunter_update()
    elif optionRK == str(2):
        rkhunter_scan()
    elif optionRK == str(3):
        rkhunter_log()
    elif optionRK == str(4):
        chkrootkit_scan()
    elif optionRK == str(0):
        rootkit_exit()
    elif optionRK == str("r") or optionRK == str("R"):
        install_rkhunter()
    elif optionRK == str("rh") or optionRK == str("RH"):
        configuration_rkhunter()
    elif optionRK == str("c") or optionRK == str("C"):
        install_chkrootkit()
    elif optionRK == str("ch") or optionRK == str("CH"):
        configuration_chkrootkit()
    else:
        rootkit()

def install_rkhunter():
    while True:
        try:
            infoos.information(infoos)
            termcolor.cprint(" DO YOU WANT INSTALL THE PROGRAM RKHUNTER? (y/n) ", "white", "on_red")
            print()
            optionIRKR = str(input("YOUR CHOOSE: "))
            if optionIRKR == "y" or optionIRKR == "Y":
                infoos.information(infoos)
                termcolor.cprint("  -- THE INSTALLATION RKHUNTER --  ", "black", "on_white")
                print()
                os.system("sudo apt-get install curl rkhunter -y")
                print()
                termcolor.cprint(" THE INSTALATION IS COMLETED.  ", "white", "on_green")
                time.sleep(3)
                infoos.information(infoos)
                rootkit()
            elif optionIRKR == "n" or optionIRKR == "N":
                infoos.information(infoos)
                rootkit()
            else:
                infoos.information(infoos)
                install_rkhunter()
        except Exception as otherExcepts:
            dt = str(datetime.datetime.now())[0:19]
            event = "[ RKHUNTER: INSTALL ]"
            print()
            print()
            termcolor.cprint(f" AN ERROR HAS OCCURED: {otherExcepts} ", "white", "on_red")
            time.sleep(3)
            infoos.information(infoos)
            with open("./logs/error/logs_error.txt", "a") as file:
                if file.writable():
                    error = otherExcepts
                    termcolor.cprint(" MORE INFORMATION ABOUT THE ERROR CAN BE FOUND IN THE 'LOGS_ERROR' FILE. ", "black", "on_white")
                    time.sleep(3)
                    file.write(dt + " " + event + " " + str(error) + "\n")
                file.close()
            rootkit()

def configuration_chkrootkit():
    infoos.information(infoos)
    termcolor.cprint(" DO YOU WANT VIEW TO THE CONFIGURATION INSTRUCTION? (y/n) ", "white", "on_red")
    print()
    optionCICH = input("YOUR CHOOSE: ")
    if optionCICH == "y" or optionCICH == "Y":
        infoos.information(infoos)
        termcolor.cprint("  -- THE CONFIGURATION INSTRUCTION CHKROOTKIT --  ", "black", "on_white")
        print()
        termcolor.cprint(
"1. We are instaling this program. \n2. After installation, we start by configuring the download of updates in the file: \
using the command 'nano /etc/chkrootkit.conf'. \n3. We can see three options: RUN_DAILY='false' - run everyday auto scan  \
(RUN_DAILY='TRUE'), RUN_DAILY_OPTS='-q' - Theres's quiet so it does not print anything on screen when running, \
DIFF_MODE='false' - If this is set to 'yes' chrootkit compares the files /var/log/chkrootkit/log.expected with  \
/var/log/chkrootkit/log.today.", "cyan")
        print()
        print()
        input(termcolor.colored(" PLEASE PRESS ANY KEY TO CONTINUE... ", "black", "on_white"))
        rootkit()
    elif optionCICH == "n" or optionCICH == "N":
        rootkit()
    else:
        configuration_chkrootkit()

def install_chkrootkit():
    while True:
        try:
            infoos.information(infoos)
            termcolor.cprint(" DO YOU WANT INSTALL THE PROGRAM CHKROOTKIT? (y/n) ", "white", "on_red")
            print()
            optionICHKR = str(input("YOUR CHOOSE: "))
            if optionICHKR == "y" or optionICHKR == "Y":
                infoos.information(infoos)
                termcolor.cprint("  -- THE INSTALLATION CHKROOTKIT --  ", "black", "on_white")
                print()
                os.system("sudo apt-get install chkrootkit -y")
                print()
                termcolor.cprint(" THE INSTALATION IS COMLETED.  ", "white", "on_green")
                time.sleep(3)
                rootkit()
            elif optionICHKR == "n" or optionICHKR == "N":
                rootkit()
            else:
                install_chkrootkit()
        except Exception as otherExcepts:
            dt = str(datetime.datetime.now())[0:19]
            event = "[ CHKROOTKIT: INSTALL ]"
            print()
            print()
            termcolor.cprint(f" AN ERROR HAS OCCURED: {otherExcepts} ", "white", "on_red")
            time.sleep(3)
            infoos.information(infoos)
            with open("./logs/error/logs_error.txt", "a") as file:
                if file.writable():
                    error = otherExcepts
                    termcolor.cprint(" MORE INFORMATION ABOUT THE ERROR CAN BE FOUND IN THE 'LOGS_ERROR' FILE. ", "black", "on_white")
                    time.sleep(3)
                    file.write(dt + " " + event + " " + str(error) + "\n")
                file.close()
            rootkit()

def chkrootkit_scan():
    infoos.information(infoos)
    termcolor.cprint(" DO YOU WANT PERFORM TO THE SCAN OPERATION SYSTEM? (y/n) ", "white", "on_red")
    print()
    optionSCHR = input("YOUR CHOOSE: ")
    if optionSCHR == "y" or optionSCHR == "Y":
        infoos.information(infoos)
        termcolor.cprint("  -- THE SCAN OPERATION SYSTEM CHKROOTKIT --  ", "black", "on_white")
        print()
        os.system("sudo chkrootkit | tee -a './logs/chkrootkit/logs_scan_chkrootkit.txt'")
        print()
        termcolor.cprint("  THE PROCESS IS COMPLATED.  ", "white", "on_green")
        time.sleep(3)
        rootkit()
    elif optionSCHR == "n" or optionSCHR == "N":
        rootkit()
    else:
        chkrootkit_scan()

def configuration_rkhunter():
    infoos.information(infoos)
    termcolor.cprint(" DO YOU WANT VIEW TO THE CONFIGURATION INSTRUCTION? (y/n) ", "white", "on_red")
    print()
    optionCIRH = str(input("YOUR CHOOSE: "))
    if optionCIRH == "y" or optionCIRH == "Y":
        infoos.information(infoos)
        termcolor.cprint("  -- THE CONFIGURATION INSTRUCTION RKHUNTER--  ", "black", "on_white")
        print()
        termcolor.cprint(
"1. We are instaling this program. \n2. After installation, we start by configuring the download of updates in the file: \
using the command 'nano /etc/rkhunter.conf'. \n3. We are looking for 'WEB_CMD=""/bin/false""' and modifying on 'WEB_CMD='. \n\
4. Then we are looking for 'MIRRORS_MODE=1' and change the option on 'MIRRORS_MODE=0'. \n5. This is the end of the configuration \
, but we should update the database. So you will to do this use the command in terminal \
\n  'sudo rkhunter --update && sudo rkhunter propupd' or you could useing my script. ", "cyan")
        print()
        print()
        input(termcolor.colored(" PLEASE PRESS ANY KEY TO CONTINUE... ", "black", "on_white"))
        rootkit()
    elif optionCIRH == "n" or optionCIRH == "N":
        rootkit()
    else:
        configuration_rkhunter()

def rkhunter_log():
    while True:
        try:
            infoos.information(infoos)
            termcolor.cprint(" DO YOU WANT OPEN THE LOG SCAN? (y/n) ", "white", "on_red")
            print()
            optionSLRKH = input("YOUR CHOOSE: ")
            if optionSLRKH == "y" or optionSLRKH == "Y":
                infoos.information(infoos)
                termcolor.cprint("  -- VIEW THE LOG SCAN --  ", "black",  "on_white")
                print()
                os.system("sudo gedit /var/log/rkhunter.log")
                print()
                termcolor.cprint("  THE PROCESS IS COMPLATED.  ", "white", "on_green")
                time.sleep(3)
                rootkit()
            elif optionSLRKH == "n" or optionSLRKH == "N":
                rootkit()
            else:
                rkhunter_log()
        except Exception as otherExcepts:
            dt = str(datetime.datetime.now())[0:19]
            event = "[ RKHUNTER: OPEN LOG ]"
            print()
            print()
            termcolor.cprint(f" AN ERROR HAS OCCURED: {otherExcepts} ", "white", "on_red")
            time.sleep(3)
            infoos.information(infoos)
            with open("./logs/error/logs_error.txt", "a") as file:
                if file.writable():
                    error = otherExcepts
                    termcolor.cprint(" MORE INFORMATION ABOUT THE ERROR CAN BE FOUND IN THE 'LOGS_ERROR' FILE. ", "black", "on_white")
                    time.sleep(3)
                    file.write(dt + " " + event + " " + str(error) + "\n")
                file.close()
            rootkit()

def rkhunter_scan():
    while True:
        try:
            infoos.information(infoos)
            termcolor.cprint(" DO YOU WANT PERFORM TO THE SCAN SYSTEM? (y/n) ", "white", "on_red")
            print()
            optionSRKH = input("YOUR CHOOSE: ")
            if optionSRKH == "y" or optionSRKH == "Y":
                infoos.information(infoos)
                termcolor.cprint("  -- SCAN THE OPERATION SYSTEM --  ", "black", "on_white")
                print()
                os.system("sudo rkhunter --check | tee -a './logs/rkhunter/logs_os_scan_rkhunter.txt'")
                print()
                termcolor.cprint("  THE PROCESS IS COMPLATED.  ", "white", "on_green")
                time.sleep(3)
                rootkit()
            elif optionSRKH == "n" or optionSRKH == "N":
                rootkit()
            else:
                rkhunter_scan()
        except Exception as otherExcepts:
            dt = str(datetime.datetime.now())[0:19]
            event = "[ RKHUNTER: SCAN ]"
            print()
            print()
            termcolor.cprint(f" AN ERROR HAS OCCURED: {otherExcepts} ", "white", "on_red")
            time.sleep(3)
            infoos.information(infoos)
            with open("./logs/error/logs_error.txt", "a") as file:
                if file.writable():
                    error = otherExcepts
                    termcolor.cprint(" MORE INFORMATION ABOUT THE ERROR CAN BE FOUND IN THE 'LOGS_ERROR' FILE. ", "black", "on_white")
                    time.sleep(3)
                    file.write(dt + " " + event + " " + str(error) + "\n")
                file.close()
            rootkit()        

def rkhunter_update():
    while True:
        try:
            infoos.information(infoos)
            termcolor.cprint(" DO YOU WANT UPDATE THE DATABASE PROGRAM RKHUNTER? (y/n) ", "white", "on_red")
            print()
            optionURKH = str(input("YOUR CHOOSE: "))
            if optionURKH == "y" or optionURKH == "Y":
                infoos.information(infoos)
                termcolor.cprint("  -- THE UPDATE SIGNATURES DATABASE --  ", "black", "on_white")
                print()
                os.system("sudo rkhunter --update && sudo rkhunter --propupd | tee -a './logs/rkhunter/logs_update_rkhunter.txt'")
                print()
                termcolor.cprint("  THE PROCESS IS COMPLATED.  ", "white", "on_green")
                time.sleep(3)
                rootkit()
            elif optionURKH == "n" or optionURKH == "N":
                rootkit()
            else:
                rkhunter_update()
        except Exception as otherExcepts:
            dt = str(datetime.datetime.now())[0:19]
            event = "[ RKHUNTER: UPDATE ]"
            print()
            print()
            termcolor.cprint(f" AN ERROR HAS OCCURED: {otherExcepts} ", "white", "on_red")
            time.sleep(3)
            infoos.information(infoos)
            with open("./logs/error/logs_error.txt", "a") as file:
                if file.writable():
                    error = otherExcepts
                    termcolor.cprint(" MORE INFORMATION ABOUT THE ERROR CAN BE FOUND IN THE 'LOGS_ERROR' FILE. ", "black", "on_white")
                    time.sleep(3)
                    file.write(dt + " " + event + " " + str(error) + "\n")
                file.close()
            rootkit()

def rootkit_exit():
    infoos.information(infoos)
    termcolor.cprint(" DO YOU WANT COME BACK TO THE MAIN MENU? (y/n) ", "white", "on_red")
    print()
    optionRKE = str(input("YOUR CHOOSE: "))
    if optionRKE == "y" or optionRKE == "Y":
        __init__()
    elif optionRKE == "n" or optionRKE == "N":
        rootkit()
    else:
        rootkit_exit()

if __name__ == "__main__":
    login_panel()