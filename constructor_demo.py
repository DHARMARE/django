class Person:
    def __init__(self): #default constructor
        self.name = "Ayush Dharmare"
        self.age = 30

    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

    def show(self):
        print("Person Information [Name : ",self.name,"Age: ", self.age,"]" )

    def display(self):
         print("Person Information [Name : ",self.name,",Age: ,", self.age,",Email: ",self.email,"]" )

# person1 = Person()
# person1.show()

person2 = Person("Ayush",30,"ayush@gmail.com")
person2.display()