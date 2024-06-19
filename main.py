import math
from calculation.fraction_year import FractionYear
from calculation.equation_of_time import EquationOfTime
from calculation.solar_time import SolarTime

def main():
    latitude = 0
    longitude = 0
    hour = 16
    minute = 0
    second = 0
    day_of_year = 117
    
    # Calculate the fraction year in radians
    fraction_of_year = FractionYear()
    y = fraction_of_year.fraction_year(day_of_year, hour)

    # Calculate the equation time and solar declination angle
    equation_of_time = EquationOfTime(y)
    eq_time = equation_of_time.equation_time()
    decl = equation_of_time.solar_declination_angle()

    solar_time = SolarTime(eq_time, decl, latitude, longitude, 2, hour, minute, second)
    time_offset = solar_time.time_offset()
    true_solar_time = solar_time.true_solar_time(time_offset)

    solar_hour_degree = solar_time.solar_hour_degree(true_solar_time)
    zenith_angle = solar_time.cos_solar_zenith_angle(solar_hour_degree)

    print(math.cos(zenith_angle) * (180 / math.pi))
    

if __name__ == "__main__":
    main()