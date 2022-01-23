import requests
from fastapi import FastAPI, Request
import uvicorn
import json

application = FastAPI()

@application.get('/')
def root(req: Request):
    query_params = dict(req.query_params)
    id = query_params['id']
    currency = query_params['currency']
    from_date = query_params['from_date']
    to_date = query_params['to_date']
    r = requests.get('https://api.coingecko.com/api/v3/coins/{}/market_chart/range?vs_currency={}&from={}&to={}'.format(id,currency,from_date,to_date ))
    try:
        return json.dumps({'Bitcoint_price': r.json()['prices']})
    except Exception:
        return Response("Internal server error", status_code=500)

if __name__ == "__main__":
    uvicorn.run(application, port=8080, host='0.0.0.0')
