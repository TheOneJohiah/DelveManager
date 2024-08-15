""" Various classes for handling time aspects """

from datetime import datetime

class Time:
    """ Class containing time constants """
    # Constants needed for time shtuff
    # second =60> minute =60> hour =24> day =8> week =4> month =11> year
    SECOND_LEN = 1000
    MINUTE_LEN = SECOND_LEN * 60
    HOUR_LEN = MINUTE_LEN * 60
    DAY_LEN = HOUR_LEN * 24
    WEEK_LEN = DAY_LEN * 8
    MONTH_LEN = WEEK_LEN * 4
    YEAR_LEN = MONTH_LEN * 11

    the_time = None

    def __init__(self, val = None):
        if isinstance(val, str):
            # Handle string
            # This may have some issues with the last bit
            # as %f is supposed to be for microseconds but it should work :)
            # example string 0936-06-03-12:00:00:000
            self.the_time = datetime.strptime(val, "%Y-%m-%d-%H:%M:%S:%f")
        elif isinstance(val, int):
            # Handle integer
            self.the_time = datetime(0, 0, 0) # empty date

            # I have no idea what is being done here but
            # lets just do it
            self.the_time.year = int(val / self.YEAR_LEN)
            val -= self.the_time.year * self.YEAR_LEN
            self.the_time.month = int(val / self.MONTH_LEN)
            val -= self.the_time.month * self.MONTH_LEN
            self.the_time.month += 1
            self.the_time.day = int(val / self.DAY_LEN)
            val -= self.the_time.day * self.DAY_LEN
            self.the_time.day += 1
            self.the_time.hour = int(val / self.HOUR_LEN)
            val -= self.the_time.hour * self.HOUR_LEN
            self.the_time.minute = int(val / self.MINUTE_LEN)
            val -= self.the_time.minute * self.MINUTE_LEN
            self.the_time.second = int(val / self.SECOND_LEN)
            val -= self.the_time.second * self.SECOND_LEN
            self.the_time.microsecond = val

    # ? why is this called path
    def path(self):
        """ Get the time as a string """
        return self.the_time.strftime("%Y-%m-%d-%H:%M:%S:%f")

    def absolute(self):
        """ Get some homegrown version of a unix timestamp """
        return (self.the_time.year * self.YEAR_LEN + \
                self.the_time.month * self.MONTH_LEN + \
                self.the_time.day * self.DAY_LEN + \
                self.the_time.hour * self.HOUR_LEN + \
                self.the_time.minute * self.MINUTE_LEN + \
                self.the_time.second * self.SECOND_LEN + \
                self.the_time.microsecond - (self.DAY_LEN + self.MONTH_LEN))

    def datetime(self):
        """ Get the time and date as a string with a nicer format """
        suffix = ""
        timestamp = ""
        event = ""

        # thanks google
        if 4 <= self.the_time.day <= 20 or 24 <= self.the_time.day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][self.the_time.day % 10 - 1]

        timestamp = self.the_time.strftime("%H:%M")
        event = ["Promise(01)",
                 "Expectation(02)",
                 "Sowing(03)",
                 "Seedlings(04)",
                 "Light(05)",
                 "First Harvest(06)",
                 "Second Harvest(07)",
                 "Frostfall(08)",
                 "Winternight(09)",
                 "Fallow(10)",
                 "Breaking(11)"][self.the_time.month - 1]


        return " ".join([timestamp,
                         str(self.the_time.day) + suffix,
                         event,
                         str(self.the_time.year)
                         ])

class Moment(Time):
    """ A singular moment, or that is to say date/time """

    def to(self, _next):
        """ Converts to an Inverval """
        return Interval(self, _next)

    def add(self, change):
        """ Add two together """
        if isinstance(change, Moment):
            return Moment(self.absolute() + change.absolute())

        return None

class Duration(Time):
    """ A time duration """
    def in_seconds(self):
        """ Get in seconds """
        return self.absolute() / self.SECOND_LEN
    def in_minutes(self):
        """ Get in minutes """
        return self.absolute() / self.MINUTE_LEN
    def in_hours(self):
        """ Get in hours """
        return self.absolute() / self.HOUR_LEN
    def in_days(self):
        """ Get in days """
        return self.absolute() / self.DAY_LEN
    def in_weeks(self):
        """ Get in weeks """
        return self.absolute() / self.WEEK_LEN
    def in_months(self):
        """ Get in months """
        return self.absolute() / self.MONTH_LEN
    def in_years(self):
        """ Get in years """
        return self.absolute() / self.YEAR_LEN

class Interval:
    """ A time interval """
    def __init__(self,start,end):
        self.start = Moment(start)
        self.end = Moment(end)
        self.length = Duration(abs(end.absolute() - start.absolute()))

    def from_start_dur(self, start,dur):
        return Interval(start,Moment(start.absolute() + dur.absolute()))
    def from_end_dur(self,end,dur):
        return Interval(Moment(end.absolute() - dur.absolute()),end)
