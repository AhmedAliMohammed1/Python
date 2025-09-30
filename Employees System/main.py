# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getSalary(self):
        return self.salary
    def updateSalary(self, salary):
        self.salary = salary


Employee_list=[]

def ADD_new_employee(name, age, salary):
    employee = Employee(name=name,age= age, salary=salary)
    Employee_list.append(employee)
    print(f"{employee.getName()} has been added")
def List_all_employees():
    if not Employee_list  :
        print("Employee list is empty\n")
        return False
    for employee in Employee_list:
        print(f"Employee Name : {employee.getName()} \n"
              f"Employee Age : {employee.getAge()} \n"
              f"Employee Salary : {employee.getSalary()}\n"
              f"-----------------------------------------")
    return True
def Delete_by_age(age):
    for employee in Employee_list:
        if employee.age == age:
            Employee_list.pop(Employee_list.index(employee))
            return True
    return False

def Update_salary_by_fullname(name,salary):
    for employee in Employee_list:
        if employee.name == name:
            employee.updateSalary(salary)
            print(f"{employee.getName()} has been updated and its salary is {employee.getSalary()}")
            return True
    return False


# Press the green button in the gutter to run the script.
def main():
    while(True):
        print("1) Add a new employee\n")
        print("2) List all employees\n")
        print("3) Delete by age range \n")
        print("4) Update Salary by Full name \n")
        print("5) Exit \n")
        while(True):
            option = int(input())
            if option == 1:
                print(f"Please Enter The Employee Name\n")
                name = str(input())
                print(f"Please Enter The Employee Age\n")
                age = int(input())
                print(f"Please Enter The Employee Salary\n")
                salary = float(input())
                ADD_new_employee(name, age, salary)
                break
            elif option == 2:
                List_all_employees()
                break
            elif option == 3:
                print(f"Please Enter The Employee Age\n")
                age = int(input())
                if(Delete_by_age(age)):
                    print(f"Employee {age} has been deleted")
                    break
                print("Could't find the Employee Age At All")
                break
            elif option == 4:
                print(f"Please Enter The Employee Name\n")
                name = str(input())
                print(f"Please Enter The New Employee Salary\n")
                salary = float(input())
                Update_salary_by_fullname(name,salary)
                break
            elif option == 5:
                return True

            else :
                print("Invalid Option")
                break




main()