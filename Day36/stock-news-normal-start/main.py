import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_api_key = "8A57S22YZJ06WSAU"
news_apikey = "406a814b8dc946a89ce663b58bbbd7ef"
twilio_appid = 'ACde652469f64d4ff082f680a6baccc9db'
twilio_auth_token = '24c0232853108d2fae2fcd1532a20f70'

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_param = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : stock_api_key
}
response = requests.get(STOCK_ENDPOINT, params = stock_param)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close'] 
print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close'] 
print(day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference_in_price = float(day_before_yesterday_closing_price) - float(yesterday_closing_price)
up_down = None
if difference_in_price > 0:
    up_down = "🔺"
else:
    up_down = "🔻"  
difference_in_price = round(abs(difference_in_price))     
print(difference_in_price)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percent = (difference_in_price / float(yesterday_closing_price)) * 100
print(diff_percent)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

# if diff_percent > 5:
#     print("Get News")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

news_param = {
    "apiKey" : news_apikey,
    "qInTitle" : COMPANY_NAME,
}

if diff_percent > 1:
    news_response = requests.get(NEWS_ENDPOINT, params = news_param)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

three_articles = articles[:3]
print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

formatted_article = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {articles['title']}.\nBrief: {articles['description']}." for articles in three_articles]
print(formatted_article)

#TODO 9. - Send each article as a separate message via Twilio. 

client = Client(twilio_appid, twilio_auth_token)

for arti in formatted_article:
    message = client.messages.create(
            from_='+13343848564',
            body=arti,
            to='+919994023452'
        )
    print(message.status) 

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

