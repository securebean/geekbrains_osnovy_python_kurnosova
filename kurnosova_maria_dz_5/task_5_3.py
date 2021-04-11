tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def my_generator(list_a, list_b):
    if len(list_a) > len(list_b):
        list_b.extend({None for i in range(len(list_a) - len(list_b))})
    for t, k in zip(list_a, list_b):
        yield t, k


my_gen = my_generator(tutors, klasses)
print(type(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))