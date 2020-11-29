#logic
x =2
print(1 < x < 5)
print(bool(11))
#####
x, y, z = 1, 0, 1
print(x and y)
print(x or y)
print(not z)
print(x and y or z)
#####
year =2012
is_leap = year %4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_leap)
#####
import calendar
print(calendar.isleap(1988))
#####