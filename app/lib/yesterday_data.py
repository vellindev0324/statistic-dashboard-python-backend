from datetime import datetime, timedelta
import pandas as pd

def get_yesterday_stats(df):

    # ensure Date is datetime
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # get yesterday
    # yesterday = (datetime.now() - timedelta(days=1)).date()
    today = datetime.now().date()
    df_yesterday = df[df["date"].dt.date == today]

    # total contacts yesterday
    y_total_contacts = len(df_yesterday)

    # breakdown by status
    y_accept_count = len(df_yesterday[df_yesterday["status"] == "Accept"])
    y_chatting_count = len(df_yesterday[df_yesterday["status"] == "Chatting"])
    y_waiting_count = len(df_yesterday[df_yesterday["status"] == "Waiting"])

    # contact by account yesterday
    y_contacts_by_account = df_yesterday["account"].value_counts().to_dict()

    response = {
        "y_total_contacts": y_total_contacts,
        "y_accept_yesterday": y_accept_count,
        "y_chatting_yesterday": y_chatting_count,
        "y_waiting_yesterday": y_waiting_count,
        "y_contacts_by_account": y_contacts_by_account,
    }
    return response

