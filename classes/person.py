#!/usr/bin/python

#Classes
################################################################################
#   Name: Evelyn Wangui
#   Date: 02-06-2022
###############################################################################
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
   
    # Sample Method 
    def say_hi(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')
   
person_001 = Person('Jack Sparrow',str(16))
person_001.say_hi()
person_002 = Person('Turner',str(22))
person_002.say_hi()