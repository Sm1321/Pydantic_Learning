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

address_dict = {'city': 'Hyderabad', 'state': 'Telangana', 'pin': '500043'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Ram', 'gender': 'male', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)
print(patient1)
print(patient1.name)
print(patient1.age)
print(patient1.address)

temp = patient1.model_dump()

print(type(temp))























# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed