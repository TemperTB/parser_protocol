# Для считывания PDF
import PyPDF2
# Для анализа структуры PDF и извлечения текста
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LTTextContainer, LTChar, LTRect, LTFigure
# Для извлечения текста из таблиц в PDF
import pdfplumber
# Для извлечения изображений из PDF
from PIL import Image
from pdf2image import convert_from_path
# Для выполнения OCR, чтобы извлекать тексты из изображений  
import pytesseract 
# Для удаления дополнительно созданных файлов
import os

# Константы
from const import PAGE_CONTENT, PAGE_TEXT, TEXT_FROM_IMAGES, TEXT_FROM_TABLES

# Создаём функцию для извлечения текста
def text_extraction(element):
    # Извлекаем текст из вложенного текстового элемента
    line_text = element.get_text()
    # Убираем переносы строки
    cleaned_line_text = line_text.replace('\n', '')
    # Возвращаем текст
    return cleaned_line_text


# Извлечение таблиц из страницы
def extract_table(pdf_path, page_num, table_num):
    # Открываем файл pdf
    pdf = pdfplumber.open(pdf_path)
    # Находим исследуемую страницу
    table_page = pdf.pages[page_num]
    # Извлекаем соответствующую таблицу
    table = table_page.extract_tables()[table_num]
    
    return table

# Преобразуем таблицу в соответствующий формат
def table_converter(table):
    table_string_array = []
    # Итеративно обходим каждую строку в таблице
    for row_num in range(len(table)):
        row = table[row_num]
        filtered_row = [x for x in row if x is not None] 
        cleaned_row = [item.replace('\n', ' ') if item is not None else item for item in filtered_row]
        table_string_array.append('|'.join(cleaned_row))
    return table_string_array

# Создаем функцию для проверки наличия элемента в таблицах, представленных на странице
def is_element_inside_any_table(element, page ,tables):
    x0, y0up, x1, y1up = element.bbox
    # Изменяем кординаты, потому что pdfminer подсчитывает от низжней до верхней части страницы
    y0 = page.bbox[3] - y1up
    y1 = page.bbox[3] - y0up
    for table in tables:
        tx0, ty0, tx1, ty1 = table.bbox
        if tx0 <= x0 <= x1 <= tx1 and ty0 <= y0 <= y1 <= ty1:
            return True
    return False

# Функция поиска таблицы для данного элемента
def find_table_for_element(element, page ,tables):
    x0, y0up, x1, y1up = element.bbox
    # Изменяем кординаты, потому что pdfminer подсчитывает от нижней до верхней части страницы
    y0 = page.bbox[3] - y1up
    y1 = page.bbox[3] - y0up
    for i, table in enumerate(tables):
        tx0, ty0, tx1, ty1 = table.bbox
        if tx0 <= x0 <= x1 <= tx1 and ty0 <= y0 <= y1 <= ty1:
            return i  # Возвращаем индекс таблицы
    return None  

# Функция для вырезания элементов изображений из PDF
def crop_image(element, pageObj):
    # Получаем координаты для вырезания изображения из PDF
    [image_left, image_top, image_right, image_bottom] = [element.x0,element.y0,element.x1,element.y1] 
    # Обрезаем страницу по координатам (left, bottom, right, top)
    pageObj.mediabox.lower_left = (image_left, image_bottom)
    pageObj.mediabox.upper_right = (image_right, image_top)
    # Сохраняем обрезанную страницу в новый PDF
    cropped_pdf_writer = PyPDF2.PdfWriter()
    cropped_pdf_writer.add_page(pageObj)
    # Сохраняем обрезанный PDF в новый файл
    with open('cropped_image.pdf', 'wb') as cropped_pdf_file:
        cropped_pdf_writer.write(cropped_pdf_file)

# Функция для преобразования PDF в изображения
def convert_to_images(input_file,):
    images = convert_from_path(input_file)
    image = images[0]
    output_file = 'PDF_image.png'
    image.save(output_file, 'PNG')

