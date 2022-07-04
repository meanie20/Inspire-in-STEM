#!/usr/bin/python

#Dictionaries
################################################################################
#   Name: Evelyn Wangui
#   Date: 23-05-2022
###############################################################################
#A dictionary is a collection of key value
#syntax: dict= ("key"): value


vehicle ={"type":"toyota","plate_number":"SZX521"}
person={"name":"Jane Doe","phone_number":"0789456321","address":"152 NY avenue","gender":"female"}

#accessing values
#print(vehicle["type"])
#print(vehicle["plate_number"])
#print(person["name"]) 
#print('{} {}'.format(person['name'], person['address']))
#print(type(person["gender"]))   // prints the data type of the value whose key is selected
#print(type(person["phone_number"]))

#adding values
person["age"]="20"
person["fav_color"]="green"
#print(person)
#print(f'{person["name"]} {person["age"]} {person["fav_color"]}')

#deleting items in the dictionary
del person["phone_number"]
#print(person)

#looping over dictionaries
#for key, value in person.items():
    
    #print(f'("value")("key")')
    #print(person)
    #break;
#print colors using a loop in uppercase
colors= {"color": "red"}
for color in colors:
    while colors=="red":
        print(colors)
        break;



