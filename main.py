import requests
from send_email import send_email


API_KEY = "35976f576b924a5fac978a0e0bd8b70e"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-07-17&" \
      "sortBy=publishedAt&apiKey=35976f576b924a5fac978a0e0bd8b70e"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)

