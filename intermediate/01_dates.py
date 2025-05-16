### dates ###

from datetime import datetime, timezone, time, date, timedelta

print('----- datetime -----')

now = datetime.now()
print(now.hour)
print(now.minute)
print(now.second)
print(now.day)
print(now.year)
print(now.month)

timestamp = now.timestamp()
print(timestamp)

utcnow = datetime.now(timezone.utc)
print(utcnow)

year_2025 = datetime(2025, 1, 1)

def print_date(date: datetime):
    print(date.microsecond)
    print(date.second)
    print(date.hour)
    print(date.day)
    print(date.month)
    print(date.year)
    print(date.timestamp())

print_date(now)
print_date(year_2025)

dif = now - year_2025
print(dif)

print('----- time -----')

current_time = time(3, 0, 59)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print('----- date -----')

current_date = date(2025, 2, 28)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date_today = date.today()
print(current_date_today)

date_diff = current_date - year_2025.date()
print(date_diff)

print('----- timedelta -----')

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
