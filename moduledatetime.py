import datetime

'''
now = datetime.datetime.today().strftime("%B, %d, %Y, %H:%M PM")
print(now)
'''

year = int(input('Type down your birthday year: '))
month = int(input('Type down your birthday month: '))
day = int(input('Type down your birthday day: '))

today = datetime.datetime.today()
birthday = datetime.datetime(year, month, day)
days_past = today - birthday
real_days_past = days_past.days

print(str(real_days_past) + ' days past since your birth')