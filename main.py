import requests
from fastapi import FastAPI
import uvicorn

# r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

# print(r.json()['bpi']['USD']['rate'])

application = FastAPI()

@application.get('/')
def root():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    return {'Bitcoint_rate USD': r.json()['bpi']['USD']['rate']}

@application.get("/GBP")
def GBP():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    return {'Bitcoint_rate GBP': r.json()['bpi']['GBP']['rate']}

@application.get("/EUR")
def EUR():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    return {'Bitcoint_rate EUR': r.json()['bpi']['EUR']['rate']}

# run the app.
if __name__ == "__main__":
    uvicorn.run(application, port=8080, host='0.0.0.0')