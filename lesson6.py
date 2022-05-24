#LISTS
Cities= ['Nairobi', 'Nakuru','Mombasa','Kisumu']
print(Cities[0])

fruits=["Mango","Pineapple","Banana"]
fruits.append=("Guava")
print(fruits)

Motorcycle_owner="Harley Marshall"
plate_number=['H2564','S1547','F7895']
Motorcycle=['Honda','Suzuki','Yamaha']
#print(Motorcycle[2])
#print(Motorcycle[0])
print(Motorcycle[-1])  #reads the list from the end

#how to change an item in a list
Motorcycle[2]= "Ferrari"
print(Motorcycle)

#how to append a list
#Motorcycle.append('Bugatti')
#plate_number.append('B2987')
#print(Motorcycle)
#print(plate_number)

#when the below code is uncommented it intefers with code 32-35 since it deletes the indices used
#how to delete an item from a list
#del Motorcycle[0]
#print(Motorcycle)

#pop_motorcycle=Motorcycle.pop()
#print(pop_motorcycle)

#Motorcycle.remove('Suzuki')
#print(Motorcycle)

print("My name is "+str(Motorcycle_owner)+" and I own a "+str(Motorcycle[0])+" plate number "+str(plate_number[0]))
print("My name is {} and I own a {} {}".format(Motorcycle_owner,Motorcycle[1],plate_number[1]))
print(f"My name is {Motorcycle_owner} and I own a {Motorcycle[0]} plate number {plate_number[0]}")
print(f"My name is {Motorcycle_owner} and I own a {Motorcycle[0]} {plate_number[0]}")






