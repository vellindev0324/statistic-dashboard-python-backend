
def search_engine(df,key) :
    # Country Dataframe
    df_by_country = df[df["country"] == key]
    # Number of Contacted
    df_number = df_by_country["country"].value_counts().to_dict()
    # # Index by Number of Contacted
    # print(df_by_country)
    # Accounts for Country
    df_accounts = df_by_country["account"].nunique()
    
    # # Number of Ran by Account
    df_by_ran = df[(df["country"] == key)&(df["status"] == "Run")]["account"].value_counts().to_dict()
    df_by_ran_total = df[(df["country"] == key)&(df["status"] == "Run")]["country"].value_counts().to_dict()
    # # Number of Reported by Account
    df_by_report = df[(df["country"] == key)&(df["status"] == "Report/Block")]["account"].value_counts().to_dict()
    df_by_report_total = df[(df["country"] == key)&(df["status"] == "Report/Block")]["country"].value_counts().to_dict()
    # # Number of Accept by Account
    df_by_accept = df[(df["country"] == key)&(df["status"] == "Accept")]["account"].value_counts().to_dict()
    df_by_accept_total = df[(df["country"] == key)&(df["status"] == "Accept")]["country"].value_counts().to_dict()
    # # Number of Chatting by Account
    df_by_chatting = df[(df["country"] == key)&(df["status"] == "Chatting")]["account"].value_counts().to_dict()
    df_by_chatting_total = df[(df["country"] == key)&(df["status"] == "Chatting")]["country"].value_counts().to_dict()
    # # Number of Waiting by Account
    df_by_waiting = df[(df["country"] == key)&(df["status"] == "Waiting")]["account"].value_counts().to_dict()
    df_by_waiting_total = df[(df["country"] == key)&(df["status"] == "Waiting")]["country"].value_counts().to_dict()

    # # Number of Balanced by Account
    df_by_balanced = df[(df["country"] == key)&(df["balanced"] == "yes")]["account"].value_counts().to_dict()
    df_by_balanced_total = df[(df["country"] == key)&(df["balanced"] == "yes")]["country"].value_counts().to_dict()

    return_df = {
        "df_number" : df_number,
        "df_accounts" : df_accounts,
        "df_by_ran" : df_by_ran,
        "df_by_ran_total" : df_by_ran_total,
        "df_by_report" : df_by_report,
        "df_by_report_total":df_by_report_total,
        "df_by_accept":df_by_accept,
        "df_by_accept_total":df_by_accept_total,
        "df_by_chatting":df_by_chatting,
        "df_by_chatting_total":df_by_chatting_total,
        "df_by_waiting":df_by_waiting,
        "df_by_waiting_total":df_by_waiting_total,
        "df_by_balanced":df_by_balanced,
        "df_by_balanced_total":df_by_balanced_total
    }
    return return_df
