
from const import ALLUM, ALPHA, AMMIAK, APAV, BARIY, BERILLIY, BETTA, BOR, BPK, BPK_POLN, BROM, CELL, CINK, CISTI, COMPANY, CVET, D_24, DATA, DATE, ECOLI, ENT, FBUZ_NSK, FBUZ_NSK_DATA, FBUZ_NSK_RESULTS, FBUZ_NU, FBUZ_NU_DATA, FBUZ_NU_RESULTS, FENOL, FTOR, GELMINT, GIDROKARBONAT, HLORID, HROM, KADMIY, KLOSTRID, KOBALT, KOLIFAG, KREMNIY, LINDAN, LITIY, LYAMBLIY, MAGNIY, MARGANEC, MED, MISHYAK, MUTN, NAME, NEFT, NIKEL, NITRAT, NITRIT, NUMBER, OKB, OMCH, PAGE_TEXT, PER_OKISL, PH, PIT, POD, POINT, POLIFOSFAT, POV, PROTOCOL_HEAD, RADON, RASTV_KISLOROD, RESULT, RTUT, SALMONELLA, SELEN, SHELOCH, STOK, STRONCIY, SUH_OST, SULFAT, SVINEC, TEXT, TEXT_FROM_TABLES, TYPE, TYPE_PIT, TYPE_POD, TYPE_POV, TYPE_STOK, UNDEFINED, VKUS, VZV_VESH, XPK, ZAPAH_20, ZAPAH_60, ZHELEZO, ZHESTKOST, ZHIZN_GELMINT

# Из текста забираем нужную информацию
def text_to_dyct(name, text):
    
    protocol = {NAME: name, COMPANY: '',
                DATA: {DATE: '', POINT: '', NUMBER: '', TYPE: ''},
                RESULT: {
                    ZAPAH_20: '',
                    ZAPAH_60: '',
                    VKUS: '',
                    CVET: '',
                    MUTN: '',
                    VZV_VESH: '',
                    PH: '',
                    PER_OKISL: '',
                    ZHESTKOST: '',
                    SUH_OST: '',
                    NEFT: '',
                    AMMIAK: '',
                    NITRIT: '',
                    NITRAT: '',
                    HLORID: '',
                    ZHELEZO: '',
                    MARGANEC: '',
                    MED: '',
                    SVINEC: '',
                    CINK: '',
                    ALLUM: '',
                    ECOLI: '',
                    ENT: '',
                    OKB: '',
                    OMCH: '',
                    KOLIFAG: '',
                    KLOSTRID: '',
                    SALMONELLA: '',
                    POLIFOSFAT: '',
                    APAV: '',
                    FENOL: '',
                    SULFAT: '',
                    RTUT: '',
                    BOR: '',
                    KREMNIY: '',
                    MISHYAK: '',
                    FTOR: '',
                    BROM: '',
                    LITIY: '',
                    BARIY: '',
                    BERILLIY: '',
                    SELEN: '',
                    STRONCIY: '',
                    LINDAN: '',
                    D_24: '',
                    NIKEL: '',
                    KADMIY: '',
                    GIDROKARBONAT: '',
                    XPK: '',
                    BPK: '',
                    GELMINT: '',
                    LYAMBLIY: '',
                    RADON: '',
                    ALPHA: '',
                    BETTA: '',
                    RASTV_KISLOROD: '',
                    KOBALT: '',
                    HROM: '',
                    MAGNIY: '',
                    BPK_POLN: '',
                    CISTI: '',
                    ZHIZN_GELMINT: '',
                    SHELOCH: '',
                    },
                    }
    
    page_text = text[PAGE_TEXT]
    text_from_tables = text[TEXT_FROM_TABLES]

    #Проверяем текст на соответствие разным типам протоколов
    for row_text_num in range(len(page_text)):
        text_current_row = text[PAGE_TEXT][row_text_num]
        if PROTOCOL_HEAD[FBUZ_NSK] in text_current_row:
            protocol[COMPANY] = FBUZ_NSK
            protocol[DATA] = get_protocol_data_nsk(page_text)
            protocol[RESULT] = get_protocol_results_nsk(text_from_tables)
            break
        elif PROTOCOL_HEAD[FBUZ_NU] in text_current_row:
            protocol[COMPANY] = FBUZ_NU
            protocol[DATA] = get_protocol_data_nu(page_text)
            protocol[RESULT] = get_protocol_results_nu(text_from_tables)
            break
    # Если тип не нашелся, то он неизвестный
    if protocol[COMPANY] == '':
        protocol[COMPANY] = UNDEFINED
    return protocol
        
