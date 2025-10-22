"""Render JPG maps for each forecast day using matplotlib (simple scatter)."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from .config import DATA_PROCESSED, OUTPUTS_DIR

def save_map(df, title, path):
    plt.figure(figsize=(8,6))
    sc = plt.scatter(df["lon"], df["lat"], c=df["pred_ice_thickness"], s=6)
    plt.colorbar(sc, label="Predicted Ice Thickness")
    plt.xlabel("Longitude"); plt.ylabel("Latitude"); plt.title(title)
    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()

def main():
    outdir = Path(OUTPUTS_DIR)/"maps"; outdir.mkdir(parents=True, exist_ok=True)
    for d in [1,2,3]:
        f = Path(DATA_PROCESSED)/f"pred_day{d}.csv"
        if not f.exists():
            print(f"[maps] missing {f}; run predict first.")
            continue
        df = pd.read_csv(f, parse_dates=["time"])
        day = df['time'].iloc[0].date()
        save_map(df, f"Ice Thickness Forecast — Day +{d} ({day})", outdir/f"day{d}_forecast.jpg")
        print(f"[maps] wrote outputs/maps/day{d}_forecast.jpg")

if __name__ == "__main__":
    main()
