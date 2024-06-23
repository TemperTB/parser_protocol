import os
import shutil

def delete_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f'Ошибка при удалении файла {file_path}. {e}')

def move_files_in_folder(folder_path_out, folder_path_in):
    for filename in os.listdir(folder_path_out):
        file_path = os.path.join(folder_path_out, filename)
        try:
            if os.path.isfile(file_path):
                shutil.move(file_path, folder_path_in + filename)
        except Exception as e:
            print(f'Ошибка при перемещении файла {file_path}. {e}')

# Определяем директории
path_pdf = 'dir/'
path_arch = 'arch/'
path_json = 'json/'
path_xlsx = 'xlsx/'
path_log = 'log/'

# Удаляем логи, JSON, xlsx
delete_files_in_folder(path_json)
delete_files_in_folder(path_log)
delete_files_in_folder(path_xlsx)

# Пермещаем файлы из архива
move_files_in_folder(path_arch, path_pdf)



