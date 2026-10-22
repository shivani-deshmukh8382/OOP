class Parent:
    def __init__(self):
        print("Parent class constructor")
    
    def m1(self):
        print("Parent class m1()")
        
    @classmethod
    def clss(cls):
        print("class method of Parent class ")
        
class Child(Parent):
    def __init__(self):
        print("Child class constructor")
      
    def m2(self):
        print("Child class m2()")
    
    @staticmethod    
    def test():
        print("Static method of child class")  
        
class CChild(Child):
    def __init__(self):
        print("CChild class constructor")
        
    def m3(self):
        print("CChild class m3()")
        
print("Multilevel inheritance")
cc=CChild()
cc.m3()
cc.m2()
cc.m1()#by using child cls ref var we can call all 
        #instance methods present in parent class 
cc.test()#by using child cls ref we can call staticmethod of parent cls
cc.clss()#by using child cls ref we can call classmethod of parent cls
CChild.clss()
CChild.test() # classmethod and staticmethod we can call using child class
                #name also