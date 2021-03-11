user_First_Name = input("What is your first name?")
length_Of_user_First_Name = len(user_First_Name)

while(length_Of_user_First_Name < 1):
    user_First_Name = input("What is your first name?")
    length_Of_user_First_Name = len(user_First_Name)




user_Last_Name = input("What is your last name?")
length_Of_user_Last_Name = len(user_Last_Name)

while(length_Of_user_Last_Name < 1):
    user_Last_Name = input("What is your last name?")
    length_Of_user_Last_Name = len(user_Last_Name)
    
 


friends_First_name = input("What is your friends first name?")
length_Of_friends_First_name = len(friends_First_name)

while(length_Of_friends_First_name < 1):
    friends_First_name = input("What is your friends first name?")
    length_Of_friends_First_name = len(friends_First_name)




friends_Last_Name = input("What is your friends last name?")
length_Of_friends_Last_Name = len(friends_Last_Name)

while(length_Of_friends_Last_Name < 1):
    friends_Last_Name = input("What is your friends last name?")
    length_Of_friends_Last_Name = len(friends_Last_Name)
    


print("Your name %s %s" % (user_First_Name, user_Last_Name))
print("%s %s is friends with %s %s" % (user_First_Name, user_Last_Name, friends_First_name, friends_Last_Name))