import os
from dotenv import load_dotenv
load_dotenv()

DATA_RAW = os.getenv("DATA_RAW", "./data/raw")
DATA_INTERIM = os.getenv("DATA_INTERIM", "./data/interim")
DATA_PROCESSED = os.getenv("DATA_PROCESSED", "./data/processed")
MODELS_DIR = os.getenv("MODELS_DIR", "./models")
OUTPUTS_DIR = os.getenv("OUTPUTS_DIR", "./outputs")

# Column synonyms (edit to match your data headers)
COLS = {
    "lat": ["lat","latitude","y"],
    "lon": ["lon","longitude","x"],
    "time": ["time","date","datetime"],
    "ice_thickness": ["ice_thickness","thickness","ice_thick_cm"],
    "ice_concentration": ["ice_concentration","ice_conc","concentration"],
    "sst": ["sst","sea_surface_temp","water_surface_temperature","wst"],
    "air_temp": ["air_temp","tas","t2m","temp_air"],
    "wind_speed": ["wind_speed","ws","wspd"],
    "wind_dir": ["wind_dir","wd","wdir"]
}

GRID_RES = 0.1  # degrees (~11km)
RANDOM_STATE = 42
