from fastapi import FastAPI
from starlette.responses import RedirectResponse

from Service.IsPrimeService import IsPrime

app = FastAPI()

@app.get("/")
def raiz():
    return RedirectResponse(url="/docs/")

isPrim = IsPrime()

@app.get("/hello")
def hello():
    return isPrime.hello()

@app.get("/IsPrime/{numero}")
def isPrime(numero: int):
    return isPrim.validate_number(numero)


    
@app.get("/fibonacci/{numero}")
def validate_fibonacci(number: int):
    if number is str: return {"Digíte un número no sea imbécil"}
    return {"Número que correspone a la posición "+str(number)+' es': calculate_fibonacci(number)}

def calculate_fibonacci(number: int):
    number_init, end_number, sucesion = 1, 1, []
    for x in range(number):
        sucesion.append(number_init)
        sucesion.append(end_number)
        number_init = number_init + end_number
        end_number = number_init + end_number
    return sucesion[number]
