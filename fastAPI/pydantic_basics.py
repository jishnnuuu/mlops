from pydantic import BaseModel

# pydantic data validation
class Patient(BaseModel):
    name : str
    age : int
    weight : int

# usual non-data validation method
def patient_details(name, age):
    print(f"Name : {name}, Age : {age}")

patient_info = {
    'name' : 'jishnu',
    'age'  : 21, 
    # if instead of 21 you give '21' internally pydantic converts into integer given age:int
    'weight' : 85
}

patient1 = Patient(**patient_info)
## print(patient1.age)

# pydantic object is passed onto the function
def patient_details_pyd(patient: Patient):
    print(f"Name : {patient.name}, Age : {patient.age}, weight: {patient.weight}")

patient_details_pyd(patient1)