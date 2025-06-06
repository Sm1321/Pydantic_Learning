from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional

class Patient(BaseModel):
    name :str = Field(max_length= 120)
    age : int
    email:EmailStr
    linkdin_url: AnyUrl
    weight : float = Field(gt = 0,lt = 120)
    # height: float
    married: bool = False
    allergies: Optional[List[str]]= None  #we should not use this list command ,List will Check the details inside the data so.
    contact_details: Dict[str,str] #we should this not use  dict command 

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.linkdin_url)
    print(patient.email)
    print(patient.contact_details)
    print(patient.married)
    print('Inserted ')


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.linkdin_url)
    print(patient.email)
    print(patient.contact_details)
    print('Updated')

##################################################
patient_info = {
    'name': 'Ram',
    'age': 30,  
    'email':'xyz@gmail.com',
    'weight': 75.2,
    'linkdin_url':'htpp:linkdin.com',
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'phone': '1234567879'  
    }
}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)
print('--'*10)
patient_info = {
    'name': 'Krish',
    'age': 30,  
    'weight': 60.2,
    'linkdin_url':'htpp:linkdin.com',
    'email':'xyz@gmail.com',
    'contact_details': {
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
