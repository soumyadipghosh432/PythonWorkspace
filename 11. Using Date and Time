################## Using Date and Time #################

# Modules : Date, Datetime, Calender


import time

print(time.gmtime(0)) # time at UTC in named struct format after 0 seconds from epoch i.e. 1st jan 1970
print(time.localtime()) # time at local timezone in named struct format
print(time.localtime(6000)) # time at local timezone in named struct format after 6000 seconds from epoch
print(time.time()) # count of seconds since epoch 
print(time.localtime(time.time())) # time at local timezone in named struct format till the seconds upto now from epoch

print("=" * 10)
# Date and Time formats. More on python.org documentation
print(time.strftime('%X', time.localtime(time.time()))) # Time in more readable format HH24:MI:SS
print(time.strftime('%H', time.localtime(time.time()))) # Time in more readable format only the hour segment in HH24 format
print(time.strftime('%M', time.localtime(time.time()))) # Time in more readable format only the minute segment
print(time.strftime('%S', time.localtime(time.time()))) # Time in more readable format only the second segment
print(time.strftime('%Y', time.localtime(time.time()))) # Time in more readable format only the year segment in full 4 characters
print(time.strftime('%y', time.localtime(time.time()))) # Time in more readable format only the year segment in trailing 2 characters
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print("=" * 10)

# Get parts of the time tuple
time_now = time.localtime()
print("Year : " , time_now[0])
print("Month : " , time_now[1])
print("Day : " , time_now[2])
#### OR ####
print("Year : " , time_now.tm_year)
print("Month : " , time_now.tm_mon)
print("Day : " , time_now.tm_mday)

# All parts
for parts in time_now:
    print(parts)


print("=" * 10)
### Use the time operations for capturing time different points

from time import time as timer

input("Press any key to start..")
start_time = time.time()

input("Press any key to end..")
end_time = timer() #same as time.time() as alias defined in import for same

print("Started at : "+ time.strftime("%X", time.localtime(start_time)))
print("Finished at : "+ time.strftime("%X", time.localtime(end_time)))
print("Reaction time : {} seconds".format(end_time - start_time))


print("=" * 10)
### Measuring the performance with performance counter and monotonic with compare to normal method
# time.time() is depending on system clock. if system clock is set in between then the actual difference will be lost
# perf_counter, monotonic calculates elapsed time rather than sync with system clock
# process_time works with the actual time that CPU uses for a process. not the time that we capture in system

from time import perf_counter as my_timer
from time import time as timer
from time import monotonic as mon_timer
from time import process_time as cpu_timer

input("Press enter to start...")
start_time = timer()
perf_start = my_timer()
mon_start = mon_timer()
cpu_start = cpu_timer()

input("Press enter again to end...")
end_time = timer()
perf_end = my_timer()
mon_end = mon_timer()
cpu_end = cpu_timer()


print("Started at : "+ time.strftime("%X", time.localtime(start_time)))
print("Finished at : "+ time.strftime("%X", time.localtime(end_time)))
print("Reaction time : {} seconds".format(end_time - start_time))

print("Perf Started at : "+ time.strftime("%X", time.localtime(perf_start)))
print("Perf Finished at : "+ time.strftime("%X", time.localtime(perf_end)))
print("Perf Reaction time : {} seconds".format(perf_end - perf_start))

print("Monotonic Started at : "+ time.strftime("%X", time.localtime(mon_start)))
print("Monotonic Finished at : "+ time.strftime("%X", time.localtime(mon_end)))
print("Monotonic Reaction time : {} seconds".format(mon_end - mon_start))

print("Process Started at : "+ time.strftime("%X", time.localtime(cpu_start)))
print("Process Finished at : "+ time.strftime("%X", time.localtime(cpu_end)))
print("Process Reaction time : {} seconds".format(cpu_end - cpu_start))

print("=" * 10)
#### Measuring different clocks can be done with get_clock_info() at once..
#### This code demonstrates wayout to different clocks but in more pythonic way

import time

print("time()\t\t\t:  ", time.get_clock_info('time'))
print("perf_counter()\t\t:  ", time.get_clock_info('perf_counter'))
print("monotonic()\t\t:  ", time.get_clock_info('monotonic'))
print("process_time()\t\t:  ", time.get_clock_info('process_time'))

print("=" * 10)
################ Using timezone #################

import time

print("Timezone details : ", time.tzname)
print("Current Timezone : ", time.tzname[0])
print("Offset from UTC : ", time.timezone)

if time.daylight != 0:
    print("Daylight Saving Time (DST) is in effect for this location")
    print("DST Time is : ", time.tzname[1])
else:
    print("DST not applicable")



################ Using Datetime ###################

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
