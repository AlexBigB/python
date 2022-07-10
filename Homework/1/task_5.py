# Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math


def gipotenuza(x1, y1, x2, y2):
    kat1 = x1 - x2
    kat2 = y1 - y2
    gip = math.sqrt(kat1 ** 2 + kat2 ** 2)
    print(kat1 ** 2)
    print(kat2 ** 2)
    return gip


s_a = input("Введите координаты а: ")
s_a_arr = s_a.split(',')
a_x = float(s_a_arr[0])
a_y = float(s_a_arr[1])
s_b = input("Введите координаты b: ")
s_b_arr = s_b.split(',')
b_x = float(s_b_arr[0])
b_y = float(s_b_arr[1])
gipo = gipotenuza(a_x, a_y, b_x, b_y)
print("%.2f" % gipo)
# К сожалению этот способ вывода округляет до нужной позиции,
# что с одной стороны верно, но в примере не так...