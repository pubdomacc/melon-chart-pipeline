# 2025-12-15
# Have to check what are the validators for

REQUIRED_FIELDS = [
	"track_id",
	"title",
	"artist",
	"rank",
	"chart_date"
]

def is_valid(item: dict) -> bool :
	"""
	Basic schema validation
	"""
	return all(item.get(field) is not None for field in REQUIRED_FIELDS)

	