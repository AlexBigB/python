# Задача еще не решена...


# Функция создает массив с с заданными параметрами
def сreate_arr(num_len, ones_amount):
    n = list(range(num_len))
    for j in range(ones_amount):
        n[j] = 1
    for i in range(ones_amount, num_len):
        n[i] = 0
    # print(str(n))  # [1, 1, 0, 0, 0, 0]
    return n

# Функция находит позицию крайнего ноля справа перед числом


def zero_position(n_arr):
    zero_pos = 0
    if n_arr[len(n_arr)-1] == 1:
        zero_pos = len(n_arr)-1
    else:
        for i in range(len(n_arr)-1, 0, -1):
            if n_arr[i-1] == 1:
                zero_pos = i
                break
    # print("zero_pos = " + str(zero_pos))
    return zero_pos


def moove_right(n_arr, ones_amount):
    ones_pos = list()
    for i in range(ones_amount):
        ones_pos.append(i)
    print(ones_pos)
    # for j in range(len(n_arr)-1, 0, -1):
    num_combintaions = []
    # [[1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 0, 1],
    #  [1, 0, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1],
    #  [1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 1, 1],
    #  [1, 1, 1, 1, 0, 0]]
    num_combintaions.append(str(n_arr))
    rev_arr = reversed(n_arr)
    print(*rev_arr)
    while n_arr[len(n_arr) - 1] != 1:
        # ones_pos[ones_amount - 1]
        # [0, 1, 2] 3, 4, 5
        n_arr[ones_pos[len(ones_pos) - 1]] = 0
        ones_pos[len(ones_pos)-1] += 1
        n_arr[ones_pos[len(ones_pos) - 1]] = 1

        num_combintaions.append(str(n_arr))
    # print(num_combintaions)
        # if n_arr[1] != 0:




    # while n_arr[len(n_arr) - 1] != 1:
    #     # ones_pos[ones_amount - 1]
    #     # [0, 1, 2] 3, 4, 5
    #     n_arr[ones_pos[len(ones_pos) - 1]] = 0
    #     ones_pos[len(ones_pos)-1] += 1
    #     n_arr[ones_pos[len(ones_pos) - 1]] = 1

    #     num_combintaions.append(str(n_arr))
    # # print(num_combintaions)
    #     # if n_arr[1] != 0:



####################################################################
tmp_arr = сreate_arr(num_len=6, ones_amount=3)
# print(tmp_arr)
zero = zero_position(n_arr=tmp_arr)
# print(zero)

moove_right(n_arr=tmp_arr, ones_amount=3)
