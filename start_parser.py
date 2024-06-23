import logging
import os
import shutil
import sys
from const import COMPANY
from function import get_cwd, get_pdf_files, write_to_json
from pdf_to_txt import pdf_to_txt
from text_to_dyct import text_to_dyct
from pprint import pprint
from write_to_excel import write_to_excel

# Парсить файл
# path - путь к файлам pdf для парсинга
# is_arch - надо ли перемещать файлы в папку arch?
# is_log - сохранять log в файл?
# is_arch - сохранять json файлы?
def start_parser(path, is_arch, is_log, is_json):

    # Определяем текущий каталог
    cwd = get_cwd()
    # Определяем вспомогательные директории
    path_arch = cwd + 'arch/'
    path_json = cwd + 'json/'
    path_xlsx = cwd + 'xlsx/'
    path_template = cwd + 'template/'
    path_log = cwd + 'log/'

    # Создаем логирование (в консоль логируем в любом случае, в файл нет)
    console_out = logging.StreamHandler()
    if is_log:
        file_log = logging.FileHandler(path_log + u'log.log')
        logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.INFO, handlers=(file_log, console_out))
    else:
        logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.INFO)
    logging.info(u'Начинаю работать со следующими параметрами: Путь к PDF: ' + path + u', Архивирование: ' + str(is_arch) + u', Логирование: ' + str(is_log) + u', Сохранение JSON: ' + str(is_json) + u'.')

    # Определяем необходимую директорию с pdf-файлами
    if path[len(path) - 1] != '/':
        path_pdf = path + '/'
    else:
        path_pdf = path

    #Проверяем директорию на существование
    if not os.path.isdir(path_pdf):
        logging.error(u'Вы указали неправильный путь')
        return

    # Находим все файлы pdf
    files_pdf = get_pdf_files(path_pdf)
    if len(files_pdf) > 0:
        logging.info(u'Определил количество протоколов: ' + str(len(files_pdf)))
    else:
        logging.error(u'Файлов PDF по заданному пути нет')
        return


    # Сканируем каждый pdf файл
    logging.info( u'Работаю с PDF протоколами')
    protocols = []
    # Берем каждый файл
    for file in files_pdf:
        logging.info( u'Начинаю работать с протоколом: ' + file)
        # Получаем имя файла
        name = os.path.splitext(file)[0]
        # Трансформируем pdf в текст
        logging.info( u'Преобразую pdf в текст')
        text = pdf_to_txt(path_pdf + file)
        logging.info( u'Файл преобразован')
        # Сохраняем в JSON первую версию если нужно
        if is_json:
            logging.info( u'Сохраняю JSON первой версии')
            write_to_json(path_json, name, text)
            logging.info( u'JSON первой версии сохранен')
        # Забираем нужные данные
        logging.info( u'Получаю необходимые данные') 
        protocol = text_to_dyct(name, text)
        logging.info( u'Данные получены')
        logging.info( u'Компания: ' + protocol[COMPANY])
        # Сохраняем в JSON протокол если нужно
        if is_json:
            logging.info( u'Сохраняю JSON итоговый')
            write_to_json(path_json, name + '_complete', protocol)
            logging.info( u'JSON итоговый сохранен')
        # Добавляем протокол в список
        protocols.append(protocol)
        logging.info( u'Работа с протоколом завершена')
        # Перемешаем pdf файл если нужно
        if is_arch:
            shutil.move(path_pdf + file, path_arch + file)
            logging.info( u'Протокол перемещен в архив')
    logging.info( u'Обработка PDF протоколов завершена')

    # Записываем результаты в Excel таблицу
    logging.info( u'Записываю данные в Excel')
    write_to_excel(path_template, path_xlsx, protocols)
    logging.info( u'Готово')

