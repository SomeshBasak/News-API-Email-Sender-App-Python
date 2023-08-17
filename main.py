import requests

API_KEY = "35976f576b924a5fac978a0e0bd8b70e"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-07-17&" \
      "sortBy=publishedAt&apiKey=35976f576b924a5fac978a0e0bd8b70e"
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["description"])
