class student(object):
    def __init__(self,marks):
        self.name="Pratha"
        self.age=14
        self.grade=9
        self.marks=marks
    def printmarks(self):
        print("total marks"+str(self.grade))
        print("total marks reiceved"+str(self.marks))
student1=student("600")
student1.printmarks()
student2=student("545")
student2.printmarks()