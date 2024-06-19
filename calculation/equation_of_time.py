import math

class EquationOfTime:

    
    def __init__(self, fractional_year: float):
        """
        We need to fractional year in radians
        """
        self.__fractional_year: float = fractional_year

    def equation_time(self) -> float:
        """
        Estimate the equation of time (in minutes)
        """
        # Constants
        A = 229.18
        B = 0.000075
        C = 0.001868
        D = -0.032077
        E = -0.014615
        F = -0.040849
        return (A * (B + C * math.cos(self.__fractional_year) + D * math.sin(self.__fractional_year) +
                     E * math.cos(2 * self.__fractional_year) + F * math.sin(2 * self.__fractional_year)))
    
    def solar_declination_angle(self) -> float:
        """
        Estimate the solar declination angle
        """
        # Constants
        A = 0.006918
        B = -0.399912
        C = 0.070257
        D = -0.006758
        E = 0.000907
        F = -0.002697
        G = 0.00148
        return (A + B * math.cos(self.__fractional_year) + C * math.sin(self.__fractional_year) +
                D * math.cos(2 * self.__fractional_year) + E * math.sin(2 * self.__fractional_year) +
                F * math.cos(3 * self.__fractional_year) + G * math.sin(3 * self.__fractional_year))