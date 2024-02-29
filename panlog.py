import sqlite3, getpass, termcolor, time
from main import loading_bar
from infoos import System as infoos


conn = sqlite3.connect("users.db")
cursor = conn.cursor()

def check_user(username, password):
    query = 'SELECT * FROM login WHERE username = ? AND password = ?'
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.commit()
    return result

def login():
    infoos.information(infoos)
    termcolor.cprint("                        POLPIOTECH®                      ", "white", "on_red")
    termcolor.cprint("░░░░░░░░░░░░░░░░░░░░░░░░░░░░█                            ", "black", "on_white")
    termcolor.cprint("░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄█▄▄                          ", "black", "on_white")
    termcolor.cprint("░░░░░░░░░░░░░░░░░░░░░░▀▀▀██▀▀▀██▀▀▀                      ", "black", "on_white")
    termcolor.cprint("░░░░░░░░░░░░░░░░░░▄▄▄▄▄▄▄███████▄▄▄▄▄▄▄                  ", "black", "on_white")
    termcolor.cprint("░░░░░░░░░░░░░░░░░░░░█▄█░░▀██▄██▀░░█▄█                    ", "black", "on_white")
    termcolor.cprint("                  -- THE LOGIN PANEL --                  ", "white", "on_red")
    print()
    username = getpass.getpass(str("USERNAME: "))
    password = getpass.getpass(str("PASSWORD: "))
    if check_user(username, password):
        print()
        termcolor.cprint("  LOGIN AND PASSWORD CORRECT!  ", "white", "on_green")
        time.sleep(3)
        loading_bar()
    else:
        print()
        termcolor.cprint("  LOGIN OR PASSWORD INCORECT!  ", "white", "on_red")
        time.sleep(3)
        login()

        

login()

cursor.close()
conn.close() 