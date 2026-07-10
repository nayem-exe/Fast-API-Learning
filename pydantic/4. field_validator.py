from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    name: str
    age: int
    weight: float
    email: EmailStr
    profile_url: AnyUrl
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name', mode='after')
    @classmethod
    def transformation_name(cls, value):
        return value.upper()

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')

def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.profile_url)
    print(patient.allergies)
    print('Updated')

patient_info = {'name':'Nayem','age':'30','weight': 84.2, 'email': 'nayemsb11@hdfc.com', 'profile_url':'https://www.linkedin.com/feed/','married':False, 'allergies':['pollen','dust'], 'contact_details': {'email':'nayemsb12@gmail.com', 'phone':'2424234'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)