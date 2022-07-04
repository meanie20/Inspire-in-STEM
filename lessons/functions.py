
#syntax of a function; (function definition)
   #  def nameof functions:
     #statements
#function parameters
# blocks of code which execute together
from cmath import sqrt
import math
from socket import MsgFlag
from venv import create
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
#a=int((input("Enter the co-efficient of the first term: ")))
#b=int((input("Enter the co-efficient of the second term: ")))
#c=int((input("Enter the constant: ")))
# def find_roots(a,b,c):
    #disc=(sqrt((b**2) - (4*a*c)))
   
    #x=(-b+disc)/(2*a)
    #y=(-b-disc)/(2*a)
    #print("The roots of the equation is ",x,y)
#find_roots(1,6,9)

#default function parameters
def print_name(name="Elssie Wamjiru"):
    print(name)
print_name("Joseph")

#return from a function
def get_sum(num1,num2):
    sum_nums =num1+num2
    return sum_nums
print(get_sum(7,12))

#Power of numbers
def get_power(num,power):
    power_num= num**power
    return power_num
print(get_power(6,4))

#
def print_fullname(fname,sname):
    fullname= fname +" " + sname
    return fullname
print("My name is",print_fullname('Edwin', 'Kiburi'))

#Returning a dicitonary from a fucntion
def create_full_name(fname,sname):
    person={'first name': fname, 'second name':sname}
    return person
student = create_full_name('Jane','Doe')
print(student)

#Parsing a list in a function
def greet_friends(names): #names is a list
    for name in names:
        msg= "Hello"+" "+name.title()+"!"
        print(msg)
friends=['Wanjiru Muchai','Gathoni Mugo','Gerry Kamau','Wamaitha Murigi']
print(greet_friends(friends))





