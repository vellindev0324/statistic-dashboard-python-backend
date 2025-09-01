import gspread
from google.oauth2.service_account import Credentials
import json

with open('apiCredential.json', 'r') as file:
    json_data = json.load(file)

def fetch_data_from_sheet():
    # Define scope
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

    # Authorize
    creds = Credentials.from_service_account_file(
        "service_account.json", scopes=SCOPES
    )
    client = gspread.authorize(creds)

    # Open spreadsheet by ID
    sheet = client.open_by_key(json_data['SPREADSHEET_ID']).sheet1

    # Read data
    data = sheet.get_all_values()
    return data
    