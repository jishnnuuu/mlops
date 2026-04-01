# initiate a class
class employee:
    
    # creating a static variable
    __user_id = 2025707
    
    # special method/ magic method/ dunder method - constructor
    def __init__(self):
        self.course = "MT"
        self.id = employee.__user_id
        employee.__user_id += 1
        #hide salary
        self.__salary = 160000 
        self.designation = "ML Engineer"
    
    def travel(self, destination):
        print(f"Employee is now travelling to {destination}")
    
    # in static methods there is no need of giving self as argument unlike other methods
    @staticmethod
    def get_id():
        return employee.__user_id
    
    @staticmethod
    def set_id(new_id):
        employee.__user_id = new_id
    
    # getter method
    def get_name(self):
        return self.__salary, self.designation
    
    # setter method
    def set_name(self, value, role):
        self.__salary = value
        self.designation = role
    
    def get_fullId(self):
        return self.course + str(self.id)

# create an obj/ instance of the class
jeeznu = employee()

print(f"Jeeznu salary: {jeeznu._employee__salary}")
jeeznu.travel("GOA")

# can create attribute outside the class too    
jeeznu.name = "Jishnu Satwik"
print(jeeznu.name)

print(jeeznu.get_name())
print("--updating role and salary using getter and setter methods--")
jeeznu.set_name(200000, "Data Scientist")
print(jeeznu.get_name())
print(jeeznu.get_fullId())

print("\n")

satwik = employee()
satwik.get_id()
satwik.set_id(2004288)
print(satwik.get_fullId())