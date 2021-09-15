import sys
import pandas as pd

class Student:

    def __init__(self,first,last):
        self.first=first
        self.last=last

    @property
    def full_name(self):
        return self.first+self.last

    @property
    def email(self):
        return '{}+{}@gmail.com'.format(self.first,self.last)

Student1=Student("Chen","raya")
Student2=Student("Xhang","XI")


print(Student1.first)
print(Student1.full_name)
print(Student1.email)



for num in [1,2,3,4]:
    print(num)


print(sys.executable)
