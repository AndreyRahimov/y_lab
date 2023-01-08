"""У каждого фильма есть расписание, по каким дням он идёт в кинотеатрах. Для
эффективности дни проката хранятся периодами дат. Например, прокат фильма
проходит с 1 по 7 января, а потом показ возобновляется с 15 января по 7
февраля:

[
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
]

Вам дан class Movie. Реализуйте у него метод schedule. Он будет генерировать
дни, в которые показывают фильм.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        period_amount = len(self.dates)
        period = 0
        while period <= period_amount - 1:
            first_date, last_date = self.dates[period]
            date = first_date - timedelta(days=1)
            while date < last_date:
                date += timedelta(days=1)
                yield date
            period += 1


m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)
