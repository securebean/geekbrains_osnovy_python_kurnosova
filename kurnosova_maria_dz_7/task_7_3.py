import os
import shutil

path = '.\my_project'
if not os.path.isdir(os.path.join(path, 'templates')):
    os.mkdir(os.path.join(path, 'templates'))
for root, dirs, files in os.walk(path):
    for file in files:
        if file.split('.')[-1] == 'html':
            folder_name = os.path.split(root)[-1]
            templates_path = '.\my_project\\templates'
            folder_in_templates = os.path.join(templates_path, folder_name)
            if not os.path.isdir(folder_in_templates):
                os.mkdir(folder_in_templates)
            try:
                new_file = shutil.copy(os.path.join(root, file), os.path.join(folder_in_templates, file))
            except shutil.SameFileError:
                pass
