from Counters import Time

class Clock:
    """ 
    Our implementation of the Clock class
    """
    def getTime(self):
        return Time.getTime()

    def setTime(self, timetuple):
        return Time.setTime(timetuple)
        
    def getHour(self):

        """return the current hour as an int """

        timetuple = Time.getTime()
        return timetuple[3]

    def setHour (self, hour):

        """ Sets the RTC Hour to the hour parameter"""
        # first get current time from the system
        timetuple = Time.getTime()
        # convert the tule into a list
        timelist = list(timetuple)
        # change the hour to the new hour
        timelist[3] = hour
        # save it back to the system
        Time.setTime(timelist)

    def getMinute(self):
        
        """ return the current minute as an int"""

        timetuple = Time.getTime()
        return timetuple[4]
    
    def setMinute(self, minute):
        
        """ Sets the RTC Minute to the minute parameter"""
        # first get time from system
        timetuple = Time.getTime()
        #convert tuple to a list
        timelist = list(timetuple)
        #change the minute to new minute
        timelist[4] = minute
        # save it back to the system
        Time.setTime(timelist)

    def getYear(self):
        
        """ return the current year as an int"""

        timetuple = Time.getTime()
        return timetuple[0]
    
    def setYear(self, year):
        
        """ Sets the RTC Year to the year parameter"""
        # first get time from system
        timetuple = Time.getTime()
        #convert tuple to a list
        timelist = list(timetuple)
        #change the year to new year
        timelist[0] = year
        # save it back to the system
        Time.setTime(timelist)

    def getMonth(self):
        
        """ return the current month as an int"""

        timetuple = Time.getTime()
        return timetuple[1]
    
    def setMonth(self, month):
        
        """ Sets the RTC Minute to the minute parameter"""
        # first get time from system
        timetuple = Time.getTime()
        #convert tuple to a list
        timelist = list(timetuple)
        #change the month to new month
        timelist[1] = month
        # save it back to the system
        Time.setTime(timelist)    
    










