from fastapi import APIRouter
from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    #employee_id: int
    name: str
    username: str
    
class EmployeeResponse(BaseModel):
    employee_id: int
    name: str
    username: str
    
router = APIRouter()

@router.get('/employees')
def get_employees():
    return {'employees:': []}


@router.get('/employees/{id}')
def get_employee(id: int):
    return {'employee_id:': id,
            'info': [] }

@router.post('/employees')
def create_employee(employee: EmployeeCreate):
    return employee

@router.delete('/employees/{id}')
def delete_employee(id: int):
    #TODO: delete logic
    return {
        'message': "employee deleted"
    }