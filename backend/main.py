from fastapi import FastAPI
from routes.employees import router as employees_router

app = FastAPI()
app.include_router(employees_router)


@app.get("/")
def greet():
    return {
        'message': "Matvei gandon"
    }