# Создаём функцию для считывания текста из изображений
def image_to_text(image_path):
    # Считываем изображение
    img = Image.open(image_path)
    # Извлекаем текст из изображения
    text = pytesseract.image_to_string(img)
    return 'text'

def pdf_to_txt(pdf_path): 
    # создаём объект файла PDF
    pdfFileObj = open(pdf_path, 'rb')
    # создаём объект считывателя PDF
    pdfReaded = PyPDF2.PdfReader(pdfFileObj)
    # Создаём словарь для извлечения текста из каждого изображения
    text_per_page = {}
    # Create a boolean variable for image detection
    image_flag = False

    #Инициализируем переменные
    page_text = []
    text_from_images = []
    text_from_tables = []
    page_content = []
    
    # Извлекаем страницы из PDF
    for pagenum, page in enumerate(extract_pages(pdf_path)):

        # Инициализируем переменные, необходимые для извлечения текста со страницы
        pageObj = pdfReaded.pages[pagenum]
        
        # Инициализируем количество исследованных таблиц
        table_in_page= -1
        # Открываем файл pdf
        pdf = pdfplumber.open(pdf_path)
        # Находим исследуемую страницу
        page_tables = pdf.pages[pagenum]
        # Находим количество таблиц на странице
        tables = page_tables.find_tables()
        if len(tables)!=0:
            table_in_page = 0

        # Извлекаем таблицы из страницы
        for table_num in range(len(tables)):
            # Извлекаем информацию из таблицы
            table = extract_table(pdf_path, pagenum, table_num)
            # Конвертируем табличную информацию в массив строк
            table_string_array = table_converter(table)
            # Добавляем текст в список
            for row_num in range(len(table_string_array)):
                text_from_tables.append(table_string_array[row_num])

        # Находим все элементы
        page_elements = [(element.y1, element) for element in page._objs]
        # Сортируем все элементы по порядку нахождения на странице
        page_elements.sort(key=lambda a: a[0], reverse=True)


        # Находим элементы, составляющие страницу
        for i,component in enumerate(page_elements):
            # Извлекаем элемент структуры страницы
            element = component[1]

            # Проверяем является ли элемент таблицей
            if table_in_page == -1:
                pass
            else:
                if is_element_inside_any_table(element, page ,tables):
                    table_found = find_table_for_element(element,page ,tables)
                    if table_found == table_in_page and table_found != None:    
                        page_content.append(text_from_tables[table_in_page])
                        table_in_page+=1
                    # Передаем эту итерацию, так как содержимое этого элемента было извлечено из таблиц
                    continue

            if not is_element_inside_any_table(element,page,tables):

                # Проверяем, является ли элемент текстовым
                if isinstance(element, LTTextContainer):
                    # Используем функцию извлечения текста и формата для каждого текстового элемента
                    line_text = text_extraction(element)
                    # Добавляем текст каждой строки к тексту страницы
                    page_text.append(line_text)
                    page_content.append(line_text)


                # Проверяем элементы на наличие изображений
                #if isinstance(element, LTFigure):
                    # Вырезаем изображение из PDF
                    #crop_image(element, pageObj)
                    # Преобразуем обрезанный pdf в изображение
                    #convert_to_images('cropped_image.pdf')
                    # Извлекаем текст из изображения
                    #image_text = image_to_text('PDF_image.png')
                    #text_from_images.append(image_text)
                    #page_content.append(image_text)
                    # Добавляем условное обозначение в списки текста и формата
                    #page_text.append('image')
                    # Обновляем флаг для изображения
                    #image_flag = True

    # Закрываем объект файла pdf
    pdfFileObj.close()
    # Удаляем созданные дополнительные файлы
    if image_flag:
        os.remove('cropped_image.pdf')
        os.remove('PDF_image.png')

    # TODO удаление пустых строк    
     # Добавляем в список значения
    text_per_page = {
        PAGE_TEXT: page_text,
        TEXT_FROM_TABLES: text_from_tables,
        TEXT_FROM_IMAGES: text_from_images,
        PAGE_CONTENT: page_content
    }

    # Возвращаем текст
    return text_per_page
    