class Time:
    def __init__ (self, h, m, s): #constructor for time object
        self.__hours = h
        self.__mins = m
        self.__secs = s

    def getHours(self): #3 accessor methods
        return self.__hours
    def getMins(self):
        return self.__mins
    def getSecs(self):
        return self.__secs

    def toString(self):
        h = str(self.getHours())
        m = str(self.getMins())
        s = str(self.getSecs())
        return h + ":" + m + ":" + s

    def timeInSeconds(self):
        return self.getSecs()+60*self.getMins()+3600*self.getMins()

    def changeTheTime(self, h, m, s):
        self.__secs += s
        self.__mins += m
        self.__hours += h
        if self.__secs >= 60: # if there are 60 or more seconds, convert extra to mins
            self.__mins += self.__secs//60
            self.__secs %= 60
        if self.__mins >= 60: # if there are 60 or more mins, convert extra to hours
            self.__hours += self.__mins//60
            self.__mins %= 60

    def twelveHourClock(self):
        if self.__hours < 12: #it is am
            return str(self.toString(), "am")
        else: #self.__hours >= 12 (it is pm)
            t = Time(self.__hours-12, self.__mins, self.__secs)
            return str(t.toString(), "pm")

    def whatTimeIsIt(self):
        if 6 <= self.__hours < 12: #between 6am and 12pm --> morning
            return "morning"
        if 12 <= self.__hours < 17: #between 12pm and 5pm --> afternoon
            return "afternoon"
        if 17 <= self.__hours < 22: #between 5pm and 10pm --> evening
            return "evening"
        if 22 <= self.__hours or self.__hours < 6: #between 10pm and 6am --> nighttime
            return "nighttime"

    def compareTo(self, t):
        return self.timeInSeconds() - t.timeInSeconds()

    def timeTill(self, t): #for timeTill, t is always in the future (after self)
        dif = self.compareTo(t)
        return Time(dif//3600, (dif % 3600)//60, dif % 60)
