#Write a program to check if a number is divisible by 5 or 7
#and checks if both condtions if true then displays true, or checks if one of the conditions is true then displays true
from unicodedata import name

num=int(input("Enter number:"))
if (num%5==0) and (num%7==0):
   print(num,"is divisible by 5 and 7")
else:
   print(num,"isn't divisible by 5 and 7 ")

