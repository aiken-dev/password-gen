
import string  
import random
letters = list(string.ascii_letters)
digits = list(string.digits)
punctuation = ["!", "@", "#", "$", "%", "^", "&", "*"]

characters = letters + digits + punctuation







def generatePassword(howManyPasswords, passwordLength):
    password = ""
    while any(ele in password for ele in letters) == False and any(ele in password for ele in digits) == False and any(ele in password for ele in punctuation) == False:
        for i in range(passwordLength):
            password = password + random.choice(characters)
            

    
        
    return password

# this part of code will only run if this module is executed directly
if __name__ == "__main__": 
    howManyPasswords = input("Enter how many passwords to generate? (default: 12): ")
    passwordsFileName = input("Name the file to output passwords (default: passwords.txt): ")
    passwordLength = input("How long should each password be? (default: 14): ")


    if howManyPasswords == "":
        howManyPasswords = 12
    else:
        howManyPasswords = int(howManyPasswords)
        
    if passwordsFileName == "":
        passwordsFile = passwordsFile = open("passwords.txt", "a")
    else:

        passwordsFile = open(f"{passwordsFileName}.txt", "a")

    if passwordLength == "":
        passwordLength == 12
    else:
        passwordLength = int(passwordLength)

    for i in range(howManyPasswords):
        print(generatePassword(howManyPasswords, passwordLength))
        passwordsFile.write(f'{generatePassword(howManyPasswords, passwordLength)}\n')

    print(f"Generated {howManyPasswords} passwords, each {passwordLength} characters long and stored them in file", f"{passwordsFileName}.txt")
    passwordsFile.close()





