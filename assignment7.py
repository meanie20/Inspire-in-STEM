#program that writes number in reverse like 100 should be 001
#using recursion
print("A program that reverses numbers.")
num = int(input("Enter the number: "))  
revr_num = 0    # initial value is 0. It will hold the reversed number  
def rev_number(num):  
    global revr_num   # We can use it out of the function  
    if (num > 0):  
        Reminder = num % 10  
        revr_num = (revr_num * 10) + Reminder  
        rev_number(num // 10)  
    return revr_num  
  
reverse_num=rev_number(num)
print("The reverse of",num,"is",reverse_num)

#using while loop
number= int(input("Enter any Number: "))    
Reverse = 0    
while(number > 0):    
    Reminder = number %10    
    Reverse = (Reverse *10) + Reminder    
    number = number //10  
print("Reverse is",Reverse)

#using for loop
num01=int(input("Enter number:"))
rev=0
for rev in range(num01):
    rem=(num01 % 10)
    rev=(rev * 10) + rem
    num01= num01 // 10
print(" The reverse is",rev)





