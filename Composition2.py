class Car:
    def __init__(self,cname,model,color):
        self.cname=cname
        self.model=model
        self.color=color
        
    def getcarinfo(self):
        print("Car name :{}, model :{}, color:{}".format(self.cname,self.model,self.color))
    
class Employee:
    def __init__(self,name,age,car):
        self.name=name
        self.age=age
        self.car=car
        
    def getdetail(self):
        print("Name of the employee : ",self.name)
        print("age : ",self.age)
        self.car.getcarinfo()
c=Car('maruti suzuki','A47',1000000)
e = Employee('chetan',35,c)
e.getdetail()     
        