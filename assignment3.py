# Write a program that get the user input and adds sh 1000 to an account whose age is between 18 and 25
acc_bal=0
age = float(input("Enter your age: "))
if age>=18 and age<=25:
    acc_bal01= acc_bal+1000
    print("Account balance is ",acc_bal01)
else:
    print("Account balance is ",acc_bal)
