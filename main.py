# from generate import generatePassword

# def checkForMasterLogin():
#     masterLogin = open("masterlogin.txt", "r")
#     if masterLogin.read():
#         loginPresence = True
#         login = masterLogin.readline().split(":")
#         start(login[0], login[1])
#         masterLogin.close()
        
        
#     else:
#         loginPresence = False

#     if loginPresence == False:
#         print("Looks like it's your first time using this password manager. Please set your master login")
#         masterUsername = input("Enter master username: ")
#         masterPassword = input("Enter master password: ")
#         masterLogin = open("masterlogin.txt", "w")
#         masterLogin.write(masterUsername+":"+masterPassword)
#         masterLogin.close()

#         masterLogin = open("masterlogin.txt", "r")
#         login = masterLogin.readline().split(":")
        
        
#         start(login[0], login[1])

from generate import generatePassword
def start():
    welcome = print("Welcome to your password manager - press 1 to login: ")
    
    

    valid = False
    while valid == False:
        masterUsername = input("Enter your username for the password manager: ")
        masterPassword = input("Enter password: ")
        if masterUsername == "aiken" and masterPassword == "12345":
            valid = True
            print("Welcome to your passwords.")
            option = int(input("Press 1 to add/edit a new password or press 2 to search for a password: "))
            if option == 1:
                addPassword()
            elif option == 2:
                searchPassword()
            
        else:
            print("\nIncorrect username or password, try again!\n ")
            
        

def addPassword():
    passwordsFile = open("passwords.txt", "a")
    newLoginWebsite = input("Enter website name: ")
    newUsername = input("Enter username of new login: ")
    createUsernameMethod = input("Would you like to generate a new password? y/n: ")
    if createUsernameMethod == "y":
        newPassword = generatePassword(1, 12)
        print("Generated password: ", newPassword)
    else: 
        newPassword = input("Enter password of new password: ")
    passwordsFile.write("\n"+newLoginWebsite+"-"+newUsername+":"+newPassword)
    print("Success! Added new login")
    passwordsFile.close()
    option = int(input("\nPress 1 to add/edit a new password or press 2 to search for a password or 3 to exit: "))
    if option == 1:
        addPassword()
    elif option == 2:
        searchPassword()
    elif option == 3:
        exit()
    

def searchPassword():
    searchWebsite = input("Enter website name: ")
    passwordsFile = open("passwords.txt", "r")
    for i in passwordsFile:
        websiteName = i[:i.find("-")]
        if searchWebsite == websiteName:
            print("Found it!")
            withoutWebsiteName = websiteName = i[i.find("-")+1:]
            login = withoutWebsiteName.split(":")
            username = login[0]
            password = login[1]
            print("Username:", username)
            print("Password:", password)
    passwordsFile.close()
    option = int(input("\nPress 1 to add/edit a new password or press 2 to search for a password or 3 to exit: "))
    if option == 1:
        addPassword()
    elif option == 2:
        searchPassword()
    elif option == 3:
        exit()


start()



        