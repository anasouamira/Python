# class variables = Shared among all instances of a class 
#                  Defined outside the constructor 
#                  Allow you to share data among all objects created from that class 



class Employee:
    # Class variable
    company_name = "TechCorp"
    num_company = 0
    
    def __init__(self, name, age):
        # Instance variables
        Employee.num_company += 1
        
        self.id = Employee.num_company
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Employee Name: {self.name}, Age: {self.age}, Company: {Employee.company_name} , id of company {self.id}")

# Create instances of the Employee class
employee1 = Employee("Alice", 28)
employee2 = Employee("Bob", 32)

# Accessing class variable
print(Employee.company_name)   # Output: TechCorp
print(employee1.company_name)  # Output: TechCorp
print(employee2.company_name)  # Output: TechCorp
print(Employee.num_company)    # Output: 2

# Modifying the class variable
Employee.company_name = "InnovateTech"

# Check the updated class variable for all instances
print(employee1.company_name)  # Output: InnovateTech
print(employee2.company_name)  # Output: InnovateTech

# Calling methods that use the class variable
employee1.display_info()  # Output: Employee Name: Alice, Age: 28, Company: InnovateTech
employee2.display_info()  # Output: Employee Name: Bob, Age: 32, Company: InnovateTech

# Overriding the class variable for one instance
employee1.company_name = "StartUpCo"

print(employee1.company_name)  # Output: StartUpCo
print(employee2.company_name)  # Output: InnovateTech
print(Employee.company_name)   # Output: InnovateTech

