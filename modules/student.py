#!/usr/bin/python

#MODULES
################################################################################
#   Name: Evelyn Wangui
#   Date: 06-06-2022
###############################################################################
class student():
    def __init__(self,name,hobby,year_of_birth):
        self.name = name
        self.hobby = hobby
        self.year_of_birth = year_of_birth
    def greetstudent(self):
        print("Hello from",self.name.title())
