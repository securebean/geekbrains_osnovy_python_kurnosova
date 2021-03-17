prices_string = ''
prices_list = [57.8, 46.51, 97, 126.50, 13.80, 16, 123.5, 11.25, 67.40, 25.89, 234.56, 65.95]
for i in range(0, len(prices_list)):
    if i < len(prices_list)-1:
        if len(str(prices_list[i]).split('.')) == 1:
            prices_string = prices_string + f"{str(prices_list[i]).split('.')[0]} руб, "
        else:
            prices_list[i] = f"{prices_list[i]:.2f}"
            prices_string = prices_string + f"{str(prices_list[i]).split('.')[0]} руб {int(str(prices_list[i]).split('.')[1])} коп, "
    else:
        if len(str(prices_list[i]).split('.')) == 1:
            prices_string = prices_string + f"{str(prices_list[i]).split('.')[0]} руб"
        else:
            prices_list[i] = f"{prices_list[i]:.2f}"
            prices_string = prices_string + f"{str(prices_list[i]).split('.')[0]} руб {str(prices_list[i]).split('.')[1]} коп"
print(prices_string)
