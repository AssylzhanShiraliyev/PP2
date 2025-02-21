# Python date

import datetime

# 1. Write a Python program to subtract five days from current date.

Current = datetime.datetime.today()

New = Current - datetime.timedelta(days=5)

print("New date:", New.strftime("%d.%m.%Y"))