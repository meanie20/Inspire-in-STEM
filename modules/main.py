
from student import student
from teacher import teacher
import operations

print(operations.add_number(5,6))
print(operations.subtract_number(5,6))
print(operations.multiply_number(5,6))
print(operations.divide_number(30,6))

student_001=student('evelyn','Swimming',str(2002))
student_001.greetstudent()

teacher_001= teacher(str(1523),'Literature',str(50000))
teacher_001.get_tsc_no()