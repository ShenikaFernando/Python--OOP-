import datetime

now = datetime.date(2015, 7, 14)

print(now.year)
print(now.month)
print(now.day)

print(datetime.date.today()) #Today's date

dateOfBirth = datetime.date(1980, 1, 1)

today = datetime.date.today()

print(today - dateOfBirth) #get the age by days