# # 1 Задача
# a, b = map(int, input().split())
# if a ** 2 == b:
#     print("да")
# else:
#     print("нет")

# # 2 Задача
# a = list(map(int, input().split()))
# max = a[0]
# for i in range(1,len(a)):
#     if a[i] > max:
#         max = a[i]
# print(max)

# 3 Задача
# print("Введите число: ")
# num = int(input())
# for i in range(-num, num+1):
#     print(i, end=', ')
# Тоже самое, но в две строки:
# n = int(input("Введите число: "))
# print(*range(-n, n+1))


# # # 4 Задача
# # print("Введите число: ")
# # num = float(input())
# # tmp = num * 10
# # tmp = int(tmp % 10)
# # print(tmp)
# # Тоже самое, но в две строки:
# num = float(input("Введите число: "))
# print(int(num * 10) % 10)

# # 5 Задача
# print("Введите число: ")
# num = int(input())
# if ((num % 5 == 0 and num % 10 == 0) or (num % 15 == 0)) and (num % 30 != 0):
#     print("yes")
# else:
#     print("no")

# 245 Задача
# Надо было переводить в двоичную систему и умножить на 5
a = int(str((bin(int(input()) - 1)[2:])))*5
print(a)