# Python date

import datetime

# 1. Write a Python program to subtract five days from current date.

Current = input("""Enter a date in format "DD.MM.YYYY": """)

Date = datetime.datetime.strptime(Current, "%d.%m.%Y")

New = Date - datetime.timedelta(days=5)

print("New date:", New.strftime("%d.%m.%Y"))

# 2. Write a Python program to print yesterday, today, tomorrow.

Date = input("""Enter a date in format "DD.MM.YYYY": """)

Today = datetime.datetime.strptime(Date, "%d.%m.%Y")

Yesterday = Today - datetime.timedelta(days=1)
Tomorrow = Today + datetime.timedelta(days=1)

print("Yesterday:", Yesterday.strftime("%d.%m.%Y"))
print("Today:", Today.strftime("%d.%m.%Y"))
print("Tomorrow:", Tomorrow.strftime("%d.%m.%Y"))

# 3. Write a Python program to drop microseconds from datetime.

Date = input("""Enter a date in format "DD.MM.YYYY HH:MM:SS": """)

Now = datetime.datetime.strptime(Date, "%d.%m.%Y %H:%M:%S")

Result = Now.replace(microsecond=0)

print("Current datetime without microseconds: ", Result.strftime("%d.%m.%Y %H:%M:%S"))

# 4. Write a Python program to calculate two date difference in seconds.

First = input("""Enter first date in format "DD.MM.YYYY HH:MM:SS": """)
Second = input("""Enter second date in format "DD.MM.YYYY HH:MM:SS": """)

One = datetime.datetime.strptime(First, "%d.%m.%Y %H:%M:%S")
Two = datetime.datetime.strptime(Second, "%d.%m.%Y %H:%M:%S")

Result = abs((Two - One).total_seconds())

print("Difference in seconds:", int(Result))
