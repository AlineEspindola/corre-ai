class Main:
    pass


print("teste")

from datetime import datetime
from Runner import Runner
from Filters import Filters
from Race import Race

runner1 = Runner(
    id=1,
    name="Thiago",
    email="thiago@example.com",
    password="123456",
    image=None,
    status="active",
    deleted_at=datetime(2025, 7, 15, 14, 30),
)

filters1 = Filters(
    id=1,
    state="Santa Catarina",
    city="Garopaba",
    distance=10,
    status="active",
    deleted_at=datetime,
)

race1 = Race(
    id=1,
    name="Corrida da Esperança",
    date=datetime(2025, 7, 15, 14, 30),
    link_image="url",
    state="Santa Catarina",
    city="Garopaba",
    status="active",
    deleted_at=None
)

