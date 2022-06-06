#!/usr/bin/python

#MODULES
################################################################################
#   Name: Evelyn Wangui
#   Date: 06-06-2022
###############################################################################
class teacher():
    def __init__(self, tsc_no,subjects,salary):
        self.tsc_no = tsc_no
        self.subjects = subjects
        self.salary = salary
    def get_tsc_no(self):
        print("This is the TSC_number",self.tsc_no)
        return self.tsc_no