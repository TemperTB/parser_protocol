# To read the PDF
import json
# To remove the additional created files
import os

from pprint import pprint
import sys

# Получаем список PDF файлов из каталога
def get_pdf_files(dir_path):
    files_pdf = []
    # Получаем список всех файлов и папок
    files = os.listdir(dir_path)
    for file in files:
        # Проверяем на то что это файл и он имеет расширение pdf
        if os.path.isfile(os.path.join(dir_path, file)) and os.path.splitext(file)[1] == '.pdf':
            files_pdf.append(file)
    return files_pdf


# Сохраняем в JSON
def write_to_json(path, name, text):
    with open(path + name +'.json', 'w') as fp:
        json.dump(text, fp, ensure_ascii=False)

# Получаем путь для текущего каталога на продуктиве и деве
def get_cwd():
    cwd = ''
    main_cwd = os.path.abspath(os.path.dirname(__file__))
    if '/' in main_cwd:
        cwd_array = main_cwd.split('/')
    if '\\' in main_cwd:
        cwd_array = main_cwd.split('\\')

    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        last_dir = len(cwd_array) - 1
    else:
        last_dir = len(cwd_array)
    for i in range(0, last_dir):
        cwd = cwd + cwd_array[i] + '/'
    return cwd
