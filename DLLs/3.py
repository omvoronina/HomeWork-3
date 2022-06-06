# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

for i in range(2, 10):
    list = []
    for j in range(2, 101):
        if j % i == 0 and j != i:
            j = 0
            list.append(j)
        else:
            j = j
    print(f'{list.count(0)} чисел кратны {i}')
