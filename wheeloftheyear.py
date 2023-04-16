import datetime
import calendar
from astral.moon import phase

date = datetime.datetime.now()
month = date.strftime("%B")
year = date.strftime("%Y")
moonphase = phase(date)
print(moonphase)

print(calendar.calendar(int(year)))
# print(calendar.calendar(year))