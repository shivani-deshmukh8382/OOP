class P:
    i=20
    def __init__(self):
        print("Perent Constructor")
        self.a=10
    
class C(P):
    def __init__(self):
        print("Child Constructor")
        self.b=50
        
c=C()#when we create child class object then only child class constructor
     #will be called ,parent class construcot will not executed.
print(c.b,c.i)     #by using child class object reference we can not 
               #access parent class instance variable but we can access 
               # static variable .
p=P()
print(p.a,P.i)#instance var can be accessed by using object ref but static 
                #var can be accessed by using both classname and object ref 
                # var.we can not acced local variable outside the class or 
                # outside of method

             