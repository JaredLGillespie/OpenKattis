# https://open.kattis.com/problems/datum

import datetime

weeks = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
d, m = map(int, input().split())
print(weeks[datetime.date(2009, m, d).weekday()])
