import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="USCG Ice Forecast", layout="wide")
st.title("USCG Great Lakes — 3‑Day Ice Forecast")

preds_path = Path("../data/processed/predictions_all.csv")
if preds_path.exists():
    df = pd.read_csv(preds_path, parse_dates=["time"])
    day = st.selectbox("Select forecast day", sorted(df["time"].dt.date.unique()))
    ddf = df[df["time"].dt.date == day]
    st.map(ddf.rename(columns={"lat":"latitude","lon":"longitude"}))
    st.dataframe(ddf.head())
else:
    st.info("Run the pipeline (make all) to generate predictions, then reload.")
