list_of_workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print('Изначальный список:', list_of_workers)
for i in range(0, len(list_of_workers)):
    human = list_of_workers[i].split(' ')
    human_name = human[-1]
    right_human_name = human_name.capitalize()
    print(f'Привет, {right_human_name}!')
