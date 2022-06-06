#convert pass_gen.py into a class
class user:
    def __init__(self,user_name,phone_number):
        self.user_name = user_name
        self.phone_number = phone_number
        user_input= user(input("Enter username (only letters): "),int(input("Enter phone number:")))
        return user_input
    print()
import random
class generator:
    def __init__(self, char,num_passwords,password_len):
        self.char= char
        self.num_passwords = num_passwords
        self.password_len = password_len
       

        user_input= generator(input("\nEnter username (only letters): "),int(input("How many passwords would you like to generate?")),int(input("How many characters would you like? ")))
        for password in range(self.num_passwords):
            password= ' '
        for c in range(self.password_len):
            password+= random.choice(user_input)
            print(password)
        return password