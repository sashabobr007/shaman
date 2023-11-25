from fastapi import FastAPI, Depends, File, UploadFile, Response
import uvicorn
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
import os
import pandas as pd
import numpy as np

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



test_json=[
    {
        "electro":100,
        "teplo":200,
        "kanal":300,
        "gaz":400,
        "electro_old":100,
        "teplo_old":200,
        "kanal_old":300,
        "gaz_old":400,
        "price":1,
        "price2":2,
        "price3":3,
        "price4":4,
        "pogoda":5,
        "oplata":1000,
        "okupaemost" : 5
    }
]



def get_years(money, house):
    return 13 + beta(a=8, b=3) * (30 - 13)


def get_cost(area=150 + 150):
    df = pd.read_excel('Artem_Hakatonovich.xlsx', index_col=0) * area
    df.to_csv('Artem_Hakatonovich.csv')

df = pd.read_csv('adres.csv', sep=";")
df['Город'] = df['Адрес'].apply(lambda x: x.split(',')[0])


@app.get("/test_city/")
async def root():
    city = df['Город'].unique().tolist()
    return city

@app.get("/test_adres/")
async def root(city: str):
    try:
        adresa = df.query(f'Город == "{city}"')['Адрес'].tolist()
        return adresa
    except:
        return {"message": "error"}

@app.get("/")
async def root():
    return {"message": "success"}

@app.get("/inflacia/")
async def inflacia():
    return FileResponse('inflycia.csv')

@app.post("/invest/")
async def invest(summa : int, chekbox : int, square : int):

    return test_json


@app.get("/test_json/")
async def root():
    return test_json

@app.get("/get_pogoda_month/")
async def get_years(year: int, month:int, city: str):
    df = pd.read_csv(f'{city}.csv')
    n = df.query(f'year == {year} and month == {month}')['temperature_2m'].values[0]
    return n


@app.get("/get_pogoda_year/")
async def get_years(year: int, city: str):
    df = pd.read_csv(f'{city}.csv')
    n = df.query(f'year == {year} and month == 10')['temperature_2m'].values[0]
    return n


@app.get("/get_years/")
async def get_years(money : int, house: int):

    return (13 + beta(a=8, b=3) * (30 - 13))

@app.get("/get_cost/")
async def get_cost(area : int):
    df = pd.read_excel('Artem_Hakatonovich.xlsx', index_col=0)  * area
    df.to_json('Artem_Hakatonovich.json')
    return FileResponse('Artem_Hakatonovich.json')

@app.get("/get_best_adresses/")
async def get_best_adresses():
    ans ={}
    list = get_best_adresses(3)
    for elem in list:
        ans[elem] = [120000, 15000]
    return ans


@app.delete("/")
async def kill():
    os.kill(os.getpid(), 9)
    return {"message": "error"}


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
