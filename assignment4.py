#Write a program to withdraw :ksh25000 if acc is between 100,000-200,0000, 30% if it is betweeen 500,000 & 1M and above 1M DEDUCT 18000
acc_amt = float(input("Enter your account's amount: "))
if acc_amt>=100000 and acc_amt<=200000:
    new_acc_amt= acc_amt-25000
    print(f"Your new account balance is {new_acc_amt} due to sh. 25000 deductions done.")
elif acc_amt>=500000 and acc_amt<1000000:
    new_acc_amt=acc_amt-(0.3*acc_amt)
    print(f"Your new account balance is {new_acc_amt} due to 30% deductions done.")
elif acc_amt>=1000000:
    new_acc_amt=acc_amt-(0.5*acc_amt)
    print(f"Your new account balance is {new_acc_amt} due to 50% deductions done.")
else:
    print("No deductions done")

#list of vehicles witn the following : BMW,Audi,Toyota,Mercedes,Jeep. Uaing if statement find a Jeep in the list and convert into uppercase
