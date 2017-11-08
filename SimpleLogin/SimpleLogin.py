# author Yuan Li

import getpass
import os

#LOCKOUTFILE = "/tmp/Lockout"
MAXATTEMPT = 3
counter = 0
Login = False

while True:
    if counter < MAXATTEMPT:
        print("--------Input Credential--------")
        username = input("Please input your username: ")
        password = getpass.getpass("Please input your password: ")

        file = open('credential', 'r')
        for line in file:
            if line == "\n":
                break
            else:
                puser = line.strip().split()[0]
                ppassword = line.strip().split()[1]

                if username == puser:
                    if os.path.exists(username) == True:
                        print("Account is lockout,please contact IT to unlock!")
                        exit()
                    elif password == ppassword:
                        Login = True
                        break

                    else:
                        counter += 1
                        Login = False
                        continue
        if Login == True:
            print("Login Successfully!")
            break
        else:
            print("Invalid Username or password!")

    else:
        print("Too many failures , the account ", username, "will be locked out!")
        open(username, 'w').close()
        break

