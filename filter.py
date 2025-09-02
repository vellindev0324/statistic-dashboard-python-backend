from use_service_account import fetch_data_from_sheet
import pandas as pd

# Fetch Data 
def fetch_data() :
    data = fetch_data_from_sheet()

    # Convert Data to Pandas DataFrame
    df = pd.DataFrame([row[:9] for row in data], columns=["No", "link", "name", "connection", "country", "account", "date", "status", "balanced"])

    # Convert date column to datetime type
    df["date"] = pd.to_datetime(df["date"], format="%m/%d/%Y", errors="coerce")

    # Individual Name in Chatting following Account
    df_chatting_names_by_account = df[df["status"]=="Chatting"].groupby("account")["name"].apply(list).to_dict()

    # Individual Name in Accept following Account
    df_waiting_names_by_account = df[df["status"]=="Waiting"].groupby("account")["name"].apply(list).to_dict()

    return_df = {
            "raw_df":df, 
            "filtered_run":df[df["status"] == "Run"],
            "filtered_notInterested":df[df["status"] == "Not Interested"],
            "filtered_connecting":df[df["status"] == "connecting"],
            "filtered_accept":df[df["status"] == "Accept"],
            "filtered_chatting":df[df["status"] == "Chatting"],
            "filtered_report":df[df["status"] == "Report/Block"],
            "filtered_waiting":df[df["status"] == "Waiting"],
            "filtered_balanced":df[df["balanced"] == "yes"],
            "chatting_names":df_chatting_names_by_account,
            "waiting_names":df_waiting_names_by_account
        }
    
    return return_df

