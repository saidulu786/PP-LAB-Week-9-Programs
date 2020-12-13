class Employee:
    count = 0
    def __init__(self, name, des, salary):
        self.name = name
        self.des = des
        self.salary = salary
        Employee.count = Employee.count + 1
    
    def displayCount(self):
        print("The number of Employess in the organization are: ", self.count)
        
    def displayEmp(self):
        print ("Name of Employee is: ", self.name)
        print ("Designation of Employee: ", self.des)
        print ("Salary of Employee: ", self.salary)
        
e1 = Employee ("Mahesh", "Manager", 20000)
e2 = Employee ("Rahul", "Team Leader", 30000)

e1.displayCount()

print("Employee Details is:")

e1.displayEmp()
e2.displayEmp()