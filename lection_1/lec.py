
value = None
a = 123
b = 1.23
print(a)
print(b)
print(type(value))
value = 123
s = "some ' word"
print(s)

print(a, b, s)
print(a, '-', b, '-', s)
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = True
list = ['1', '2', '3']
print(list)


# print("Введите а: ")
# a = int(input())
# print("Введите b: ")
# b = int(input())

a = 1.1232
b = 3
c = round(a * b, 5)
print(c)

a += 5

f = [1, 2, 3, 4]
print(2 in f)  # True

a = int(input('a = '))
b = int(input('b = '))

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй хватит')
print(inverted2)

for i in range(1, 10, 2):
    print(i)

text = 'съешь ещё этих мягких французских булок'
print(len(text))
print('ещё' in text)
print(text.isdigit())
print(text.islower())
print(text.replace('ещё', 'ЕЩЁ'))
print(text[:2])
print(text[-2])


list.append('some')
list.remove('some')  # or del


# def f(x):
#     # body
