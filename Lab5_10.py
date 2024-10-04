global result

def rectangle():
    a = float(input("Введите ширину: "))
    b = float(input("Введите высоту: "))
    global result
    result = a * b
    print(f"Площадь прямоугольника равна {a} * {b} = {result} ")

def trangle():
    a = float(input("Введите основание: "))
    h = float(input("Введите высоту: "))
    global result
    result = 0.5 * a * h
    print(f"Площадь треугольника равна 0.5 * {a} * {h} = {result} ")

figure  = input("Выберите фигуру:\n1 - прямоугольник\n2 - треугольник\n")
if figure == '1':
    rectangle()
elif figure == '2':
    trangle()
