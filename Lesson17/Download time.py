# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).


def download_time(file_size,file_unit,bandwidth,band_unit):
    unit = ['kb','kB','Mb','MB','Gb','GB','Tb','TB']
    tran = [2 ** 10, 2 ** 10 * 8,2 ** 20, 2 ** 20 * 8,2 ** 30, 2 ** 30 * 8,2 ** 40, 2 ** 40 * 8]
    i = 0
    file = 0
    band = 0
    while i < len(unit):
        if file_unit == unit[i]:
            file = tran[i] * file_size
        if band_unit == unit[i]:
            band = tran[i] * bandwidth
        i = i + 1
    time = file * 1.0 / band
    hour = (int)(time / 3600)
    minute = (int)(time % 3600 / 60)
    second = time % 3600 % 60
    str1 = ""
    if hour == 1:
        str1 = str1 + str(hour) + " hour, "
    else:
        str1 = str1 + str(hour) + " hours, "
    if minute == 1:
        str1 = str1 + str(minute) + " minute, "
    else:
        str1 = str1 + str(minute) + " minutes, "
    if second == 1:
        str1 = str1 + str(second) + " second"
    else:
        str1 = str1 + str(second) + " seconds"
    return str1


print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')

