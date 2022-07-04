def palindrome(user_input):
        rev=''.join(reversed(user_input))
        if (user_input==rev):
            return True
        return False
choice=input('Do you want to check whether it is a number or name? ')

if (choice=='number'):
    user_input=input("Enter input: ")
    results= palindrome(user_input)
    if (results):
        print(str(user_input),"is a palindrome")
    else:
        print(str(user_input),"is not a palindrome")
else:
    user_input=input("Enter input: ")
    results=palindrome(user_input)
    if (results):
         print(user_input,"is a palindrome")
    else:
        print(user_input,"is not a palindrome")



