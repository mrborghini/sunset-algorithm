import math


class SolarTime:
    def __init__(self, equation_of_time: float, solar_declination_angle: float, latitude: float, longitude: float, timezone: int, hour: int, minute: int, second: int) -> None:
        """
        We need to calculate the true solar time. The timezone, latitude, longitude, current time (hour, minute and second), 
        estimate the equation of time (in minutes) and solar declination angle is required for this
        """
        self.__eqtime = equation_of_time
        self.__decl = solar_declination_angle
        self.__timezone = timezone
        self.__latitude = latitude
        self.__longitude = longitude
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    
    def time_offset(self) -> float:
        """
        Calculate the time offset with the equation of time and longitude and timezone
        """
        return self.__eqtime + 4 * self.__longitude - 60 * self.__timezone

    def true_solar_time(self, time_offset: float) -> float:
        """
        Calculate the true solar time based on the time, hour and second given
        """
        return self.__hour * 3600 + self.__minute * 60 + self.__second + time_offset
    

    def solar_hour_degree(self, true_solar_time: float) -> float:
        """
        Calculate the solar hour in degrees
        """
        return (true_solar_time / 4) / 180
    
    def cos_solar_zenith_angle(self, solar_hour_degree: float):
        """
        Calculate the solar_zenith_angle in cos(solar_zenith_angle)
        """
        return math.sin(self.__latitude) * math.sin(self.__decl) + math.cos(self.__latitude) * math.cos(self.__decl) * math.cos(solar_hour_degree)
    
    def solar_azimuth(self):
        pass