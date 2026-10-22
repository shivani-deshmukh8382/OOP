class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def m1(self):
        print("Person class m1 method : ")
        
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno = eno
        self.esal = esal
        
    def work(self):
        print("Employee name :",self.name)
        print("Employee age : ",self.age)
        print("Employee eno : ",self.eno)
        print("Employee salary : ",self.esal)
        
employee = Employee('Raghav',43,eno=67558,esal=5000)
employee.work()
        