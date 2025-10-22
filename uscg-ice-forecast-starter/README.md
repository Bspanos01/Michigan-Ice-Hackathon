# USCG Great Lakes Ice Forecast — Starter Kit

Turn‑key pipeline for the Coast Guard hackathon (today + 3 day ice forecast).

## Structure
```
uscg-ice-forecast-starter/
├─ app/                      # Streamlit demo dashboard
├─ data/
│  ├─ raw/
│  │  ├─ Ice_Data/
│  │  ├─ Water_Surface_Temperature/
│  │  └─ Weather_Data/
│  ├─ interim/
│  └─ processed/
├─ models/                   # saved model.pkl
├─ outputs/
│  ├─ maps/                  # exported JPG/HTML maps
│  └─ figures/
├─ report/
├─ scripts/
├─ src/                      # pipeline code
├─ .env.example
├─ .gitignore
├─ Makefile
├─ requirements.txt
└─ README.md
```

## Quickstart
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

cp .env.example .env
# Put provided data into data/raw/ in the three folders shown above.

make all            # run entire pipeline
make app            # launch Streamlit demo
```
