import requests
import json


url = 'https://api.languagetool.org/v2/check'
data = {
    "text": "Ths is a nixe day",
    "language": "auto"
}

response = requests.post(url, data=data)
result = json.loads(response.text)
print(result)