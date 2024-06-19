import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "IF7S51MU5B30WYV1"
NEWS_API_KEY = "b2cbe4fc08c84411b83d4ed7776e0124"

account_sid = "ACaa0365418ab81d7e959a8e14cce3f9ac"
auth_token = "b256b2f39c056f6b01f9a7abc35b1f4e"

# # STEP 1: Use https://www.alphavantage.co/documentation/#daily When stock price
# increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions
#  on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_parameters = {"function": "TIME_SERIES_DAILY", "symbol": STOCK_NAME, "apikey": STOCK_API_KEY}
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
data = response.json()
print(data)

daily_data_list = [value for (key, value) in data["Time Series (Daily)"].items()]
yesterday_closing_price = float(daily_data_list[0]['4. close'])
print(yesterday_closing_price)

# TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_closing_price = float(daily_data_list[1]['4. close'])
print(day_before_yesterday_closing_price)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20,
#  but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference_closing_price = abs(day_before_yesterday_closing_price - yesterday_closing_price)
print(difference_closing_price)

# TODO 4. - Work out the percentage difference in price between closing price yesterday
#  and closing price the day before yesterday.
percentage_difference_closing_price = (difference_closing_price / yesterday_closing_price) * 100
print(percentage_difference_closing_price)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# if percentage_difference_closing_price > 5:
#     print("Get News")


# # STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# TODO 6. - Use the News API to get articles related to the COMPANY_NAME.
if percentage_difference_closing_price > 5:
    news_parameters = {"apiKey": NEWS_API_KEY, "qInTitle": COMPANY_NAME}
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_data = news_response.json()["articles"]

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
#  Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = news_data[:3]
    # print(three_articles)


# # STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.
# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    info_articles_list = [f"Headline: {article['title']}\n Brief: {article['description']}" for article in three_articles]
    print(info_articles_list)

# TODO 9. - Send each article as a separate message via Twilio.

    for info_article in info_articles_list:
        client = Client(account_sid, auth_token)
        message = client.messages.create(from_='+18509990952',body=info_article, to='+17788757291')
        print(message.status)



