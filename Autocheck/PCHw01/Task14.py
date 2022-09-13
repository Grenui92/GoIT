from math import *
from math import radians, acos, sin, cos


RADIUS = 6371.01

lat1 = radians(50.45)
lon1 = radians(30.523)

lat2 = radians(51.5072)
lon2 = radians(-0.1275)

distance = RADIUS*acos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(lon1-lon2))
print(distance)
