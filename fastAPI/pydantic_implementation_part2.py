from pydantic import BaseModel, EmailStr, AnyUrl, field_validator, Field
from typing import List, Dict, Optional

# usual non-data validation method
def patient_details(name, age):
    print(f"Name : {name}, Age : {age}")

class ContactDetails(BaseModel):
    address : str
    phone : int

# pydantic data validation
class Patient(BaseModel):
    name : str = Field(max_length=50) # restricting the length to 50
    age : int = Field(ge=18, le=80) # restricting the age group to be with in (18-80)
    # using EmailStr built in pydantic data validation for validation email addresses
    email: EmailStr
    weight : float = Field(gt=0) # weight is greater than 0
    # we can keep few variables optional also and give a default value for it
    married : Optional[bool] = None
    allergies : List[str]
    # rather Dict[str, str] we give ContactDetails model
    contact_details: ContactDetails
    linkedInURL : AnyUrl
    
    # age to be between 20 and 60 using field_validator
    @field_validator('age')
    @classmethod
    def check_age(cls, v : int) -> int:
        if v < 18 or v > 80:
            raise ValueError('age is not in bound')
        return v
    
    
    # our linkedinURL must have linkedin.com, so we are using field_validator
    @field_validator('linkedInURL')
    @classmethod
    def check_linkedIn_domain(cls, v: AnyUrl) -> AnyUrl:
        # v.host extracts the domain (eg. 'linkedin.com)
        if not v.host or 'linkedin.com' not in v.host:
            raise ValueError('The URL must be a valid linkedin.com profile')
        return v

patient_info = {
    'name' : 'ram',
    'age'  : 32,
    # if instead of 21 you give '21' internally pydantic converts into integer given age:int
    'email' : 'ram@gmail.com',
    # ram@gmail.com works, but ramgmail.com will give validation error as we used in built EmailStr for email validation
    'weight' : 70 ,
    # same way weight is converted to float though integer is passes given weight:float
    # 'married' : True,
    'allergies' : ['pollen', 'dust'],
    # in this case i want contact_details dictionary to have str for address, and int for phone, so we create a specific model for it
    'contact_details' : {
        'address' : 'Hyderabad, India',
        'phone' : 32423592
    },
    'linkedInURL' : 'https:linkedin.com/ramgopalverma'
}

patient1 = Patient(**patient_info)
## print(patient1.age)

# pydantic object is passed onto the function
def patient_details_pyd(patient: Patient):
    print(f"Name : {patient.name}, Age : {patient.age}, weight: {patient.weight}")
    print(f"Email address : {patient.email}")
    print(f"Marital Status: {patient.married}")
    print(f"Allergies : {patient.allergies}")
    print(f"Contact Details : {patient.contact_details}")
    print(f"LinkedIn Profile : {patient.linkedInURL}")

patient_details_pyd(patient1)