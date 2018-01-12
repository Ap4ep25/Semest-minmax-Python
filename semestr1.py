a = float(input("Начальная граница: "))
b = float(input("Конечная граница: "))
c = float(input("Точность: "))

while ((b - a) > c) or (-1 * (b - a) > c):
    x = (a + b) / 2
    x1 = (x - c)
    f1 = x1 * 2 - x1 * 4
    x2 = (x + c)
    f2 = x2 * 2 + x2 * 4
    if f1 < f2:
        b = x
    else:
        a = x
print("Результат: " + str(a))
print("Результат: " + str(b))