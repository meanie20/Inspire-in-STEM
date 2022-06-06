import random
print("--- WELCOME TO AZTECH PASSWORD GENERATOR ---")
char='sparrow@2022'
num_passwords = int(input("\nHow many passwords would you like to generate?"))
password_len = int(input("How many characters would you like? "))

for password in range(num_passwords):
    password= ' '
    for c in range(password_len):
        password+= random.choice(char)
    print(password)


