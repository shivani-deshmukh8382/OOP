class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    
    def display(self):
        print("Name : ",self.name)
        print("Gender : ",self.gender)
    
class Student(Person):
    def __init__(self,id,name, gender,marks):
        super().__init__(name, gender)  #By using super() we can call constructor of parent class
        self.id=id
        self.marks=marks
        
    def display(self):
        print("Id : ",self.id)
        super().display()      #By using super() we can call constructor of
                                #parent class and parent class instance method 
        print("marks : ",self.marks)
    
stud=Student(12,'shivani','female',89)
stud.display()
