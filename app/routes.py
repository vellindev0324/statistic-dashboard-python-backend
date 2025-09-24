from flask import Blueprint, jsonify, request
from flask_cors import CORS  # Import CORS
from datetime import datetime, timedelta, date
from .lib.search_engine import search_engine
from .lib.yesterday_data import get_yesterday_stats
from .lib.filter import fetch_data
from .lib.handle_sheet import add_new_content, update_status_content, record_daily_data
from .lib.use_service_account import get_sheet_dict, fetch_data_from_sheet

bp = Blueprint("api", __name__)
CORS(bp) # Enable CORS for all routes

def recording_daily_data(data):
    
    df = fetch_data(data)
    df_raw = df["raw_df"]
    # Get Yesterday Data
    y_data = get_yesterday_stats(df_raw)
    today = date.today()
    listed_y_data = [today.strftime("%m/%d/%Y"), y_data["y_total_contacts"], y_data["y_accept_yesterday"], y_data["y_chatting_yesterday"],y_data["y_waiting_yesterday"]]
    sheet2 = get_sheet_dict(2)
    record_daily_data(today,sheet2,listed_y_data)

@bp.route("/api/result_data", methods=["GET"])
def get_result_data():
    data = fetch_data_from_sheet()
    recording_daily_data(data)
    df = fetch_data(data)
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

@bp.route("/api/submit", methods=["POST"])
def receive_text():
    data = fetch_data_from_sheet()
    df = fetch_data(data)
    df_raw = df["raw_df"]
    # Contacted Countries
    data = request.get_json()
    user_text = data.get("text", "")
    
    # Example: process text
    response = search_engine(df_raw, user_text)
    return jsonify(response)

@bp.route("/api/update", methods=["POST"])
def update_status():
    sheet1 = get_sheet_dict(1)
    data = request.get_json()  # get JSON from frontend
    keyword = data.get("keyword")
    new_value = data.get("new_value")
    res = update_status_content(keyword, new_value, sheet1)
    return res

    

def register_routes(app):
    app.register_blueprint(bp)

