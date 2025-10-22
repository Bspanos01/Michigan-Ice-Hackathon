"""Ingest raw CSV/NetCDF into tidy CSVs in data/interim."""
import glob
from pathlib import Path
import pandas as pd
import xarray as xr
from .config import DATA_RAW, DATA_INTERIM, COLS
from .utils import standardize_core, finalize_numeric

def ingest(subdir, tag):
    raw_dir = Path(DATA_RAW) / subdir
    out_dir = Path(DATA_INTERIM); out_dir.mkdir(parents=True, exist_ok=True)
    frames = []
    for f in glob.glob(str(raw_dir / "**/*"), recursive=True):
        if f.endswith(".csv"):
            df = pd.read_csv(f)
        elif f.endswith(".nc"):
            ds = xr.open_dataset(f)
            df = ds.to_dataframe().reset_index()
        else:
            continue
        df = standardize_core(df, COLS)
        df = finalize_numeric(df)
        df["source_tag"] = tag
        frames.append(df)
    if frames:
        out = pd.concat(frames, ignore_index=True).dropna(subset=["lat","lon","time"])
        out.to_csv(out_dir / f"{tag}.csv", index=False)
        print(f"[ingest] wrote {tag}.csv — {len(out):,} rows")
    else:
        print(f"[ingest] no files in {raw_dir}")

def main():
    ingest("Ice_Data","ice")
    ingest("Water_Surface_Temperature","wst")
    ingest("Weather_Data","wx")

if __name__ == "__main__":
    main()
