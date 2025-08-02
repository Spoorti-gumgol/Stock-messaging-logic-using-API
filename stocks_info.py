from datetime import datetime,timedelta
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key_news = 'your generated API key from news endpoint'
api_key_stock = 'your generated API key form stock endpoint'
account_sid = 'your account sid'
auth_token = 'your auth token'



yesterday = datetime.today().date()- timedelta(days=1)
day_before_yesterday = yesterday- timedelta(days=1)

params_stock ={

    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":api_key_stock

}

response_stock = requests.get(url=STOCK_ENDPOINT,params=params_stock)
if response_stock.status_code != 200:
    response_stock.raise_for_status()
stock_data = response_stock.json()
yesterday_closing_price = float(stock_data["Time Series (Daily)"][f'{yesterday}']['4. close'])
day_before_yesterday_closing_price = float(stock_data["Time Series (Daily)"][f'{day_before_yesterday}']['4. close'])

params_news ={
    "q":COMPANY_NAME,
    "apiKey":api_key_news,
}

response_news = requests.get(url=NEWS_ENDPOINT,params=params_news)
if response_news.status_code != 200:
    response_news.raise_for_status()


news_data = response_news.json()
top_three_news = news_data["articles"][:3]
top_three_news_data =[data["description"] for data in top_three_news]

client = Client(account_sid, auth_token)



if (day_before_yesterday_closing_price-yesterday_closing_price)<0:
    percentage_of_rise_or_low = ((abs(yesterday_closing_price-day_before_yesterday_closing_price))/(day_before_yesterday_closing_price))*100
    if percentage_of_rise_or_low>5:
        for news in top_three_news_data:
            message = client.messages.create(
                from_='whatsapp:+your twilio no',
                body=f"""
                    TSLA: ⬆️{percentage_of_rise_or_low}%
                    Headline: {news}
                    """,
                to='whatsapp:+your no'
            )
    else:
        print("No news")
elif (day_before_yesterday_closing_price-yesterday_closing_price)==0:
    percentage_of_rise_or_low = ((abs(yesterday_closing_price-day_before_yesterday_closing_price))/(day_before_yesterday_closing_price))*100
else:
    percentage_of_rise_or_low = ((abs(yesterday_closing_price-day_before_yesterday_closing_price))/(day_before_yesterday_closing_price))*100
    if percentage_of_rise_or_low>5:
        for news in top_three_news_data:
            message = client.messages.create(
                from_='whatsapp:+your twilio virtual no',
                body=f"""
                    TSLA: ⬇️{percentage_of_rise_or_low}%
                    Headline: {news}""",
                to='whatsapp:+your no.'
            )
    else:
        print("No news")

