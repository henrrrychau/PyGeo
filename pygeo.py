from numpy import *

class time_processer:              #Process the time and 
    #y,m,d,h,min,
    # Tnow:local time
    # Tsp:The vernal equinox time
    def __init__(self,y:int,m:int,d:int,h:int,min:int):
        if y>=0 and 1<=m<=12 and 1<=d<=30 and 0<=h<24 and 0<=min<60:
            self.y=y
            self.m=m
            self.d=d
            self.h=h 
            self.min=min
    
    @staticmethod
    def Tnow2Decimal(self):    #Turn the current time(h-m) into decimal.
        min60=self.min/60
        return self.h+min60
    
    @staticmethod
    def ymd2D(self):        #Count the days from 1st Jan. to certain m-d in certain year.
        if is_leapyear(self.y):
            feb=29
        else:
            feb=28
        months=[31,feb,31,30,31,30,31,31,30,31,30,31]
        if self.m==1:
            return self.d       #January is needed to be processed individually.
        else:
            index = self.m-1
            sum=0
            for index in range(0,index):
                sum+=months[index]
            return sum+self.d           #The sum equals to the count of days during months-1 plus the submitted days

    @staticmethod
    def retTsp(self):
        if is_leapyear(self.y):
            return 81 
        else:
            return 80

#********************************************************************************
def s_by_D(D:int,Tsp:int):          #Tsp: The count of the days from Jan.1 to the vernal equinox.
    return rad2deg(arcsin(sin(deg2rad(23.43)) * sin(((D-Tsp) / 365.2422) * 2*pi)))

def is_leapyear(y:int):     #Check if the year is leap year
    return True if ((not y%4) and y%100) or (not y%400) else False
def f(sitar:float,s:float,t0:float,h:float):        #Calculate lat.
    t0=deg2rad((t0-12)*(2*180/24))
    sitar=deg2rad(sitar)
    s=deg2rad(s)
    return h*sqrt(1/(cos(sitar)*cos(s)*cos(t0) + sin(sitar)*sin(s))**2 - 1)

#********************************************************************************

class lat_fucker:    #Now the latitude is known and it's time to make something interesting by it.
    #s:Direct solar point
    #lat:Latitude
    def __init__(self,s:float,lat:float): 
        self.s=s
        self.lat=lat
    
    @staticmethod
    def daytime_length(self):       #Calculate the daytime length by direct solar point and lat
        return 24*(1 - ((arccos(tan(deg2rad(self.s)) * tan(deg2rad(self.lat)))) / pi))

    @staticmethod
    def Tsr(self):                 #Calculate the sunrise time
        return (12 * arccos(tan(deg2rad(self.s)) * tan(deg2rad(self.lat)))) / pi

    @staticmethod
    def sunrise_by_lat(self):      #The time of sunrise calculated through latitude
        return abs( (12 * arccos(tan(deg2rad(self.s)) * tan(deg2rad(self.lat)))) / pi )

    @staticmethod
    def daytime_by_lat(self):      #The daytime length calculated through latitude
        return 24*(1-(arccos(tan(rad2deg(self.s))*tan(rad2deg(self.lat))))/pi)

class lat_long_hacker:    #The latitude is still unknown. Let's calculate it out and do something further.
    #s:Direct solar point
    #Tnow:local time (DECIMAL FORM!!!!!!)
    #stdtz_long:The longitude of a standard time zone.  (DEGREE FORM!!!!!)
    #stdtz_time:The time of the standard time zone (DECIMAL FORM!!!!!).
    #l:Length of the stick shadow
    #H:Height of the stick
    def __init__(self,s:float,Tnow:float,stdtz_long:float,stdtz_time:float,H:float,l:float):
        self.s=s
        self.stdtz_time=stdtz_time
        self.stdtz_long=stdtz_long
        self.Tnow=Tnow 
        self.H=H
        self.l=l

    @staticmethod
    def shadow2lat(self):   #Calculate the latitude with the shadow length.
        l=-90
        r=90
        while True:
            m=(l+r) / 2
            if f(m,self.s,self.Tnow,self.H)>self.l and m-l>0.00000001:
                r=m
                continue
            if f(m,self.s,self.Tnow,self.H)<self.l and r-m>0.00000001:
                l=m
                continue
            break
        return m
        
    @staticmethod
    def tnow2long(self):        #Turn local time into longitude
        return self.stdtz_long + 15 * (self.Tnow - self.stdtz_time)

def printd(sth:str):    #A debug function which would print something and then exit.
    print(sth)
    exit(0)

if __name__ == "__main__":
#"stdtz_time" is the time of the timezone where your position locates.
#"Tnow" stands for the local time of your position
# (Local time and timezone time is different, which means that the former one is calculated out by measuring
# the shadow length, as "l", and the real length of stick, as "H", and the latter one is known by checking the 
# current timezone where the position locates.)
    print("The string below stands for year-month-day-hour(localtime)-minutes(localtime)-hour(timezonetime)-minutes(timezonetime)\n********************************************************************************")
    tstring=input("Please enter y-m-d-hr-min-hr(timezone_time)-min(timezone_time)-timezone_latitude:")
    timearray=tstring.rsplit("-")
    stkinfo=input("Please enter stick length and shadow length in \"stick_l-shadow_l\" format ")     #Some information of the stick including shadow length and real length.
    stkinfo=stkinfo.split("-")
#********************************************************************************************
    if len(timearray)!=8:
        print(len(timearray))
        print("Oops!Something has been absent with the date information!")
        exit(-1)
    if len(stkinfo)!=2:
        print(len(stkinfo))
        print("Oops!Something has been absent with the stick information!")
        exit(-2)
    y=float(timearray[0])
    m=float(timearray[1])
    d=float(timearray[2])
    hr=float(timearray[3])
    min=float(timearray[4])
    hr0=float(timearray[5])
    min0=float(timearray[6])
    tz_lat=float(timearray[7])
#***********************
    stk_l=float(stkinfo[0])
    shdw_l=float(stkinfo[1])
#********************************************************************************************
    t=time_processer(y,m,d,hr,min) 
    Tnow=t.Tnow2Decimal(t)
    D=t.ymd2D(t)
    Tsp=t.retTsp(t)
    s=s_by_D(D,Tsp)
    stdtz_time=time_processer(y,m,d,hr0,min0)
    stdtz_time=stdtz_time.Tnow2Decimal(stdtz_time)
    llh=lat_long_hacker(s,Tnow,tz_lat,stdtz_time,stk_l,shdw_l)
    print('Tnow='+str(Tnow))
    print('Tsp='+str(Tsp))
    print('s='+str(s))
    print('D='+str(D))
    print('lat='+str(llh.shadow2lat(llh)))
    print('long='+str(llh.tnow2long(llh)))