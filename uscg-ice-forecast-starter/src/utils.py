import pandas as pd
import numpy as np

def pick(df, candidates, new_name):
    for c in candidates:
        if c in df.columns:
            df[new_name] = df[c]
            return df
    df[new_name] = np.nan
    return df

def standardize_core(df, colmap):
    df.columns = [c.strip().lower() for c in df.columns]
    df = pick(df, colmap["lat"], "lat")
    df = pick(df, colmap["lon"], "lon")
    df = pick(df, colmap["time"], "time")
    return df

def finalize_numeric(df):
    for c in ["lat","lon"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    if "time" in df.columns:
        df["time"] = pd.to_datetime(df["time"], errors="coerce")
    return df
