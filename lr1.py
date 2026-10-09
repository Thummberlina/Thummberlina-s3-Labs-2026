while True:
    try:
        koef_a = float(input("Введите A: "))
        break
    except ValueError:
        print("Это не число, введите число")

while True:
    try:
        koef_b = float(input("Введите B: "))
        break
    except ValueError:
        print("Это не число, введите число")

while True:
    try:
        koef_c = float(input("Введите C: "))
        break
    except ValueError:
        print("Это не число, введите число")

if koef_a == 0:
    print("A = 0, решаем уравнение B*x^2 + C = 0")

    if koef_b == 0:
        if koef_c == 0:
            print("Уравнение 0 = 0, любое x является решением")
        else:
            print("Уравнение не имеет решений")
    else:
        zamena = -koef_c / koef_b
        if zamena < 0:
            print("Нет действительных корней")
        elif zamena == 0:
            print("x = 0")
        else:
            x1 = zamena ** 0.5
            x2 = -x1
            print("x1 =", x1)
            print("x2 =", x2)
else:
    D = koef_b * koef_b - 4 * koef_a * koef_c
    print("D =", D)

    if D < 0:
        print("Нет действительных корней")
    elif D == 0:
        zamena = -koef_b / (2 * koef_a)
        if zamena < 0:
            print("Нет действительных корней")
        elif zamena == 0:
            print("x = 0")
        else:
            x1 = zamena ** 0.5
            x2 = -x1
            print("x1 =", x1)
            print("x2 =", x2)
    else:
        zamena1 = (-koef_b - D ** 0.5) / (2 * koef_a)
        zamena2 = (-koef_b + D ** 0.5) / (2 * koef_a)

        if zamena1 > 0:
            x1 = zamena1 ** 0.5
            x2 = -x1
            print("x1 =", x1)
            print("x2 =", x2)
        elif zamena1 == 0:
            print("x = 0")

        if zamena2 > 0:
            x3 = zamena2 ** 0.5
            x4 = -x3
            print("x3 =", x3)
            print("x4 =", x4)
        elif zamena2 == 0:
            print("x = 0")

        if zamena1 < 0 and zamena2 < 0:
            print("Нет действительных корней")