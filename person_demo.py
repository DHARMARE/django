# class Person:
#     def set_info(self,pid,pname,page): #self is used to refer to current object
#         self.pid = pid
#         self.pname = pname
#         self.page = page

# person1 = Person() #object
# person1.set_info(1233,"Ayush Dharmare",23)
# print(person1.pid,":",person1.pname,":",person1.page)


class Students:
    def set_stu(self,roll_no,name,course,m1,m2,m3):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

student1 = Students()
student1.set_stu(165,"Ayush Dharmare","C.Tech",12,15,20)
print(student1.roll_no,":",student1.name,":",student1.course,":",student1.m1,":",student1.m2,":",student1.m3,":")