from pydantic import BaseModel
from typing import List,Dict
class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')

def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('Updated')

patient_info = {'name':'Nayem','age':'30','weight': 84.2, 'married':False, 'allergies':['pollen','dust'], 'contact_details': {'email':'nayemsb12@gmail.com', 'phone':'2424234'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)