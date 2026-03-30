# initiate a class
class employee:
    # special method/ magic method/ dunder method - constructor
    def __init__(self):
        print("started executing attributes")
        self.id = "MT2025707"
        self.salary = 160000 
        self.designation = "ML Engineer"
        print("attributes have been initiated")
    
    def travel(self, destination):
        print(f"Employee is now travelling to {destination}")

# create an obj/ instance of the class
jeeznu = employee()

print(f"Jeeznu salary: {jeeznu.salary}")
jeeznu.travel("GOA")

==