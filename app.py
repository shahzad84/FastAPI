from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

students={
    1:{
        "name":"shahzad",
        "age":11,
        "year":"year 12"

    }
}
class Studentvalue(BaseModel):
    name:str
    age:int
    year:str

@app.get("/")
def index():
    return{"name":"first Data"}
@app.get("/get-student/{student_id}")
def get_student(student_id:int): # int= Path(None,gt=0,lt=4)#gt is greater than.
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*,student_id:int,name:Optional[str]=None,age:int= None):# none will remove the require parameter or simple we can write as name:str
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data":"Not Found"}


@app.post("/create-student/{student_id}")
def create_student(student_id:int,student:Studentvalue):
    if student_id in students:
        return {"Error":"student exists"}
    students[student_id]=student
    return students[student_id]
    