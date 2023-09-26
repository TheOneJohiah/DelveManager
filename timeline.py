# second =60> minute =60> hour =24> day =8> week =4> month =11> year

from math import *
class Moment:
    def __init__(self,src=None):
        if type(src) is str:
            date = src.split('-')
            time = date[3].split(":")
            self.year   = int(date[0])
            self.month  = int(date[1])
            self.day    = int(date[2])
            self.hour   = int(time[0])
            self.minute = int(time[1])
            self.second = int(time[2])
            self.milli  = int(time[3])
        elif type(src) is int:
            self.year = int(src/30412800000)
            src -= self.year*30412800000
            #self.year += 1
            self.month = int(src/2764800000)
            src -= self.month*2764800000
            self.month += 1
            self.day = int(src/86400000)
            src -= self.day*86400000
            self.day += 1
            self.hour = int(src/3600000)
            src -= self.hour*3600000
            self.minute = int(src/60000)
            src -= self.minute*60000
            self.second = int(src/1000)
            src -= self.second*1000
            self.milli = src
        elif type(src) is Moment: self = src

    def absolute(self): return (self.year*30412800000 + self.month*2764800000 + self.day*86400000 + self.hour*3600000 + self.minute*60000 + self.second*1000 + self.milli - 2851200000)

    def path(self): return "-".join([str(self.year).rjust(4,"0"), str(self.month).rjust(2,"0"),str(self.day).rjust(2,"0"),":".join([str(self.hour).rjust(2,"0"),str(self.minute).rjust(2,"0"),str(self.second).rjust(2,"0"),str(self.milli).rjust(3,"0")])])

    def to(self,next): return Interval(self,next)

    def plus(self,change): return Moment(self.absolute() + change.absolute())

class Duration:
    def __init__(self,src=None):
        if type(src) is str:
            date = src.split(';')
            time = date[3].split(":")
            self.years   = int(date[0])
            self.months  = int(date[1])
            self.days    = int(date[2])
            self.hours   = int(time[0])
            self.minutes = int(time[1])
            self.seconds = int(time[2])
            self.millis  = int(time[3])
        elif type(src) is int:
            self.years = int(src/30412800000)
            src -= self.years*30412800000
            self.months = int(src/2764800000)
            src -= self.months*2764800000
            self.days = int(src/86400000)
            src -= self.days*86400000
            self.hours = int(src/3600000)
            src -= self.hours*3600000
            self.minutes = int(src/60000)
            src -= self.minutes*60000
            self.seconds = int(src/1000)
            src -= self.seconds*1000
            self.millis = src
        elif type(src) is Moment: self = src

    def absolute(self): return (self.years*30412800000 + self.months*2764800000 + self.days*86400000 + self.hours*3600000 + self.minutes*60000 + self.seconds*1000 + self.millis)

    def path(self): return ";".join([str(self.years).rjust(4,"0"), str(self.months).rjust(2,"0"),str(self.days).rjust(2,"0"),":".join([str(self.hours).rjust(2,"0"),str(self.minutes).rjust(2,"0"),str(self.seconds).rjust(2,"0"),str(self.millis).rjust(3,"0")])])

    def in_seconds(self): return self.absolute()/1000
    def in_minutes(self): return self.absolute()/60000
    def in_hours(self): return self.absolute()/3600000
    def in_days(self): return self.absolute()/86400000
    def in_weeks(self): return self.absolute()/691200000
    def in_months(self): return self.absolute()/2764800000
    def in_years(self): return self.absolute()/30412800000

class Interval:
    def __init__(self,start,end):
        self.start = Moment(start)
        self.end = Moment(end)
        self.length = Duration(abs(end.absolute() - start.absolute()))

    def from_start_dur(start,dur): return Interval(start,Moment(start.absolute() + dur.absolute()))
    def from_end_dur(end,dur): return Interval(Moment(end.absolute() - dur.absolute()),end)