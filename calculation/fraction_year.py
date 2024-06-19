import math

class FractionYear:
    def __init__(self, is_leap_year: bool = False) -> None:
        # Normal year
        self.__total_days: int = 365

        # Case if it's a leap year
        if is_leap_year:
            self.__total_days: int = 366

    def __calculate_pi_year(self) -> float:
        return (2 * math.pi) / self.__total_days

    def __calculate_hours(self, hour: int, day_of_year: int) -> float:
        return (day_of_year - 1 + ((hour - 12) / 24))

    def fraction_year(self, day_of_year: int, hour: int) -> float:
        """
        #### The fraction year is calculated in radians. 
        This is required so we can estimate the equation of time in minutes and the solar declination


        first we calculate the year by using pi (2π / total_days_in_a_year), 
        so either 365 or 366 depending on the year

        Then we actually calculate it by using the current hour and day of year

        Finally multiply the year and the hours and geet the fraction year
        """
        return self.__calculate_pi_year() * self.__calculate_hours(hour, day_of_year)

    