class Engine:
    a=10
    def __init__(self):
        self.b=20
        print("Engine Constructor..")
    
class Car:
    def __init__(self):
        self.engine=Engine()
        
    def f1(self):
        print(self.engine.a)
        print(self.engine.b)

c=Car()
c.f1()
    