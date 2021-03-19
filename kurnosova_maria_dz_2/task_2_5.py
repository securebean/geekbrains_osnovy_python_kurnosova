# задание 5
prices_string = ''
prices_list = [57.8, 46.51, 97, 126.50, 13.80, 16, 123.5, 11.25, 67.40, 25.89, 234.56, 65.95]

for i in prices_list:
    num_1 = int(i // 1)  # кол-во рублей
    num_2 = int(i % 1 * 100)  # кол-во копеек
    prices_string = prices_string + f'{num_1} руб {num_2:02} коп, '    # в задании вывести в строку через запятую

prices_string = prices_string[:-2]
print(prices_string)


print(id(prices_list))    # цены, отсортированные по возрастанию, новый список не создавать
prices_list.sort()
print(prices_list)
print(id(prices_list))


reversed_prices_list = prices_list[::-1]    # новый список, содержащий те же цены, но отсортированные по убыванию
print(reversed_prices_list)


print('5 самых дорогих товаров:')
reversed_string = ''
for i in range(0, 5):
    num_1 = int(reversed_prices_list[i] // 1)  # кол-во рублей
    num_2 = int(reversed_prices_list[i] % 1 * 100)  # кол-во копеек
    reversed_string = reversed_string + f'{num_1} руб {num_2:02} коп, '    # в задании вывести в строку через запятую

reversed_string = reversed_string[:-2]
print(reversed_string)
