import math 

def degreeCalc(degree):
    angle_in_radians = (degree * math.pi) / 180

    angleCos = math.cos(angle_in_radians)
    angleSin = math.sin(angle_in_radians)
    angleTan = math.tan(angle_in_radians)

    print("Cos of " + degree + " is " + angleCos)
    print("Sin of " + degree + " is " + angleSin)
    print("Tan of " + degree + " is " + angleTan)