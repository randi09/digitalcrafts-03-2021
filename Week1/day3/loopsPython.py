nameOfUser = input("What is your name?")
lengthOfUserName = len(nameOfUser)

while (lengthOfUserName < 0):
    nameOfUser = input("What is your name?")
    lengthOfUserName = len(nameOfUser)

print("The user name is %s " % (nameOfUser))