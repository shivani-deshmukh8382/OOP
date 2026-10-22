class Parent:
    def __init__(self):
        print("Parent constructor")
        
    def test1(self):
        print("Instance method")
        
    @staticmethod
    def test2():
        print("static mathod")
        
    @classmethod
    def test3(cls):
        print("class method")
        
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Chile class Constructor")
        
child = Child()
child.test1()   #Using super() we can call cmallmethos staticmethod 
             #and instancemethod of parent class using child class
child.test2()
child.test3()