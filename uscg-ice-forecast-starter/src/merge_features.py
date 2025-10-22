"""Merge interim features into a training matrix keyed by (lat, lon, time)."""
from pathlib import Path
import pandas as pd
from .config import DATA_INTERIM, DATA_PROCESSED

def main():
    p = Path(DATA_INTERIM)
    ice = pd.read_csv(p/"ice.csv") if (p/"ice.csv").exists() else pd.DataFrame()
    wst = pd.read_csv(p/"wst.csv") if (p/"wst.csv").exists() else pd.DataFrame()
    wx  = pd.read_csv(p/"wx.csv")  if (p/"wx.csv").exists() else pd.DataFrame()

    if all(df.empty for df in [ice,wst,wx]):
        print("[merge] nothing to merge — run ingest and ensure data exists.")
        return

    # Select and rename columns if present
    keep_cols = lambda df, extra: [c for c in ["lat","lon","time"]+extra if c in df.columns]
    ice = ice[keep_cols(ice, ["ice_thickness","ice_concentration"])]
    wst = wst[keep_cols(wst, ["sst"])]
    wx  = wx[keep_cols(wx, ["air_temp","wind_speed","wind_dir"])]

    # Merge on (lat, lon, time)
    df = ice
    if not wst.empty: df = df.merge(wst, on=["lat","lon","time"], how="left")
    if not wx.empty:  df = df.merge(wx,  on=["lat","lon","time"], how="left")

    outdir = Path(DATA_PROCESSED); outdir.mkdir(parents=True, exist_ok=True)
    df.to_csv(outdir/"training_matrix.csv", index=False)
    print(f"[merge] wrote training_matrix.csv — {len(df):,} rows")

if __name__ == "__main__":
    main()
