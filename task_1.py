import os


PROJECT_NAME = 'my_project'
if not os.path.exists(PROJECT_NAME):
    os.mkdir(PROJECT_NAME)

dir_names = ['settings', 'mainapp', 'adminapp', 'authapp']
for dir_name in dir_names:
    if not os.path.exists(dir_name):
        os.makedirs(f'{PROJECT_NAME}/{dir_name}', exist_ok=True)
