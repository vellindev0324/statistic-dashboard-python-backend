# import gspread
# from google.oauth2.service_account import Credentials
# import json

# with open('app/apiCredential.json', 'r') as file:
#     json_data = json.load(file)

# def fetch_data_from_sheet():
#     # Define scope
#     SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

#     # Authorize
#     creds = Credentials.from_service_account_file(
#         "app/service_account.json", scopes=SCOPES
#     )
#     client = gspread.authorize(creds)

#     # Open spreadsheet by ID
#     sheet = client.open_by_key(json_data['SPREADSHEET_ID']).sheet1

#     # Read data
#     data = sheet.get_all_values()
#     return data

import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os
import json

# load .env
load_dotenv()

def fetch_data_from_sheet():
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

    # Load JSON key from env variable
    service_account_info = json.loads(os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON"))
    creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)

    client = gspread.authorize(creds)
    sheet = client.open_by_key(os.getenv("SPREADSHEET_ID")).sheet1
    return sheet.get_all_values()

    