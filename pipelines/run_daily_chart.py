# 2025-12-15

from datetime import date
from fetchers.dummy_fetcher import DummyFetcher
from parsers.chart_parser import normalize_track
from validators.schema import is_valid
from storage.writer import save_raw_json, save_csv

def run():
	today = date.today().isoformat()


	fetcher = DummyFetcher()
	raw_data = fetcher.get_daily_chart()

	save_raw_json(f"data/raw/chart_{today}.json", raw_data)

	processed = []
	for track in raw_data:
		item = normalize_track(track)
		if is_valid(item):
			processed.append(item)

	save_csv(f"data/processed/chart_{today}.csv", processed)
	print("ingested records : ", len(processed))


if __name__ == "__main__":
	run()