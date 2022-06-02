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