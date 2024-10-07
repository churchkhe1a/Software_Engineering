import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

max_sides = [max(one), max(two), max(three)]
min_sides = [min(one), min(two), min(three)]

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

area_max = triangle_area(*max_sides)
area_min = triangle_area(*min_sides)

print(f"Площадь треугольника из максимальных сторон: {area_max}")
print(f"Площадь треугольника из минимальных сторон: {area_min}")
