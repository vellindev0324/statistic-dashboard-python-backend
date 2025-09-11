import requests
import json

with open('app/apiCredential.json', 'r') as file:
    json_data = json.load(file)


RANGE = "Class A!A2:D10"

url = f"https://sheets.googleapis.com/v4/spreadsheets/{json_data['SPREADSHEET_ID']}/values/{RANGE}?key={json_data['API_KEY']}"

response = requests.get(url)
data = response.json()

print(data)
