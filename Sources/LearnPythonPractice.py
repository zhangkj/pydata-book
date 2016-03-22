#-*-encoding:utf-8-*-


#计算闰年函数
def LeapYear(year):
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        return  True
    else:
        return  False

print LeapYear(2015)