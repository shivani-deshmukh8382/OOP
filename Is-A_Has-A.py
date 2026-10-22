class Car:
    def __init__(self,cname,model,color):
        self.cname = cname 
        self.model = model
        self.color = color
    
    def m1(self):
        print("Car class m1 method") 
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def m2(self):
        print("Person class m2 method")
        
class Employee(person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
        self.car = car
        
    def m3(self):
        car.m1()
        self.m2()
        print("Employee class inherited from Person class and uses (Has-A) relation with Car ")
        
car = Car('maruti suzuki','AK24',3000000)
employee = Employee('shivani',26,78865,50000,car)
employee.m3()
