#Half pyramid of stars using a nested for loop
rows=int(input("Enter number of rows: "))
for i in range (0,rows):
    for j in range(0,i+1):
        print('*', end="") #Changing * into numbers or letters
    print("\r")

#half pyramid of numbers that repe
#rows=int(input("Enter number of rows: "))
#for i in range (0,rows):
    #for j in range(0,i+1):
       # print('*', end="")
    #print("\r")

#pyramid of stars
    #rows=int(input("Enter number of rows: "))
#k=0
#for i in range (0,rows):    #for j in range((0,i+1)):
        #print(end=" ")
    #while k!=(2*1-1):
     #print('*', end=" ")
     #k+=1

userInput=int(input("Please enter the amount of rows:"))
row=""
count =1
spacing =0
star=0
u=0
while(count <=userInput):
    spacing =spacing +count 
    while(spacing<userInput):
        row+=" "
        spacing +=1
    star=count +u
    while(star>0):
        row+="*"
        star-=1
    count +=1
    spacing=0
    u+=1
    print(row)
    row*=-1

userInput = int(input("Please enter the amount of rows: "))

row = 0
while(row < userInput):
    row += 1
    spaces = userInput - row

    spaces_counter = 0
    while(spaces_counter < spaces):
        print(" ", end='')
        spaces_counter += 1

    num_stars = 2*row-1
    while(num_stars > 0):
        print("*", end='')
        num_stars -= 1

    print()