import math

def calculate_trigonometry(angle_in_degrees):
    angle_in_radians = (angle_in_degrees * math.pi) / 180
    sin_angle = math.sin(angle_in_radians)
    cos_angle = math.cos(angle_in_radians)
    tan_angle = math.tan(angle_in_radians)
    print("sin(", angle_in_degrees, "degrees) =", sin_angle)
    print("cos(", angle_in_degrees, "degrees) =", cos_angle)
    print("tan(", angle_in_degrees, "degrees) =", tan_angle)

angle = float(input("Enter an angle in degrees: "))
calculate_trigonometry(angle)