# second =60> minute =60> hour =24> day =8> week =4> month =11> year
seclen = 1000
minlen = seclen*60
hourlen = minlen*60
daylen = hourlen*24
weeklen = daylen*8
monlen = weeklen*4
yearlen = monlen*11

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
            self.year = int(src/yearlen)
            src -= self.year*yearlen
            self.month = int(src/monlen)
            src -= self.month*monlen
            self.month += 1
            self.day = int(src/daylen)
            src -= self.day*daylen
            self.day += 1
            self.hour = int(src/hourlen)
            src -= self.hour*hourlen
            self.minute = int(src/minlen)
            src -= self.minute*minlen
            self.second = int(src/seclen)
            src -= self.second*seclen
            self.milli = src
        elif type(src) is Moment: self = src

    def absolute(self): return (self.year*yearlen + self.month*monlen + self.day*daylen + self.hour*hourlen + self.minute*minlen + self.second*seclen + self.milli - (daylen+monlen))

    def path(self): return "-".join([str(self.year).rjust(4,"0"), str(self.month).rjust(2,"0"),str(self.day).rjust(2,"0"),":".join([str(self.hour).rjust(2,"0"),str(self.minute).rjust(2,"0"),str(self.second).rjust(2,"0"),str(self.milli).rjust(3,"0")])])

    def datetime(self):
        return " ".join([
            ":".join([
                str(self.hour).rjust(2,"0"),
                str(self.minute).rjust(2,"0"),
                #str(self.second).rjust(2,"0"),
                #str(self.milli).rjust(3,"0")
            ]),
            #["AM","PM"][int(self.hour/13)],
            ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th","31st","32nd"][self.day - 1],
            ["Promise(01)", "Expectation(02)","Sowing(03)","Seedlings(04)","Light(05)","First Harvest(06)","Second Harvest(07)","Frostfall(08)","Winternight(09)","Fallow(10)","Breaking(11)"][self.month - 1],
            str(self.year).rjust(4,"0"),
        ])
    
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
            self.years = int(src/yearlen)
            src -= self.years*yearlen
            self.months = int(src/monlen)
            src -= self.months*monlen
            self.days = int(src/daylen)
            src -= self.days*daylen
            self.hours = int(src/hourlen)
            src -= self.hours*hourlen
            self.minutes = int(src/minlen)
            src -= self.minutes*minlen
            self.seconds = int(src/seclen)
            src -= self.seconds*seclen
            self.millis = src
        elif type(src) is Moment: self = src

    def absolute(self): return (self.years*yearlen + self.months*monlen + self.days*daylen + self.hours*hourlen + self.minutes*minlen + self.seconds*seclen + self.millis)

    def path(self): return ";".join([str(self.years).rjust(4,"0"), str(self.months).rjust(2,"0"),str(self.days).rjust(2,"0"),":".join([str(self.hours).rjust(2,"0"),str(self.minutes).rjust(2,"0"),str(self.seconds).rjust(2,"0"),str(self.millis).rjust(3,"0")])])

    def in_seconds(self): return self.absolute()/seclen
    def in_minutes(self): return self.absolute()/minlen
    def in_hours(self): return self.absolute()/hourlen
    def in_days(self): return self.absolute()/daylen
    def in_weeks(self): return self.absolute()/weeklen
    def in_months(self): return self.absolute()/monlen
    def in_years(self): return self.absolute()/yearlen

class Interval:
    def __init__(self,start,end):
        self.start = Moment(start)
        self.end = Moment(end)
        self.length = Duration(abs(end.absolute() - start.absolute()))

    def from_start_dur(start,dur): return Interval(start,Moment(start.absolute() + dur.absolute()))
    def from_end_dur(end,dur): return Interval(Moment(end.absolute() - dur.absolute()),end)