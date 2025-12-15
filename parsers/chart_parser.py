# 2025-12-15
# Question for this block : def functionName(input : type) -> (type)
# not sure abt the format as above



def normalize_track(track: dict) -> dict:

	"""
	Convert raw track dict into a normalized schema
	"""

	return {

		"track_id": track.get("songId"),
		"title": track.get("songName"),
		"artist": track.get("artistName"),
		"album": track.get("albumName"),
		"rank": int(track.get("rank")),
		"chart_date": track.get("chartDate"),
		"source": "dummy"
	}