#iterating through a dictionary using keys directly
colors= {"color": "red"}
#for color in colors:
    #print(colors[color].upper())
    #break;

colors= {"color": "red"}
for color in colors.values():
        print(color.upper())

colors= {"color": "red"}
for color in colors:
    print(color, '->', colors[color])


#To return values in a dcitionary you can use:
#for color in colors.values():
#for color in colors.keys():
#for color in colors.items(:
# the .values() and .keys() return view objects but .items return both key and value 

colors= {"color": "red"}
for color in colors.items():
  print(color) #x rep the key, y rep the value
  print(type(color))

colors= {"color": "red"}
for key, value in colors.items():
    print(key, ':', value)

colors= {"color": "red"}
for color in colors.keys():
    print(color)

prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for key in list(prices.keys()):
    if key == 'orange':
        del prices[key]
        print(prices)

cars= {
    'year':'1964',
    'brand':'Ford',
    'model':'Mustang'
    }
sorted_cars = {k: cars[k] for k in sorted(cars)}
print(sorted_cars)

cars= {
    'year':'1964',
    'brand':'Ford',
    'model':'Mustang'
    }
sorted_cars = {k: cars[k] for k in sorted(cars)}
for key, value in sorted_cars.items():
    print(key.title(), ':', value)



class dog:
    def att(name,age):
        print(name,age)
    def breed(type):
        print(type)
    att("Fluffy",8)
    breed("German Shepherd")

class Dog:
    def __init__(self, name, breed, gender,age):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.age = age
    
    def say_hi(self):
         print(f'This is {self.name}.It is a {self.breed} {self.gender} and is {self.age} years old.')
Dog_001 = Dog('Fluffy','German Shepherd','male',str(8))
Dog_001.say_hi()
Dog_002 = Dog('Bee','Rotwiler','male',str(6))
Dog_002.say_hi()
Dog_003 = Dog('Spark','Golden Retriever','female',str(3))
Dog_003.say_hi()