#!/usr/bin/python

#FILE OPERATIONS
################################################################################
#   Name: Evelyn Wangui
#   Date: 06-06-2022
###############################################################################

#f = open("lesson.txt",'r') #read-only
#f = open("lesson.txt",'w') #write-only
#f = open("lesson1.txt",'x') #opens file for exclusive; create a new file
#f = open("lesson.txt",'a') #opens a file for appending
#f = open("lesson.txt",'t') #opens file in text mode
#f = open("lesson.txt",'b') #opens file in binary mode
#opens a file for reading and writing

f= open("lesson.txt") #default opening a text file
print(f.read())
f.close()

#f= open("lesson1.txt","x") #creates a new file

f= open("lesson1.txt")
with open("lesson1.txt","w",encoding = "UTF-8")as f:
    f.write("This is my new file\n")
    f.write("Consider a module to be the same as a code library.\nA file containing a set of functions you want to include in your application")
#print(f.read())
#f.close()

f= open("lesson1.txt") 
print(f.readline()) #reads one line









