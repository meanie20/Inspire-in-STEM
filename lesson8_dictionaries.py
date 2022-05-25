#!/usr/bin/python

#Dictionaries
################################################################################
#   Name: Evelyn Wangui
#   Date: 23-05-2022
###############################################################################
#A dictionary is a collection of key value
#syntax: dict= ("key"): value
#Intialisng dictionaries
student={"name":"Jack Sparrow","age":"100"}
book={"author":"Collen Hoover","title":"Verity"}



#Accessing values in the dictionary
print(student["name"])

#Adding pairs
student["Gender"]="Male"
student["Adm_no"]="78965"
print(student)

#intialising an empty dictionary
student_01= {}
student_01["fav_food"]="Pilau"
student_01["home_city"]="Nairobi"
student_01["fav_song"]="Last last by burna boy"
print(student_01)

#modifying the values
student["name"]="Timmy Turner"
student["age"]="150"
print(student)

#removing values
del student["name"]
print(student)





























