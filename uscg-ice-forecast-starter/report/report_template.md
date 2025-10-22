# Domestic Icebreaking — 3‑Day Operational Ice Forecast
**Team:** <Your names>  
**Date:** <YYYY‑MM‑DD>

## 1. Mission & Inputs
- Datasets: Ice Data, Water Surface Temperature, Weather Data (winds, air temp)
- AOI: Great Lakes
- Time horizon: Today + 3 days

## 2. Method
- Ingest → feature merge by (lat, lon, time)
- Model: RandomForestRegressor (baseline)
- Recursion for +2/+3 days
- Confidence: empirical residuals ± one sigma

## 3. Results
- RMSE / MAE on hold‑out
- Maps: see `/outputs/maps/`

## 4. Operational Value
- Chokepoint callouts
- Update cadence (12–24h), auto‑ingest, dashboard

## 5. Next Steps
- Swap to XGBoost or LSTM
- Add ice motion vectors (wind + prior day drift)
