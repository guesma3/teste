from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    A: int
    B: int

@app.post("/compare")
def compare_values(data: InputData):
    a = data.A
    b = data.B

    result = max(a, b)
    return {"result": result}
