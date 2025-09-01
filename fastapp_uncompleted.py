from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any
import requests

# Your existing functions
from filter import filtered_run, filtered_balanced, filtered_report, rawData

# Initialize app
app = FastAPI(
    title="Analytics API",
    description="API that fetches external data and processes filtered datasets.",
    version="1.0.0"
)

# Enable CORS (React frontend can call this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in production, restrict e.g. ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_URL = "https://api.example.com/data"  # Replace with your real API

# 🔹 Response Schema (Pydantic)
class ResultDataResponse(BaseModel):
    external_data: Any
    run_country_counts: Dict[str, int]
    run_account_counts: Dict[str, int]
    balanced_country_counts: Dict[str, int]
    balanced_account_counts: Dict[str, int]
    report_country_counts: Dict[str, int]
    report_account_counts: Dict[str, int]
    contacted_countries_counts: Dict[str, int]

# 🔹 External API fetcher
def fetch_external_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# 🔹 Endpoint
@app.get("/api/result_data", response_model=ResultDataResponse)
def get_result_data():
    external_data = fetch_external_data()

    df_run = filtered_run()
    df_balanced = filtered_balanced()
    df_report = filtered_report()
    df = rawData()

    response_data = {
        "external_data": external_data,
        "run_country_counts": df_run['country'].value_counts().to_dict(),
        "run_account_counts": df_run['account'].value_counts().to_dict(),
        "balanced_country_counts": df_balanced['country'].value_counts().to_dict(),
        "balanced_account_counts": df_balanced['account'].value_counts().to_dict(),
        "report_country_counts": df_report['country'].value_counts().to_dict(),
        "report_account_counts": df_report['account'].value_counts().to_dict(),
        "contacted_countries_counts": df['country'].value_counts().to_dict()
    }

    return response_data
