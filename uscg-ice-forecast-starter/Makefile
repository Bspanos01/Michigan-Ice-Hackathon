.PHONY: all ingest merge train predict maps clean app

all: ingest merge train predict maps

ingest:
	python -m src.data_ingest

merge:
	python -m src.merge_features

train:
	python -m src.train_model

predict:
	python -m src.predict

maps:
	python -m src.make_maps

app:
	streamlit run app/streamlit_app.py

clean:
	rm -rf data/interim/* data/processed/* models/* outputs/maps/* outputs/figures/*
