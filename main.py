import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "KEVHABEFBJXDL6HT"
NEWS_API_KEY = "d0455fbcefc6458f812881cd147970b1"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "full",
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

# get the day before yesterday market close price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

closing_data_difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
# . - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
market_change = closing_data_difference / yesterday_closing_price * 100

print(f"{round(market_change, 2)} %")
# - If percentage is greater than 5 then print("Get News").

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if market_change > 1:
    new_params = {
        "qInTitle": "bitcoin",
        "apikey": NEWS_API_KEY
    }
    new_response = requests.get(NEWS_ENDPOINT, params=new_params)
    articles = new_response.json()["articles"]

    # T -Python slice operator to create a list that contains the first 3 articles. Hint:
    # https://stackoverflow.com/questions/509211/understanding-slice-notation

    three_articles = articles[:3]

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_article_list = [f"Headline: {article['title']}. \n Brief: {article['description']}" for (article, description) in three_articles]

#  - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
