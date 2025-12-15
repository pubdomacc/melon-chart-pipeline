from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseFetcher(ABC):
	@abstractmethod
	def get_daily_chart(self) -> List[Dict[str,Any]]:
		"""
		Return raw chart data as a list of dictionaries.
		The raw shape should match what an external API would return
		"""
		raise NotImplementedError
