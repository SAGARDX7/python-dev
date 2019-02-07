class employee:
    tot_salary=0
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        employee.tot_salary=employee.tot_salary+salary
    def display_details(self):
        print("name=",self.name)
        print("age=",self.age)
        print("salary=",self.salary)
    def display_sum():
        print(employee.tot_salary)
e1=employee("a",23,2000)
e2=employee("b",34,3500)
e3=employee("c",30,2800)
e1.display_details()
e2.display_details()
e3.display_details()
employee.display_sum()
print("max salary among all is:",max(e1.salary,e2.salary,e3.salary))
