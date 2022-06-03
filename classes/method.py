#!/usr/bin/python

#Classes
################################################################################
#   Name: Evelyn Wangui
#   Date: 02-06-2022
###############################################################################
#Using a sample method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
   
    #sample method
    def say_hi(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')
   
person_001 = Person('Jack Sparrow',str(16))
person_001.say_hi()
person_002 = Person('Turner',str(22))
person_002.say_hi()

class Dog:
    def __init__(self, name, breed, gender,age):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.age = age
    
    def say_hi(self):
         print(f'This is {self.name}. It is a {self.breed} {self.gender} and is {self.age} years old.')
Dog_001 = Dog('Fluffy','German Shepherd','male',str(8))
Dog_001.say_hi()
Dog_002 = Dog('Bee','Rotwiler','male',str(6))
Dog_002.say_hi()
Dog_003 = Dog('Spark','Golden Retriever','female',str(3))
Dog_003.say_hi()

class Employee:
    def __init__(self, name, emp_ID, salary_amount):
        self.name = name
        self.emp_ID = emp_ID
        self.salary_amount = salary_amount
    def att(self):
        print(f"I am {self.name} , my employee ID is {self.emp_ID} and I earn {self.salary_amount} Kenyan Shillings per year.")
Emp_001= Employee('Homer Simpson', str(852693), str(144000))
Emp_001.att()
