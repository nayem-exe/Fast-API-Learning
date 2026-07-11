from pydantic import BaseModel, EmailStr,AnyUrl, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    height: float
    email: EmailStr
    profile_url: AnyUrl
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height ** 2),2)
        return bmi



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
    print('BMI', patient.bmi)
    print('Updated')

patient_info = {'name':'Nayem','age':'30','weight': 84.2, 'height': 1.72, 'email': 'nayemsb11@hdfc.com', 'profile_url':'https://www.linkedin.com/feed/','married':False, 'allergies':['pollen','dust'], 'contact_details': {'email':'nayemsb12@gmail.com', 'phone':'2424234'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)