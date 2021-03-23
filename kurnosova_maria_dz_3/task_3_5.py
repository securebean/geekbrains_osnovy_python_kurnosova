from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    ''' возвращает n шуток, сформированных из трех случайных слов из списков noun, adverbs, adjectives
    n: количество шуток, которые вернет функция
    return: список из n сформированных шуток '''
    result = []
    for i in range(0, n):
        joke = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        result.append(joke)
    return result


print(get_jokes(10))