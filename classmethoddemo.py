class ClassMethodDemo:
    institute = "" #class variable
    def addStudent(self, enrollmentNo, name, course):
        self.enrollmentNo = enrollmentNo
        self.name = name
        self.course = course

    def StudentInfo(self):
        print("Student Information: ",self.enrollmentNo,":",self.name,":",self.course,":",self.institute)

    @classmethod
    def setInstituteName(cls):
        cls.institute = "ITVedant ghvtyvtyvyv"


student1 = ClassMethodDemo()
student1.addStudent(12345,"Ayush","C.Tech")
student1.StudentInfo()
ClassMethodDemo.setInstituteName()
student1.StudentInfo()