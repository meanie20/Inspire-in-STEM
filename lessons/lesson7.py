#!/usr/bin/python

#LOOPS
################################################################################
#   Name: Evelyn Wangui
#   Date: 23-05-2022
###############################################################################
#FOR LOOP
#for num in range (0,10):
    #print(num)

#printing a table of number and its square
print("Number\t\tSquares")
print("-----------------------")
for num in range (0,10):
  print(num,'\t\t',num**2)

#printing a list of squares
#squares =[]
#for numbers in range (0,10):
   # square=numbers**2
    #squares.append(square)
#print(squares)

#printing a list of cubes
#cubes =[]
#for numbers in range (0,10):
    #cube=numbers**3
    #cubes.append(cube)
#print(cubes)

#printing a list of squares
#sum =0
#for numbers in range (0,100):
    #sum=sum+numbers
#print(sum)

#print a diamond of stars
#print a pyramid of stars


#IF AND IF...ELSE STATEMENTS
age= 25
if age >= 18:
  print("You are allowed to drive")
else:
  print("You are too young to drive")

# Write a program thta get the user input and adds sh 1000 to an account whose age is between 18 and 25
acc_bal=0
age = float(input("Enter your age: "))
if age>=18 and age<=25:
    acc_bal01= acc_bal+1000
    print("Account balance is ",acc_bal01)
else:
    print("Account balance is ",acc_bal)