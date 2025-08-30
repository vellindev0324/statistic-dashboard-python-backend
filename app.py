from filter import filtered_run, filtered_balanced, filtered_report, rawData
from flask_cors import CORS  # Import CORS
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

@app.route("/api/result_data", methods=["GET"])
def get_result_data():
    df_run = filtered_run()
    df_balanced = filtered_balanced()
    df_report = filtered_report()
    df = rawData()

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

    contacted_countries_counts = df['country'].value_counts().to_dict()

    # Create a dictionary to return
    response_data = {
        "run_country_counts": run_country_counts,
        "run_account_counts": run_account_counts,
        "balanced_country_counts": balanced_country_counts,
        "balanced_account_counts": balanced_account_counts,
        "report_country_counts": report_country_counts,
        "report_account_counts": report_account_counts,
        "contacted_countries_counts": contacted_countries_counts
    }

    return jsonify(response_data)

if __name__ == "__main__" :
    app.run()

