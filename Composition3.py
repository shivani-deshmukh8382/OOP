class X:
    a=10 #this is static variable accessed by cls name of object ref and if 
            #we want it to print then by using self keyword
    def __init__(self):
        self.b=20 #instance var
    def m1(self):
        print("m1 method in X class ")
    
class Y:
    c=30    #this is static variable accessed by cls name of object ref and if 
            #we want it to print then by using self keyword
    def __init__(self):
        self.d=40 # this is instance variable accesed by using object class ref
    def m2(self):
        print("m2 method in Y class ")
        
    def m3(self):
        x1=X()
        print(x1.a)
        print(x1.b)
        x1.m1()
        print(self.c)
        print(self.d)
        self.m2()
        print('m3 method in y class')
y =Y()
y.m3()
print(Y.c,y.c,y.d)