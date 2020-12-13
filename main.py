class students:
    count = 0
    def __init__(self, name):
        self.name = name
        self.marks = []
        students.count = students.count + 1
        
    def enterMarks(self):
        for i in range(3):
            m = int(input("Enter the marks of %s in %d subject: "%(self.name, i+1)))
            self.marks.append(m)
            
    def display(self):
        print (self.name, "got ", self.marks)
s1 = students("meera")
s1.enterMarks()
s2 = students("ram")
s2.enterMarks()
s1.display()
s2.display()