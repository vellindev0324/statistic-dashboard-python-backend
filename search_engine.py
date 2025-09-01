
def search_engine(df,key) :
    # Country Dataframe
    df_by_country = df[df["country"] == key]
    # Number of Contacted
    df_number = df_by_country["country"].value_counts()
    # # Index by Number of Contacted
    # print(df_by_country)
    # Accounts for Country
    df_accounts = df_by_country["account"].nunique()
    
    # # Number of Ran by Account
    df_by_ran = df[(df["country"] == key)&(df["status"] == "Run")]["account"].value_counts()
    df_by_ran_total = df[(df["country"] == key)&(df["status"] == "Run")]["country"].value_counts()
    # # Number of Reported by Account
    df_by_report = df[(df["country"] == key)&(df["status"] == "Report/Block")]["account"].value_counts()
    df_by_report_total = df[(df["country"] == key)&(df["status"] == "Report/Block")]["country"].value_counts()
    # # Number of Accept by Account
    df_by_accept = df[(df["country"] == key)&(df["status"] == "Accept")]["account"].value_counts()
    df_by_accept_total = df[(df["country"] == key)&(df["status"] == "Accept")]["country"].value_counts()
    # # Number of Chatting by Account
    df_by_chatting = df[(df["country"] == key)&(df["status"] == "Chatting")]["account"].value_counts()
    df_by_chatting_total = df[(df["country"] == key)&(df["status"] == "Chatting")]["country"].value_counts()
    # # Number of Waiting by Account
    df_by_waiting = df[(df["country"] == key)&(df["status"] == "Waiting")]["account"].value_counts()
    df_by_waiting_total = df[(df["country"] == key)&(df["status"] == "Waiting")]["country"].value_counts()

    return_df = {
        "df_number" : df_number.to_dict(),
        "df_accounts" : df_accounts.to_dict(),
        "df_by_ran" : df_by_ran.to_dict(),
        "df_by_ran_total" : df_by_ran_total.to_dict(),
        "df_by_report" : df_by_report.to_dict(),
        "df_by_report_total":df_by_report_total.to_dict(),
        "df_by_accept":df_by_accept.to_dict(),
        "df_by_accept_total":df_by_accept_total.to_dict(),
        "df_by_chatting":df_by_chatting.to_dict(),
        "df_by_chatting_total":df_by_chatting_total.to_dict(),
        "df_by_waiting":df_by_waiting.to_dict(),
        "df_by_waiting_total":df_by_waiting_total.to_dict()
    }
    return return_df
