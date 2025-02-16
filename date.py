from datetime import datetime, timedelta

print((datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d"))

# esep 2

from datetime import datetime, timedelta

print((datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"))
print((datetime.now()).strftime("%Y-%m-%d"))
print((datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"))

#esep 3

from datetime import datetime

now = datetime.now().replace(microsecond=0)
print(now)

# esep 4

from datetime import datetime

d1 = input("input YYYY-MM-DD: ")
d2 = input('input YYYY-MM-DD: ')

date1 = datetime.strptime(d1,'%Y-%m-%d')
date2 = datetime.strptime(d2,'%Y-%m-%d')

date3 = (date2-date1).total_seconds()
print(date3)