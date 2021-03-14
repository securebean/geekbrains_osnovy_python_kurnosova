cubes_list = []
sum_divided_7 = 0    #сумма чисел, сумма цифр которых делится на 7 из первоначального списка
sum_divided_after = 0    #сумма чисел, сумма цифр которых делится на 7 после добавления к каждому элементу 17ти

for i in range(0, 1000):
    cubes_list.append(i**3)
    cube_string = str(cubes_list[i])
    sum_digits = 0
    for digit in cube_string:    #считаем сумму цифр числа в итерации
        sum_digits = sum_digits + int(digit)
    if sum_digits % 7 == 0:    #если сумма цифр числа делится на 7, прибавляем его к имеющейся сумме
        sum_divided_7 = sum_divided_7 + cubes_list[i]
    cubes_list[i] = cubes_list[i] + 17
    another_cube_string = str(cubes_list[i])
    another_sum_digits = 0
    for digit in another_cube_string:    #считаем сумму цифр числа в итерации после добавления к нему 17
        another_sum_digits = another_sum_digits + int(digit)
    if another_sum_digits % 7 == 0:
        sum_divided_after = sum_divided_after + cubes_list[i]


print(sum_divided_7)
print(sum_divided_after)