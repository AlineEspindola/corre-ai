from datetime import datetime
from typing import Optional

class Race:
    def __init__(
        self,
        id: int,
        name: str,
        date: datetime,
        link_image: str,
        state: str,
        city: str,
        distance: int,
        status: str,
        deleted_at: Optional[datetime],
    ):
        self.id = id
        self.name = name
        self.date = date
        self.link_image = link_image
        self.state = state
        self.city = city
        self.distance = distance
        self.status = status
        self.deleted_at = deleted_at
