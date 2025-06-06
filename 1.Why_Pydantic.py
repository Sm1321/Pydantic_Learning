from pydantic import BaseModel
from typing import List,Dict

class Patient(BaseModel):
    name :str
    age : int
    weight : float
    # height: float
    married: bool
    allergies: List[str]  #we should not use this list command 
    contact_details: Dict[str,str] #we should this not use  dict command 

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print('Inserted ')


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print('Updated')

##################################################
patient_info = {
    'name': 'Ram',
    'age': 30,  
    'weight': 75.2,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'email': 'abc@gmail.com',
        'phone': '1234567879'  
    }
}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)

# patient_info = {'name':'Ram','age':'thirty'}
# # patient_info = {'name':'Krishna','age':30} 
# patient1 = Patient(**patient_info)
# insert_patient_data(patient1)


















# def insert_paitient_data(name : str,age : int):
#     if type(name) == str and type(age) == int:
#         if age < 0:
#             raise ValueError('Age can\'t be negative')    
#         print(name)
#         print(age)
#         print("Inserted into the Database")
#     else:
#         raise TypeError('Incorrect Data type')    


# def update_paitient_data(name : str,age : int):
#     if type(name) == str and type(age) == int:    
#         print(name)
#         print(age)
#         print("Inserted into the Database")
#     else:
#         raise TypeError('Incorrect Data type')    
    
# #Insert the deatils
# insert_paitient_data('Ram',10) 
# insert_paitient_data('Raj','30')     
