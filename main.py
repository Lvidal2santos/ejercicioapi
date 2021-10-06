from fastapi import FastAPI, Path, HTTPException
import requests

TOKEN = '11155|CLin3h*eomdP*quJH7eUXXGrJ2ucmSxd'
VALID_CURRENCIES = ['BGN', 'BRL', 'USD', 'EUR']
app = FastAPI()


@app.get("/cotizacion/{currency}/{quantity}")
def cotizacion(currency: str = Path(None, description="El código ISO de la moneda que se quiere cotizar"),
               quantity: str = Path(None, description="La cantidad que se quiere cotizar.")):

    currency = currency.upper()
    if currency not in VALID_CURRENCIES:
        return HTTPException(status_code=404, detail="Invalid currency ISO")

    response = requests.get(f'https://api.cambio.today/v1/quotes/ARS/{currency}/json?quantity={quantity}&key={TOKEN}')

    return response.json()['result']['amount']

