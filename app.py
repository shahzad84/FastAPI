from fastapi import FastAPI,Path
app=FastAPI()

students={
    1:{
        "name":"shahzad",
        "age":"21"
    }
}
@app.get("/")
def index():
    return{"name":"first Data"}
@app.get("/get-student/{student_id}")
def get_student(student_id:int): # int= Path(None,gt=0,lt=4)#gt is greater than.
    return students[student_id]
