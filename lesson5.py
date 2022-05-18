#String Methods
name="Jack Sparrow"
age= 100
user_name=" Cpt Sparrow "
#person = "I am " +str(name)+ " and I am " +str(age)+ " years old."
#print(person)

#FORMAT METHOD
#print("My name is {} and I am {} years old".format(name,age))
print(f"My name is {name} \nI am {age} years old")

#STRIP
#.lstrip strips space from the left &.rstrip is from thr right
print(user_name.strip())

# using triple or double quotes for print
msg="Hello, world! Open the page in your browser of choice to see your Bootstrapped page. Now you can start building with Bootstrap by creating your own layout,"
print(msg)
txt='''This on-page optimization tool analyzes your website or URL address and gives you an overview of the SEO Optimization factors. You can add up to five keywords, which the algorithm will search for and tell you how often each word is used'''
print(txt)

#Udint slice method
city= "Nairobi"
print(city[:3])
print(city[:-2])

#CHANGING CASE
s_name="KENNEDY"
print(s_name.lower())
s_name="kennedy"
print(s_name.upper())

#CONVERSION
num= 20
print(float(num))
x= 12.0000
print(str(x))
x= 240.0000
print(int(x))

f_name= "Elssie"
s_name= " Wanjiru "
full_name= f_name + s_name
print(full_name)

#replace
print(full_name.replace('e','i') )

#split a statement
txt= "Hello Ryle Kincaid.How are you?"
print(txt.split())

#finding the length of a string
txt= "Hello Ryle Kincaid.How are you?"
print(txt.length())



