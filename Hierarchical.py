print("One parent class and multiple child class")
class Parent:
    def __init__(self):
        print("Parent class constructor")
        
    def add(self,a,b):
        print(a+b)
        
class Child1(Parent):
    def __init__(self):
            print("Child1 class constructor")
            
class Child2(Parent):
    def __init__(self):
            print("Child2 class constructor")
c2=Child2()
c1=Child1()
c1.add(9,2)
c2.add(2,5)