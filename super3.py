class Parent:
    a=10
    def __init__(self):
        print("Parent class constructor")
        self.b=20
    def test1(self):
        print("Parent class Instance method")
            
    @staticmethod
    def test2():
        print("Parent class static mathod")
            
    @classmethod
    def test3(cls):
        print("Parent class class method")
         
class Child(Parent):
    def __init__(self):
        print("Child class constructor")
        super().__init__()
        print(super().a)    #by using super()we can access static method but we can not 
                                #access instance variable.But we can access instanse 
                                # variable using self keyword
        #print(super().b)
        print(self.b)
        print(self.a)   #static variable we can access by using self keyword and super()
        super().test1()
        super().test2()
        super().test3()
        
    def display(self):
        print("Display method in child class ")
        super().__init__()
        super().test1()    #From child class constructor and instance method we can call 
                            #staticmethod,classmethod,instancemethod and constructor using super() 
        super().test2()
        super().test3()
        
    @classmethod
    def clsm(cls):
        print("child class classmethod..........................................")
        super().test2()
        super().test3()#we can call parent class staicmethod and classmethod from 
                            #classmethod of child class
       # super().test1()  we can not call parent class instance methods and 
                    # constructor from class method of child class
        print("_____________________________________________________________________")
        super(Child,cls).test1(cls)   #we can call instance method and constructor 
                                        #of parent class indirectly 
        super(Child,cls).__init__(cls)   
                    
    @staticmethod
    def stsm():
        #super().test1()
        #super().test2()
        #super().test3() from static method of child we can not use super()
        super(Child,c).test1()
        super(Child,c).test2()
        super(Child,c).test3()
        super(Child,c).__init__
        pass
        
c=Child()
print(c.a)
c.display()
c.clsm()
c.stsm()

