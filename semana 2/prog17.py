import datetime

dt_str = 'July 20, 2020'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
