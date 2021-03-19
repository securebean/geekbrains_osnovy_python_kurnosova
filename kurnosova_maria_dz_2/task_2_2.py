list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(list):
    if not list[i].isalpha():
        if list[i][0] in ('+', '-'):
            number = f'{int(list[i][1:]):02d}'
            list[i] = list[i][0] + number
        else:
            list[i] = f'{int(list[i]):02d}'
        list.insert(i, '\"')
        list.insert(i+2, '\"')
        i = i + 3
    else:
        i = i + 1

print(list)
i = 0
string = ''
while i < len(list):
    if list[i] == '\"':
        string = string + (list[i] + list[i+1] + list[i+2] + ' ')
        i = i + 3
    else:
        string = string + (list[i] + ' ')
        i = i + 1

print(string)
