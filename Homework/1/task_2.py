# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input("Введите бинарное X: "))
y = int(input("Введите бинарное Y: "))
z = int(input("Введите бинарное Z: "))

print("¬(X ⋁ Y ⋁ Z) = ", not(x or y or z))
print("¬X ⋀ ¬Y ⋀ ¬Z = ", not x and not y and not z)
print("Соответственно всё утверждение = ", (not(x or y or z)) == (not x and not y and not z))