from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def raiz():
    return RedirectResponse(url="/docs/")

@app.get("/hello")
def hello():
    return "Hello FastApi"

@app.get("/IsPrime/{numero}")
def validate_number(number: int):
    if number < 2 or number <=0: return False
    remainderCount = calculate_is_prime_number(number)
    return True if remainderCount==0 else False

def calculate_is_prime_number(number: int):
    remainderCount = 0
    for i in range(2, number):
        remainder = number % i
        if remainder == 0: remainderCount+=1
    return remainderCount
    
@app.get("/fibonacci/{numero}")
def calculate_fibonacci(number: int):
    number_init, end_number, sucesion = 1, 1, []
    for x in range(number):
        sucesion.append(number_init)
        sucesion.append(end_number)
        number_init = number_init + end_number
        end_number = number_init + end_number
    return {"Número que correspone a la posición": sucesion[number]}
