
# Market Risk Analytics API

A FastAPI-based service to calculate market risk for financial assets.

## Steps to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the application locally:
   ```
   uvicorn app.main:app --reload
   ```
3. Use the API to calculate risk:
   - Endpoint: `/risk`
   - Query parameters: `asset` (string), `exposure` (float)
            