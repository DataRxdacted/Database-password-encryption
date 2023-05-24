
#LoginDatabase
from random import randint
array = [["admin", "1234"]]
encrypted = []
tempList = []
encryptionNumber = randint(1, 100)


def Encryption(tempArray):
    for x in range(len(tempArray)):
        tempList.append(tempArray[x][1])
        passwordForEncryption = tempList[x]
        seperatedPassword = list(passwordForEncryption)
    for x in range(len(seperatedPassword)):
        encrypted.append(ord(seperatedPassword[x]) * encryptionNumber)
    return(encrypted)

def Decryption(encrypted):
    decryptedPassword = ""
    for x in range(len(encrypted)):
        decryptedInt = int(encrypted[x]/encryptionNumber)
        decryptedChar = (chr(decryptedInt))
 
        decryptedPassword = decryptedPassword + decryptedChar
        print(decryptedPassword)


Encryption(array)
Decryption(encrypted)
run = True
userDatabase = [["admin","1234"]]
loggedIn = "nil"

def LogIn():
    userChoiceUser = input("Please enter your username")
    userChoicePass = input("Please enter password")
    for x in range(len(userDatabase)):
        if userDatabase[x][0] == userChoiceUser and userDatabase[x][1] == userChoicePass:
            print("Logged in")
            loggedIn = userDatabase[x]

def AccountInfo():
    if loggedIn != "nil":
        print(loggedIn)
        print("Index is ",userDatabase.index(loggedIn))
    else:
        print("Not logged in")

def DeleteAccount():
    if loggedIn != "nil":
      userDatabase.remove(loggedIn)
      loggedIn = "nil"

def Register():
    if loggedIn == "nil":
    
      noDupe = False

      userChoiceUser = input("Please choose a name")
      userChoicePass = input("Please choose a password")
  
      for x in range(len(userDatabase)):
        if userDatabase[x][0] == userChoiceUser:
          print("Username in use")
          break
        else:
          noDupe = True

      if noDupe == True:

        userDatabase.append(["",""])
        userDatabase[len(userDatabase)-1][0] = userChoiceUser
        userDatabase[len(userDatabase)-1][1] = userChoicePass
        print("registered")

    else:
      print("Logged in, please log out")


while run:


  userChoice = input("1. Log in\n2. Account Info\n3. Delete Account\n4. Register\n5. Log Out")

  if userChoice == '1':
      LogIn()

  elif userChoice == '2':
      AccountInfo()
    

  elif userChoice == '3':
      DeleteAccount()
   

  elif userChoice == '4':
      Register()


  elif userChoice == '5':
    loggedIn = "nil"
  
  elif userChoice == '6':
    print(userDatabase)

