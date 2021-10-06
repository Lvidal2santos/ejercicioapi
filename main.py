from fastapi import FastAPI, Path
import requests

TOKEN = '11155|CLin3h*eomdP*quJH7eUXXGrJ2ucmSxd'

app = FastAPI()


@app.get("/cotizacion/{currency}/{quantity}")
def cotizacion(currency: str = Path(None, description="El código ISO de la moneda que se quiere cotizar"),
               quantity: int = Path(None, description="la cantidad que se quiere cotizar.")):

    return requests.get(f'https://api.cambio.today/v1/quotes/ARS/{currency}/json?quantity={quantity}&key=11155|CLin3h*eomdP*quJH7eUXXGrJ2ucmSxd')

