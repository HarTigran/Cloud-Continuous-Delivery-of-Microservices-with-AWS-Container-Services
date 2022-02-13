import requests
import streamlit as st
import datetime
import time
import pandas as pd
import json
import plotly.express as px
import boto3
import gzip

s3 = boto3.resource("s3")
obj = s3.Object("sagemaker-us-east-1-118600533013", "bitcoin-notebook/output/regression-dd3c9070872411ec9ce40a5f9c26874b1/output/model.tar.gz")
with gzip.GzipFile(fileobj=obj.get()["Body"]) as gzipfile:
    content = gzipfile.read()
st.sidebar.subheader('content')



today = datetime.date.today()

# construct UI layout

st.sidebar.subheader('Query parameters')

# Date Time


start_date = st.sidebar.date_input("Start date", datetime.date(2022, 1, 1))
from_date = time.mktime(start_date.timetuple())

end_date = st.sidebar.date_input("End date", datetime.date.today())
to_date= time.mktime(end_date.timetuple())

# Coin Id

coin_id_list = ['bitcoin','ethereum','tether', 'binancecoin', 'usd-coin', 'cardano','solana', 'ripple'] 
id = st.sidebar.selectbox('Coin ID', coin_id_list) # Select coin

# Currency

currency_list = ['usd','eur','gbp','jpy']
currency = st.sidebar.selectbox('Currency', currency_list) # Select currency

# Get Data

payload = {'id':id, 'currency':currency,'from_date':from_date,'to_date':to_date}
res = requests.get('http://localhost:8080', params=payload)
data = json.loads(res.json())

# Transform Data

df = pd.DataFrame.from_dict(data["Bitcoint_price"])
df.columns = ['Date_Time', 'Price']
df['Date_Time'] = pd.to_datetime(df['Date_Time'], unit='ms')

# # Bollinger bands
# st.header('**Bollinger Bands**')
# qf=cf.QuantFig(df,title='First Quant Figure',legend='top',name='GS')
# # qf.add_bollinger_bands()
# fig = qf.iplot(asFigure=True)
# st.plotly_chart(fig)

# Display Plot

st.header('**Trend**')
fig = px.line(df, x='Date_Time', y='Price')
st.write(fig)

# Display Data Table

st.header("Coin Price Data")
st.write(df)