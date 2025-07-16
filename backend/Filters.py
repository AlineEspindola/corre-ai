from datetime import datetime
from typing import Optional

class Filters:
    def __init__(
        self,
        id: int,
        state: str,
        city: str,
        distance: int,
        status: str,
        deleted_at: Optional[datetime],
    ):
        self.id = id
        self.state = state
        self.city = city
        self.distance = distance
        self.status = status
        self.deleted_at = deleted_at

    def decrease_distance(self, distance):
      self.distance -= distance