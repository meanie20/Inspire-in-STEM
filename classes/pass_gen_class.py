import random
class generator:
    def __init__(self, char,num_passwords,password_len):
        self.char= char
        self.num_passwords = num_passwords
        self.password_len = password_len
       
    def extra(self):
        for password in range(self.num_passwords):
            password= ' '
        for c in range(self.password_len):
            password+= random.choice(self.char)
            print(password)
        
userleft=(generator('sparrow@2022#',5,4))
print("Here are your passwords: ")
userleft.extra()


