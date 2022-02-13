import requests
import streamlit as st
import datetime
import time
import pandas as pd
import json
import plotly.express as px
import boto3

client = boto3.client('s3')
result = client.get_object(Bucket="sagemaker-us-east-1-118600533013", Key="bitcoin-notebook/data/batch-prediction/test.json.out") 
csvcontent = result['Body'].read().decode('utf-8')
data = csvcontent.split("}")
d = data[0]+'}}'
e = data[2]+'}}'
bit_mean = json.loads(d)['mean']
ev_mean = json.loads(e)['mean']




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

# Prediction
today = datetime.date.today()
date_pred = [today + datetime.timedelta(days=i) for i in range(1,8)]

df_pred = pd.DataFrame(date_pred, columns=['Date_Time'])

#df_pred['Ethereum'] = ev_mean

# # Bollinger bands
# st.header('**Bollinger Bands**')
# qf=cf.QuantFig(df,title='First Quant Figure',legend='top',name='GS')
# # qf.add_bollinger_bands()
# fig = qf.iplot(asFigure=True)
# st.plotly_chart(fig)

if id == 'bitcoin':
    df_pred['Price'] = bit_mean
    df_long = df.append(df_pred, ignore_index=True)
    st.header('**Bitcoin Price Prediction for The Next 7 Days**')
    fig = px.line(df_long, x='Date_Time', y='Price')
    st.write(fig)
elif id == 'ethereum':
    df_pred['Price'] = ev_mean
    df_long = df.append(df_pred, ignore_index=True)
    st.header('**Ethereum Price Prediction for The Next 7 Days**')
    fig = px.line(df_long, x='Date_Time', y='Price')
    st.write(fig)
else: 
    st.header('**Price Trend for {}**'.format(id))
    fig = px.line(df, x='Date_Time', y='Price')
    st.write(fig)

# Display Data Table

st.header("Coin Price Data")
st.write(df)