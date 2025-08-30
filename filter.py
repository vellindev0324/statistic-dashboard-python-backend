from use_service_account import export_data
import pandas as pd

# Import Data 
data = export_data()

# Convert to DataFrame
df = pd.DataFrame([row[:9] for row in data], columns=["No", "link", "name", "connection", "country", "account", "date", "status", "balanced"])

# Convert date column to datetime type
df["date"] = pd.to_datetime(df["date"], format="%m/%d/%Y", errors="coerce")

def rawData() :
    return df

def filtered_run() :
    # Filter
    filtered = df[df["status"] == "Run"]
    return filtered

def filtered_report() :
    # Filter
    filtered = df[df["status"] == "Report/Block"]
    return filtered

def filtered_notInterested() :
    # Filter
    filtered = df[df["status"] == "Not Interested"]
    return filtered

def filtered_connecting() :
    # Filter
    filtered = df[df["status"] == "connecting"]
    return filtered

def filtered_accept() :
    # Filter
    filtered = df[df["status"] == "Accept"]
    return filtered

def filtered_chatting() :
    # Filter
    filtered = df[df["status"] == "Chatting"]
    return filtered

def filtered_waiting() :
    # Filter
    filtered = df[df["status"] == "Waiting"]
    return filtered

def filtered_balanced() :
    # Filter
    filtered = df[df["balanced"] == "yes"]
    return filtered