# Получить данные о протоколе ФБУЗ г.Ноябрьск (тип, дата, номер, точка отбора)
def get_protocol_data_nsk(page_text): 
    data = {}
    for row_text_num in range(len(page_text)):
        current_row = page_text[row_text_num]
        if FBUZ_NSK_DATA[TYPE_PIT] in current_row:
            data[TYPE] = PIT
        if FBUZ_NSK_DATA[TYPE_POD] in current_row:
            data[TYPE] = POD
        if FBUZ_NSK_DATA[TYPE_POV] in current_row:
            data[TYPE] = POV
        if FBUZ_NSK_DATA[TYPE_STOK] in current_row:
            data[TYPE] = STOK
        if FBUZ_NSK_DATA[DATE] in current_row:
            array = current_row.split(' ')
            data[DATE] = array[5]
        if FBUZ_NSK_DATA[POINT] in current_row:
            data[POINT] = current_row.replace(FBUZ_NSK_DATA[POINT], '').strip()
        if FBUZ_NSK_DATA[NUMBER] in current_row:
            array = current_row.split(' ')
            data[NUMBER] = array[3].strip()
    return data

# Получить данные о результатах ФБУЗ г. Ноябрьск
def get_protocol_results_nsk(text_from_tables): 
    results = {}
    for key in FBUZ_NSK_RESULTS.keys():
        results[key] = ''
        for row_text_num in range(len(text_from_tables)):
            current_row = text_from_tables[row_text_num]
            if FBUZ_NSK_RESULTS[key][TEXT] in current_row:
                array = current_row.split('|')
                results[key] = array[FBUZ_NSK_RESULTS[key][CELL]]
                break
    return results

# Получить данные о протоколе ФБУЗ г.Новый Уренгой (тип, дата, номер, точка отбора)
def get_protocol_data_nu(page_text): 
    data = {}
    for row_text_num in range(len(page_text)):
        current_row = page_text[row_text_num]
        if FBUZ_NU_DATA[TYPE_PIT] in current_row:
            data[TYPE] = PIT
        if FBUZ_NU_DATA[TYPE_POD] in current_row:
            data[TYPE] = POD
        if FBUZ_NU_DATA[TYPE_POV] in current_row:
            data[TYPE] = POV
        if FBUZ_NU_DATA[TYPE_STOK] in current_row:
            data[TYPE] = STOK
        if FBUZ_NU_DATA[DATE] in current_row:
            current_row = current_row.strip()
            array = current_row.split(' ')
            data[DATE] = array[2]
        if FBUZ_NU_DATA[POINT] in current_row:
            data[POINT] = current_row.replace(FBUZ_NU_DATA[POINT], '').strip()
        if FBUZ_NU_DATA[NUMBER] in current_row:
            array = current_row.split(' ')
            data[NUMBER] = array[3].strip()
    return data

# Получить данные о результатах ФБУЗ г. Новый Уренгой
def get_protocol_results_nu(text_from_tables): 
    results = {}
    for key in FBUZ_NU_RESULTS.keys():
        results[key] = ''
        for row_text_num in range(len(text_from_tables)):
            current_row = text_from_tables[row_text_num]
            if FBUZ_NU_RESULTS[key][TEXT] in current_row:
                array = current_row.split('|')
                results[key] = array[FBUZ_NU_RESULTS[key][CELL]]
                break
    return results

