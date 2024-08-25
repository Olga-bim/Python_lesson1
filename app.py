# username = input("Enter username:")
# print("Username is: " + username)

# email = input("Enter email:")
# print("email is: " + email )

# # #  печатает в отдельных строчках
# num = 5
# for _ in range (3):
#     print(num)

# # # печатает как массив
#     number = 5
# numbers_list = [number] * 3
# print(numbers_list)

# # # печатает в одну строчку подряд без запятых
# number = 5
# result = " ".join([str(number)] * 3)
# print(result)

# # # печатает в одну строчку подряд без запятых
# number = 5
# print(number, number, number)

# # # печатает в одну строчку подряд без запятых
# number = 5
# print(f"{number} " * 3)



# # печпатает умноженное число на 3
# n1 = input ("Enter a number:")
# print (f"{n1} *3  is: {3 * int(n1)}")


# напечатать числа от 0 до -100 прыжком через 5
for num in range(0, -101, -5):
    print(num)


    num = 0
while num >= -100:
    print(num)
    num -= 5

# import json
# import os

# contacts = []

# file_path = "contacts.json"

# def getUserData(contacts):
#     userName = input("Enter your name?")
#     email = input("email?")
#     contacts.append({"user": userName, "email": email})

# def clearScreen():
#       os.system('cls' if os.name == 'nt' else 'clear')

# def showContacts(contacts):
#     print("All contacts")
#     print(contacts)


# def searchContact(contacts):
#     search_name = input("Enter the name to search: ")
#     found = False
#     for contact in contacts:
#         if search_name.lower() in contact['user'].lower():
#             print(f"Name: {contact['user']}, Email: {contact['email']}")
#             found = True
#     if not found:
#         print("No contact found with that name.")

# def main():
     
#      with open('contacts.json', 'r') as file:
#         contacts = json.load(file)
#         print(contacts)

#         while True:
  
#             print ("1 - Add new contact")
#             print ("2 - del a contact")
#             print ("3 - edit contact")
#             print ("4 - show all contact")
#             print ("5 - clear")
#             print ("6 - search contact")
#             print ("x - exit")

#             userSelection = input("selection?")
#             if userSelection == "x": 
#                 with open('contacts.json', 'w') as file:
#                     json.dump(contacts, file, indent=4)
#                 return
#             if userSelection == "1": 
#                 getUserData(contacts)
#             if userSelection == "2": 
#                 # delete
#                 pass
#             if userSelection == "3": print("edit")
#             if userSelection == "5": 
#                 clearScreen()
#             if userSelection == "4": 
#                 showContacts(contacts)
#             if userSelection == "6":
#                 searchContact(contacts)

# if __name__== "__main__":
#         main()


