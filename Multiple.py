class Parent1:
    def __init__(self):
        self.a=10
        print("Parent1 constructor")
        
class Parent2:
    def __init__(self):
        self.a=20
        print("Parent2 constructor")
        
class Child(Parent1,Parent2):
    pass
c=Child()
print(c.a)