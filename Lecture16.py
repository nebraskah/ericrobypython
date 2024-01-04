"""
Working with dates
"""

import datetime

today = datetime.date.today()
print(today.weekday())
print(today.isoweekday())

create_day = datetime.date(2023, 12, 25)
print(create_day)

new_year = datetime.date(2025, 1 , 1)
days_remaining = new_year - today
print(days_remaining)

my_birthday = datetime.date(2024, 11, 24)
days_remaining = my_birthday - today
print(days_remaining)

today_string = '2024-01-04'
date_obj = datetime.date.fromisoformat(today_string)
print(date_obj)
