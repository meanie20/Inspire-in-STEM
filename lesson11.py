#function parameters
from cmath import sqrt
import math
def say_hello():
    print("Hello from JKUAT")

    x = 7
    y = 8 
    z = x+y
    print(z) 
say_hello()

def bark():
    print("Dogs bark woof woof woof")
    print("Cows moos mooo mooo mooo ")
    print("Ducks quack quack quack quack")
bark()

#function parameters
def add_numbers(x,y):
    sum_nums= x + y
    print("the sum of numbers is ",sum_nums )
add_numbers(68,89)
add_numbers(80,20)
add_numbers(60,90)

def multipy_numbers (x,y):
    prod_nums= x*y
    print("The product of numbers is ",prod_nums)
multipy_numbers(7,4)
multipy_numbers(67,34)

#Quadratic equation

a=int((input("Enter the co-efficient of the first term: ")))
b=int((input("Enter the co-efficient of the second term: ")))
c=int((input("Enter the constant: ")))
disc=(sqrt((b**2) - (4*a*c)))
x=(-b+disc)/(2*a)
y=(-b-disc)/(2*a)
print("The roots of the equation is ",x,y)



