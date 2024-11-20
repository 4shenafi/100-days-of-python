import requests
import os
from twilio.rest import Client

stock_api = os.environ['STOCK_API']
news_api = os.environ['NEWS_API']

parameters = {
    "function": "GLOBAL_QUOTE",
    "symbol": "TSLA",
    "interval": "1m",
    "apikey": stock_api
}
response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()

parameters = {
    "q": "tesla",
    "from": "2024-10-20",
    "sortBy": "publishedAt",
    "page_size": 1,
    "apikey": news_api,
}

response2 = requests.get("https://newsapi.org/v2/everything", params=parameters)
response2.raise_for_status()
news = response2.json()

article = news.get("articles", [])[0]
title = article["title"]
description = article["description"]
article_url = article["url"]

global_quote = data["Global Quote"]
current_price = float(global_quote["05. price"])
previous_close = float(global_quote["08. previous close"])

stock_message = f"Tesla Stock Info:\nCurrent price: ${current_price}\nPrevious close: ${previous_close}"
news_message = f"\nLatest Tesla News:\nTitle: {title}\nDescription: {description}\nRead more: {article_url}"

full_message = stock_message + news_message

twilio_account_sid = ""
twilio_auth_token = ""
twilio_phone_number = ""
to_phone_number = ""

client = Client(twilio_account_sid, twilio_auth_token)
message = client.messages.create(
    body=full_message,
    from_=twilio_phone_number,
    to=to_phone_number
)


