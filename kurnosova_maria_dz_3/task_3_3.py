def thesaurus(*names):
    workers_by_letter = {}
    for name in names:
        if name[0] in workers_by_letter:
            workers_by_letter[name[0]].append(name)
        else:
            workers_by_letter[name[0]] = [name]
    return workers_by_letter


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))