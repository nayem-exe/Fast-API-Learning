from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    email: EmailStr
    profile_url: AnyUrl
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode = 'after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model

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