input_seconds = int(input('Введите количество секунд: '))
#до суток: <h> час <m> мин <s> сек;
if input_seconds > 3599:
    hours = input_seconds // 3600
    extra_seconds = input_seconds % 3600
    minutes = extra_seconds // 60
    seconds = extra_seconds % 60
    print('в', input_seconds, 'секундах', hours, 'час', minutes, 'мин', seconds, 'сек')
elif input_seconds > 59:
    minutes = input_seconds // 60
    seconds = input_seconds % 60
    print('в', input_seconds, 'секундах', minutes, 'мин', seconds, 'сек')
else:
    seconds = input_seconds
    print('в', input_seconds, 'секундах', seconds, 'сек')
