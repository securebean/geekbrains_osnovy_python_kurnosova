import os

path = '.\some_data'
file_dict = {100:0, 1000:0, 10000:0, 100000:0}
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    size = os.stat(file_path).st_size
    if size < 100:
        file_dict[100] += 1
    elif size < 1000:
        file_dict[1000] += 1
    elif size < 10000:
        file_dict[10000] += 1
    elif size < 100000:
        file_dict[100000] += 1

print(file_dict)