import os
import shutil


os.system('pyinstaller --noconfirm app.py')
os.makedirs('dist/app/dir')
os.makedirs('dist/app/arch')
os.makedirs('dist/app/json')
os.makedirs('dist/app/xlsx')
os.makedirs('dist/app/template')
os.makedirs('dist/app/log')

shutil.copy('template/Template.xlsx', 'dist/app/template/Template.xlsx')