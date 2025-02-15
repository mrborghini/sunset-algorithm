import math

def julian_day(year, month, day):
    return 367 * year - (7 * (year + (month + 9) // 12) // 4) + (275 * month // 9) + day + 1721013.5

def equation_of_time(n):
    B = math.radians((360 / 365) * (n - 81))
    return 9.87 * math.sin(2 * B) - 7.53 * math.cos(B) - 1.5 * math.sin(B)

def solar_declination(n):
    return math.radians(23.44) * math.sin(math.radians((360/365.24) * (n - 81)))

def hour_angle(latitude, declination, correction=0):
    lat_rad = math.radians(latitude)
    return math.acos((math.sin(math.radians(-0.833 + correction)) - math.sin(lat_rad) * math.sin(declination)) /
                     (math.cos(lat_rad) * math.cos(declination)))

def calculate_sunset(year, month, day, latitude, longitude, timezone):
    JD = julian_day(year, month, day)
    n = JD - 2451545.0  

    EoT = equation_of_time(n)
    declination = solar_declination(n)
    
    H = hour_angle(latitude, declination, correction=-0.9)  # Adjust for atmospheric refraction
    
    solar_noon_utc = 12 - (EoT / 60) - (longitude / 15)  # Adjust for longitude
    sunset_utc = solar_noon_utc + (H * 180 / math.pi) / 15
    sunset_local = sunset_utc + timezone  
    
    hours = int(sunset_local)
    minutes = int((sunset_local - hours) * 60)
    
    return f"{hours:02d}:{minutes:02d}"

# Location: Schagen, Netherlands (52.7865°N, 4.7986°E, Timezone: UTC+1)
sunset_time = calculate_sunset(2025, 2, 15, 52.7865, 4.7986, 1)
print("Sunset in Schagen on 15-02-2025:", sunset_time)
