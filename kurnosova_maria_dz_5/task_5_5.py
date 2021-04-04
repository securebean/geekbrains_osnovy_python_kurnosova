src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []


for i in range(0, len(src)):
    if src.count(src[i]) == 1:
        result.append(src[i])

print(set(src))