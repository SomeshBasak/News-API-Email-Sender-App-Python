import requests
from send_email import send_email

topic = "chandrayan"
API_KEY = "35976f576b924a5fac978a0e0bd8b70e"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&from=2023-07-24&" \
      "sortBy=publishedAt&" \
      "apiKey=35976f576b924a5fac978a0e0bd8b70e&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject:Today's news" + "\n"

for article in content["articles"][:20]:
    if (article["title"] is not None) and (article["description"] is not None):
        body = body + article["title"] + "\n" + article["description"] \
               + "\n" + article["url"] + 2 * "\n"


body = body.encode("utf-8")
send_email(message=body)

