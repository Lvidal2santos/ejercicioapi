from fastapi import FastAPI

CAMBIOTODAYAPIKEY = '11155|CLin3h*eomdP*quJH7eUXXGrJ2ucmSxd'

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Testing FastAPI"}
