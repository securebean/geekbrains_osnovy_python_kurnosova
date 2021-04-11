import os

main_dir_name = 'my_project'
other_dir_names = ['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.isdir(main_dir_name):
    os.mkdir(main_dir_name)
for d in other_dir_names:
    dir_path_to_make = os.path.join(main_dir_name, d)
    if not os.path.isdir(dir_path_to_make):
        os.mkdir(dir_path_to_make)
