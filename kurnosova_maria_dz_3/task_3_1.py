numbers = {'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре',
           'five': 'пять',
           'six': 'шесть',
           'seven': 'семь',
           'eight': 'восемь',
           'nine': 'девять',
           'ten': 'десять'}


def num_translate(input_number):
    for key, value in numbers.items():
        if input_number == key:
            return value


print(num_translate('six'))
print(num_translate('eleven'))