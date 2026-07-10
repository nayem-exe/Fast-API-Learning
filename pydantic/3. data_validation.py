from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    name: Annotated[ str, Field(max_length= 50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nayem', 'Nobita'])]
    age: int = Field(gt=0, lt=120)
    weight: Annotated[ float, Field(gt = 0, strict=True) ]
    email: EmailStr
    profile_url: AnyUrl
    married: bool = False
    # allergies: Optional[List[str]] = Field(max_length= 5)
    allergies: Annotated [Optional[List[str]] , Field(max_length= 5, default= None)]
    contact_details: Dict[str, str]

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

patient_info = {'name':'Nayem','age':'30','weight': 84.2, 'email': 'nayemsb11@gmail.com', 'profile_url':'https://www.linkedin.com/feed/','married':False, 'allergies':['pollen','dust'], 'contact_details': {'email':'nayemsb12@gmail.com', 'phone':'2424234'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)