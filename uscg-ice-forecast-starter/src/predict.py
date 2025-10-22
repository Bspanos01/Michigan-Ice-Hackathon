"""Produce day+1/+2/+3 predictions by recursive roll-forward and save CSVs."""
from pathlib import Path
import pandas as pd
import numpy as np
import joblib
from .config import DATA_PROCESSED, MODELS_DIR, OUTPUTS_DIR

def main():
    bundle = joblib.load(Path(MODELS_DIR)/"model.pkl")
    model = bundle["model"]; features = bundle["features"]

    df = pd.read_csv(Path(DATA_PROCESSED)/"training_matrix.csv", parse_dates=["time"])
    latest_day = df["time"].max().normalize()
    outdir = Path(OUTPUTS_DIR)/"maps"; outdir.mkdir(parents=True, exist_ok=True)

    preds_list = []
    prev = df[df["time"]==latest_day].copy()
    for d in [1,2,3]:
        day = latest_day + pd.Timedelta(days=d)
        frame = prev.copy()
        frame["time"] = day
        # Predict thickness
        X = frame[features].fillna(method="ffill").fillna(0)
        frame["pred_ice_thickness"] = model.predict(X)
        frame.to_csv(Path(DATA_PROCESSED)/f"pred_day{d}.csv", index=False)
        preds_list.append(frame[["lat","lon","time","pred_ice_thickness"]])
        # carry forward for recursive step (could add melt/growth heuristics)
        prev = frame.copy()

    allpreds = pd.concat(preds_list, ignore_index=True)
    allpreds.to_csv(Path(DATA_PROCESSED)/"predictions_all.csv", index=False)
    print("[predict] wrote predictions for +1/+2/+3 days")

if __name__ == "__main__":
    main()
