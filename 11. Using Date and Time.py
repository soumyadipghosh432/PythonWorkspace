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


############################################### USING PYTZ ################################################
# 1. Install and Configure pip. In windows : Reinstall python, Linux : sudo apt-get install python3-pip
# 2. Install pytz. In Windows from CMD or from Linux from Terminal : pip3 install pytz

import pytz
import datetime

country = "GB"
city = "Europe/Moscow"
city = "Europe/Paris"
city = "Asia/Calcutta"

tz_local = pytz.timezone(country)
tz_local = pytz.timezone(city)

local_time = datetime.datetime.now(tz=tz_local)
print("Local Time in {} is {}".format(city, local_time))

print("==============")
# List all available timezones in pytz
for x in pytz.all_timezones:
    print(x)

print("==============")
# List all available country with country codes
for x in sorted(pytz.country_names):
    print(x, " : " , pytz.country_names[x])

print("==============")
# List of country names with codes and timezones
for x in sorted(pytz.country_names):
    print(x, " : ", pytz.country_names[x], " : ",pytz.country_timezones.get(x))


# Get the current localtime for all timezones
for x in sorted(pytz.country_names):
    print(x, " : ", pytz.country_names[x])
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            local_tz = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=local_tz)
            print("\tTime at {} is : \t\t\t {}".format(local_tz, local_time))
    else:
        print("\ttNo Timezone available for this country")


print("=" * 40)

############## NAIVE AND AWARE DATETIME ##################
import datetime
import pytz

naive_local_time = datetime.datetime.now()
naive_utc_time = datetime.datetime.utcnow()

print("Naive Local Time : ", naive_local_time)
print("Naive UTC Time   : ", naive_utc_time)


aware_local_time = pytz.utc.localize(naive_local_time)
aware_utc_time = pytz.utc.localize(naive_utc_time)

# Both is converted to UTC and timezone will be UTC. Offset will be 0 for both times
print("Aware Local Time : {} at Timezone : {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC Time   : {} at Timezone : {}".format(aware_utc_time, aware_utc_time.tzinfo))

tz = pytz.timezone("GB")
aware_local_time = pytz.utc.localize(naive_utc_time).astimezone() # Convert to current system timezone
aware_local_time = pytz.utc.localize(naive_utc_time).astimezone(tz) # Convert to timezone passed as parameter
print("Aware Local Time : {} at Timezone : {}".format(aware_local_time, aware_local_time.tzinfo))


# Declaraing a time by choice and generating datetime from seconds
# datetime.datetime(year, month, date, hour, minute, second, millisecond)
gap_time = datetime.datetime(1990, 10, 23, 11, 40, 0, 0)
print(gap_time)
print(gap_time.timestamp()) # Number of seconds from epoch till current time in systems timezone

print(datetime.datetime.fromtimestamp(gap_time.timestamp())) # Converts to local datetime without the UTC Offset
print(datetime.datetime.utcfromtimestamp(gap_time.timestamp())) # Converts to UTC datetime without the UTC Offset
print(pytz.utc.localize(datetime.datetime.utcfromtimestamp(gap_time.timestamp()))) # Converts with UTC Offset
print(pytz.utc.localize(datetime.datetime.utcfromtimestamp(gap_time.timestamp())).astimezone(tz)) # Converts with UTC Offset and timezone as parameter
print(pytz.utc.localize(datetime.datetime.utcfromtimestamp(gap_time.timestamp())).astimezone()) # Converts with UTC Offset and timezone as local system

########## PYTZ Program ###########

available_zones = {"1":"Asia/Kolkata", "2":"Europe/London", "3":"Japan", "4":"Zulu"}
print("Enter a choice for Timezone (0 to quit)")
for place in sorted(available_zones):
    print("\t\t{} : {}".format(place, available_zones[place]))


while True:
    choice = input()
    if choice == '0':
        break
    if choice in available_zones.keys():
        tz_display = pytz.timezone(available_zones.get(choice))
        world_time = datetime.datetime.now(tz=tz_display)
        print("The time in {} is : {} , Timezone : {}".format(available_zones.get(choice), world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print("Local time is : {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is : {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
        print()



