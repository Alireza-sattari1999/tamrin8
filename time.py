class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour

        self.minute = minute

        self.second = second
        self.true()

    def print(self):

        print(self.hour, ':', self.minute, ':', self.second)

    def true(self):

        if self.second >= 60 or self.second < 0:

            minute = self.second // 60

            mod = self.second % 60
            
            self.minute += minute

            self.second = mod

        if self.minute >= 60 or self.minute < 0:

            hour = self.minute // 60 

            mod_hour = self.minute % 60
            self.hour += hour
            self.minute = mod_hour
        return self

    def add(self, other):

        hour = self.hour + other.hour

        minute = self.minute + other.minute

        second = self.second + other.second

        return Time(hour,minute,second).true()

    def sub(self, other):
        hour = self.hour - other.hour

        minute = self.minute - other.minute

        second = self.second - other.second

        return Time(hour,minute,second).true()

    def toSeconds(self):

        return self.second + (self.minute * 60) + (self.hour * 3600)

    def fromSeconds(self, second):

        h = second // 3600

        second %= 3600

        minute = second // 60

        second %= 60

        self.hour = hour

        self.minute = minute

        self.second = second
        return self
while True:
    print("welcome😎")
    hour1=input('hour1 is=')

    minute1=input('minute1 is=')

    second1=input('second1 is=')

    hour2=input('hour2 is=')

    minute2=input('minute2=')

    second2=input('second2=')
    time1 = Time(int(hour1),int(minute1),int(second1))

    time2 = Time(int(hour2),int(minute2),int(second2))
    

    print('time1 + time2 = ')

    time1.add(time2).print()

    print('time1 - time2 = ')

    time1.sub(time2).print()

    print('\ntime 1  tabdil be sanie  = ',time1.toSeconds())

    print('time 2 tabdil be sanie = ',time2.toSeconds())

    print("have a good time!")


    second = input('\nenter second : ')

    print(second, ' change to  time is ')

    t = Time()

    t.fromSeconds(int(second)).print()

  

    