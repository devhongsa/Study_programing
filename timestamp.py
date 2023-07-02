from datetime import datetime, timedelta
import time

# unix time
now=time.time() 
nowts = datetime.now().timestamp()

print(nowts)

# date 
nowdt = datetime.now()

delta = nowdt - timedelta(days=60)

deltadate = delta - nowdt
print(deltadate.days)
if deltadate == 60:
    print(nowdt - delta)
    
# datetime to timestamp
datetime.timestamp(nowdt)   

# timestamp to datetime
now_date=datetime.fromtimestamp(now)  


print(datetime.timestamp(nowdt)) 
print(datetime.timestamp(delta))

nowd=now_date-timedelta(minutes=1)  #timedelta

nowd_unix=datetime.timestamp(nowd)


date_string='2020-12-15'
date_string2='2021-01-28 21:16:00'

# str을 datetime 으로
date=datetime.strptime(date_string,'%Y-%m-%d')     

# datetime to str
datetimeStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%L")  


print(date)

date2=datetime.strptime(date_string2,'%Y-%m-%d %H:%M:%S')

timestamp=datetime.timestamp(date)   #datetime을 unixtime 으로 
timestamp2=datetime.timestamp(date2)

'''
print(int(timestamp*1000))
print(timestamp2)
print((date2-date).days)
'''

start=time.strftime("%Y-%m-%d")
print(start)

delta=timedelta(minutes=1)

#print(time.strftime("%Y-%m-%d %H:%M:%S"))  # datetime을 str 으로


timestamp=1646133708

date3=datetime.fromtimestamp(timestamp)  #unixtime 을 datetime 으로
print(date3)

print(date)

print((date2-date))

a = 44*24*60 + 4*60 + 15

print(a)