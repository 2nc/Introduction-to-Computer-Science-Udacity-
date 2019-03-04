# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def is_leap_year(year):
    if year % 400 == 0:
        return True
    else:
        if year % 100 != 0:
            if year % 4 == 0:
                return True
    return False

def convert_to_day(year,month,day):
    day_convert = 0
    if month > 1:
        day_convert = day_convert + 31
    if month > 2:
        if is_leap_year(year):
            day_convert = day_convert + 29
        else:
            day_convert = day_convert + 28
    if month > 3:
        day_convert = day_convert + 31
    if month > 4:
        day_convert = day_convert + 30
    if month > 5:
        day_convert = day_convert + 31
    if month > 6: 
        day_convert = day_convert + 30
    if month > 7:
        day_convert = day_convert + 31
    if month > 8:
        day_convert = day_convert + 31
    if month > 9:
        day_convert = day_convert + 30
    if month > 10:
        day_convert = day_convert + 31
    if month > 11:
        day_convert = day_convert + 30
    day_convert = day_convert + day - 1
    return day_convert

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    day_total = 0
    year = year1
    while year < year2:
        if is_leap_year(year):
            day_total = day_total + 366
        else:
            day_total = day_total + 365
        year = year + 1
    day_total = day_total + convert_to_day(year2,month2,day2) - convert_to_day(year1,month1,day1)
    return day_total
    ##


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
