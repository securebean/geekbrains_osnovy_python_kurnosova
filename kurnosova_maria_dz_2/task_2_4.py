list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print('Изначальный список:', list)
for i in range(0, len(list)):
    human = list[i].split(' ')
    human_name = human[-1]
    right_human_name = human_name.capitalize()
    print(f'Привет, {right_human_name}!')
    human[-1] = right_human_name
    list[i] = ' '.join(human)

print('Корректный список', list)
