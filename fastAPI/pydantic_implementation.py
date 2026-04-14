from pydantic import BaseModel
from typing import List, Dict, Optional

# usual non-data validation method
def patient_details(name, age):
    print(f"Name : {name}, Age : {age}")

class ContactDetails(BaseModel):
    email : str
    phone : int

# pydantic data validation
class Patient(BaseModel):
    name : str
    age : int
    weight : float
    # we can keep few variables optional also give a default value for it
    married : Optional[bool] = None
    allergies : List[str]
    # rather Dict[str, str] we give ContactDetails model
    contact_details: ContactDetails

patient_info = {
    'name' : 'ram',
    'age'  : 21, 
    # if instead of 21 you give '21' internally pydantic converts into integer given age:int
    'weight' : 70 ,
    # same way weight is converted to float though integer is passes given weight:float
    # 'married' : True,
    'allergies' : ['pollen', 'dust'],
    # in this case i want contact_details dictionary to have str for email, and int for phone, so we create a specific model for it
    'contact_details' : {
        'email' : 'ram@gmail.com',
        'phone' : 32423592
    }
}

patient1 = Patient(**patient_info)
## print(patient1.age)

# pydantic object is passed onto the function
def patient_details_pyd(patient: Patient):
    print(f"Name : {patient.name}, Age : {patient.age}, weight: {patient.weight}")
    print(f"Marital Status: {patient.married}")
    print(f"Allergies : {patient.allergies}")
    print(f"Contact Details : {patient.contact_details}")

patient_details_pyd(patient1)