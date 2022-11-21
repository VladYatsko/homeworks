import math

point_x = int(input("Please specify x coordinate: "))
point_y = int(input("Please specify y coordinate: "))
point_x_1 = int(input("Please specify x1 coordinate: "))
point_y_1 = int(input("Please specify y1 coordinate: "))
distance = round(math.sqrt((point_x_1 - point_x)**2 +
                           (point_y_1 - point_y)**2), 2)

print(f"Distance between points is {distance}")
