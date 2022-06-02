class Employee:
    def __init__(self, name, emp_ID, salary_amount):
        self.name = name
        self.emp_ID = emp_ID
        self.salary_amount = salary_amount
    def att(self):
        print(f"I am {self.name} , my employee ID is {self.emp_ID} and I earn {self.salary_amount} Kenyan Shillings per year.")
Emp_001= Employee('Homer Simpson', str(852693), str(144000))
Emp_001.att()