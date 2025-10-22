"""Train a baseline RandomForest model to predict ice_thickness."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
from .config import DATA_PROCESSED, MODELS_DIR, RANDOM_STATE

TARGET = "ice_thickness"

def main():
    df = pd.read_csv(Path(DATA_PROCESSED)/"training_matrix.csv")
    # Basic feature set
    features = [c for c in ["lat","lon","sst","air_temp","wind_speed","wind_dir","ice_concentration"] if c in df.columns]
    df = df.dropna(subset=features+[TARGET])
    X = df[features]; y = df[TARGET]

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=RANDOM_STATE)
    model = RandomForestRegressor(n_estimators=300, random_state=RANDOM_STATE, n_jobs=-1)
    model.fit(X_train, y_train)

    preds = model.predict(X_val)
    mae = mean_absolute_error(y_val, preds)
    rmse = mean_squared_error(y_val, preds, squared=False)
    print(f"[train] MAE={mae:.3f}  RMSE={rmse:.3f}  n={len(y_val)}")

    Path(MODELS_DIR).mkdir(exist_ok=True, parents=True)
    joblib.dump({"model": model, "features": features}, Path(MODELS_DIR)/"model.pkl")
    print("[train] saved models/model.pkl")

if __name__ == "__main__":
    main()
