STICK A STONE HERE!!HAHHA ;-p
# PyGeo
A Python library for certain geographic calculation written by HinWai

# Abstract
Hey guys! I've finished a python geographic calculation library written in Python.
Actually it's not only a library, but a simple program that could be used to calculate latitude and longtitude roughtly through
given date,time and other information.

# How to use it?
Let's assume that you've got a stick here which is taking bath under the sunshine. There would be shadow of the stick lying behind
the stick. First you've got to get the date and the timezone time. Timezone time is the time you could get from your watch or smartphone. Then  Measure the length of the stick and it's shadow, calculate out the local time which should be turned into decimal form 
and then push them into PyGeo. Local time and timezone time is different, which means that the former one is calculated out by measuring the shadow length, as "l", and the real length of stick, as "H", and the latter one is known by checking the current timezone 
where the position locates. Finally, PyGeo would return a series of numbers like Tnow(Local time),Tsp(The day count of the vernal equ-
inox), s(Direct solar point),D(Days counted from 1st Jan. to the date input),lat(Latitude),long(Longtitude). 

The code was written by a noob and there would be several bugs in it.
BTW,it's my first time to submit open source project on GitHub and wanna stick a stone here.

# Here is the example:


>>The string below stands for year-month-day-hour(localtime)-minutes(localtime)-hour(timezonetime)-minutes(timezonetime)

>>Please enter y-m-d-hr-min-hr(timezone_time)-min(timezone_time)-timezone_latitude:2010-1-17-11-58-12-00-120
>>Please enter stick length and shadow length in "stick_l-shadow_l" format 15.10-21.40
>>Tnow=11.966666666666667
>>Tsp=80
>>s=-20.572760575374385
>>D=17.0
>>lat=34.21809233317617
>>long=119.5

