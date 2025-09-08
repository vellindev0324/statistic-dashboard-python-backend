# from filter import filtered_run, filtered_balanced, filtered_report, rawData
from filter import fetch_data
from flask_cors import CORS  # Import CORS
from flask import Flask, jsonify, request
from search_engine import search_engine
from yesterday_data import get_yesterday_stats

app = Flask(__name__)
CORS(app) # Enable CORS for all routes



@app.route("/api/result_data", methods=["GET"])
def get_result_data():
    
    df = fetch_data()
    df_run = df["filtered_run"]
    df_balanced = df["filtered_balanced"]
    df_report = df["filtered_report"]
    df_raw = df["raw_df"]

    # Get Yesterday Data
    y_data = get_yesterday_stats(df_raw)
    # Country & Accounts by Run
    run_country_counts = df_run['country'].value_counts().to_dict()
    run_account_counts = df_run['account'].value_counts().to_dict()

    # Country & Accounts by Balanced
    balanced_country_counts = df_balanced['country'].value_counts().to_dict()
    balanced_account_counts = df_balanced['account'].value_counts().to_dict()

    # Country & Accounts by Report
    report_country_counts = df_report['country'].value_counts().to_dict()
    report_account_counts = df_report['account'].value_counts().to_dict()

    # Contacted Countries

    contacted_countries_counts = df_raw['country'].value_counts().to_dict()
    

    # Create a dictionary to return
    response_data = {
        "run_country_counts": run_country_counts,
        "run_account_counts": run_account_counts,
        "balanced_country_counts": balanced_country_counts,
        "balanced_account_counts": balanced_account_counts,
        "report_country_counts": report_country_counts,
        "report_account_counts": report_account_counts,
        "contacted_countries_counts": contacted_countries_counts,
        "y_data":y_data,
        "chatting_names":df["chatting_names"],
        "waiting_names":df["waiting_names"],
        "accept_names":df["accept_names"],
        "events_by_account":df["events_by_account"]
    }
    return jsonify(response_data)

@app.route("/api/submit", methods=["POST"])
def receive_text():
    df = fetch_data()
    df_raw = df["raw_df"]
    # Contacted Countries
    data = request.get_json()
    user_text = data.get("text", "")
    
    # Example: process text
    response = search_engine(df_raw, user_text)
    return jsonify(response)

if __name__ == "__main__" :
    app.run(debug=True, use_reloader=False)

