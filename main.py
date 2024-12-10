
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Market Risk Analytics API"}

@app.get("/risk")
def calculate_risk(asset: str, exposure: float):
    risk_value = exposure * 0.05  # Example risk calculation
    return {"asset": asset, "exposure": exposure, "risk_value": risk_value}
            