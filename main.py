import requests as r
import json
import pandas as pd

api_key = "APIKEY"

url = f"https://newsapi.org/v2/everything?q=Apple&from=2023-03-21&sortBy=popularity&apiKey={api_key}"

request = r.get(url)

content = request.json()

c = ""

for article in content["articles"]:
    c += f'{article["title"]};{article["content"]};{article["author"]}'
print(c)

