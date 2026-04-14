from pydantic import BaseModel, EmailStr, AnyUrl, field_validator, Field, model_validator
from typing import List, Dict, Optional, Annotated
from typing_extensions import Self

# usual non-data validation method
def patient_details(name, age):
    print(f"Name : {name}, Age : {age}")

class ContactDetails(BaseModel):
    address : str
    phone : Annotated[Optional[int], Field(default=None, title='Phone Number',description="Enter phone number")]

# pydantic data validation
class Patient(BaseModel):
    name : Annotated[str, Field(max_length=50,
                                title= 'Name of the Patient',
                                description='Give the name of the patient in less than 50 chars',
                                examples= ['Jishnu', 'Satwik'])] # restricting the length to 50
    age : int = Field(ge=18, le=80) # restricting the age group to be with in (18-80)
    # using EmailStr built in pydantic data validation for validation email addresses
    email: EmailStr
    weight : Annotated[float, Field(gt=0, strict=True)] # weight is greater than 0
    # we can keep few variables optional also give a default value for it
    married : Annotated[Optional[bool], Field(default = None, description='Is the Patient Married or not?')]
    allergies : List[str]
    # rather Dict[str, str] we give ContactDetails model
    contact_details: Annotated[ContactDetails, Field(description="Fill Contact Details", title="Contact Details")]
    linkedInURL : AnyUrl
    
    
    # Capitalizing name
    @field_validator('name')
    @classmethod
    def transform_name(cls, name: str) -> str:
        return name.upper()
    
    # age to be between 20 and 60 using field_validator (this can be done using Field also)
    """
    try with mode = 'before' it will give you error because pydantic coverts '21' to 21 but 'before' mode
    means before the pydantic operation, so it will still string, so the error comes, default the value of
    mode = 'after'
    """
    @field_validator('age', mode='after')
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
    
    @model_validator(mode='after')
    def validate_emergency(cls, self) -> Self:
        if self.age > 60 and  self.contact_details.phone is None:
            raise ValueError('Patients of age above 60 need to have contact_details filled')
        return self
    
    

patient_info = {
    'name' : 'ram',
    'age'  : '62',
    # if instead of 21 though you give '21' internally pydantic converts into integer given age:int
    'email' : 'ram@gmail.com',
    # ram@gmail.com works, but ramgmail.com will give validation error as we used in built EmailStr for email validation
    'weight' : 70,
    # same way weight is converted to float though integer is passes given weight:float
    # 'married' : True,
    'allergies' : ['pollen', 'dust'],
    # in this case i want contact_details dictionary to have str for address, and int for phone, so we create a specific model for it
    'contact_details' : {
        'address' : 'Hyderabad, India',
        'phone' : 32423592
    },
    'linkedInURL' : 'https://linkedin.com/ramgopalverma'
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