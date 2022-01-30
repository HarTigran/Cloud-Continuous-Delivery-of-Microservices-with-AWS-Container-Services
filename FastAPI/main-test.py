import requests

def ping():
    r = requests.get(
            "https://api.coingecko.com/api/v3/coins/{}/market_chart/range?vs_currency={}&from={}&to={}".format(
                'bitcoin', 'usd', '1643329264','1643415664'
            )
        )
    try:
        r.status_code == 200
    except ValueError:
        return "Link is unavailable"
        
def test_link_check():
    assert ping() != 'Link is unavailable'
