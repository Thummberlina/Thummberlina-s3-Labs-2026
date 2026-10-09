def vvesti_chislo(imya):
    while True:
        try:
            return float(input("Введите " + imya + ": "))
        except ValueError:
            print("Это не число, введите число")


def vvesti_koeficienty():
    koef_a = vvesti_chislo("A")
    koef_b = vvesti_chislo("B")
    koef_c = vvesti_chislo("C")
    return koef_a, koef_b, koef_c


def reshenie_kvadratnogo(koef_b, koef_c):
    print("A = 0, решаем квадратное уравнение B*x^2 + C = 0")

    if koef_b == 0:
        if koef_c == 0:
            print("Уравнение 0 = 0, любое x является решением")
        else:
            print("Уравнение не имеет решений")
        return

    zamena = -koef_c / koef_b
    if zamena < 0:
        print("Нет действительных корней")
    elif zamena == 0:
        print("x = 0")
    else:
        print("x =", zamena ** 0.5)
        print("x =", -zamena ** 0.5)


def reshenie_bikvadratnogo(koef_a, koef_b, koef_c):
    D = koef_b * koef_b - 4 * koef_a * koef_c
    print("D =", D)

    if D < 0:
        print("Корней нет")
    elif D == 0:
        zamena = -koef_b / (2 * koef_a)
        if zamena < 0:
            print("Корней нет")
        elif zamena == 0:
            print("x = 0")
        else:
            print("x =", zamena ** 0.5)
            print("x =", -zamena ** 0.5)
    else:
        zamena1 = (-koef_b + D ** 0.5) / (2 * koef_a)
        zamena2 = (-koef_b - D ** 0.5) / (2 * koef_a)

        if zamena1 > 0:
            print("x =", zamena1 ** 0.5)
            print("x =", -zamena1 ** 0.5)
        elif zamena1 == 0:
            print("x = 0")

        if zamena2 > 0:
            print("x =", zamena2 ** 0.5)
            print("x =", -zamena2 ** 0.5)
        elif zamena2 == 0:
            print("x = 0")

        if zamena1 < 0 and zamena2 < 0:
            print("Корней нет")


def main():
    koef_a, koef_b, koef_c = vvesti_koeficienty()
    if koef_a == 0:
        reshenie_kvadratnogo(koef_b, koef_c)
    else:
        reshenie_bikvadratnogo(koef_a, koef_b, koef_c)


if __name__ == "__main__":
    main()