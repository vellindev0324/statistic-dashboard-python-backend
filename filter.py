from use_service_account import fetch_data_from_sheet
import pandas as pd

# Fetch Data 
def fetch_data() :
    data = fetch_data_from_sheet()

    # Convert to DataFrame
    df = pd.DataFrame([row[:9] for row in data], columns=["No", "link", "name", "connection", "country", "account", "date", "status", "balanced"])

    # Convert date column to datetime type
    df["date"] = pd.to_datetime(df["date"], format="%m/%d/%Y", errors="coerce")

    return_df = {
            "raw_df":df, 
            "filtered_run":df[df["status"] == "Run"],
            "filtered_notInterested":df[df["status"] == "Not Interested"],
            "filtered_connecting":df[df["status"] == "connecting"],
            "filtered_accept":df[df["status"] == "Accept"],
            "filtered_chatting":df[df["status"] == "Chatting"],
            "filtered_report":df[df["status"] == "Report/Block"],
            "filtered_waiting":df[df["status"] == "Waiting"],
            "filtered_balanced":df[df["balanced"] == "yes"]
        }
    
    return return_df
# def rawData() :
#     return df

# def filtered_run() :
#     # Filter
#     filtered = df[df["status"] == "Run"]
#     return filtered

# def filtered_report() :
#     # Filter
#     filtered = df[df["status"] == "Report/Block"]
#     return filtered

# def filtered_notInterested() :
#     # Filter
#     filtered = df[df["status"] == "Not Interested"]
#     return filtered

# def filtered_connecting() :
#     # Filter
#     filtered = df[df["status"] == "connecting"]
#     return filtered

# def filtered_accept() :
#     # Filter
#     filtered = df[df["status"] == "Accept"]
#     return filtered

# def filtered_chatting() :
#     # Filter
#     filtered = df[df["status"] == "Chatting"]
#     return filtered

# def filtered_waiting() :
#     # Filter
#     filtered = df[df["status"] == "Waiting"]
#     return filtered

# def filtered_balanced() :
#     # Filter
#     filtered = df[df["balanced"] == "yes"]
#     return filtered

