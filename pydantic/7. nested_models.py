from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address


address_dict = {'city': 'Dhaka', 'state':'Dhaka', 'pin': '112233'}

address_1 = Address(**address_dict)

patient_dict = {'name':'Nayem', 'gender':'male', 'age': 25, 'address': address_1}

patient_1 = Patient(**patient_dict)

print(patient_1)
print(patient_1.name)
print(patient_1.address.city)


temp = patient_1.model_dump()
print(temp)
print(type(temp))

temp2 = patient_1.model_dump_json()
print(temp2)
print(type(temp2))