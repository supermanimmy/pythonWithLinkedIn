from datetime import date 
from datetime import time
from datetime import datetime

today = date.today()
print(today)

days = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
print("Tomorrow will be " + days[(today.weekday())+1])
print(date.today())
print(datetime.date(datetime.now()))