import enum

PAGE_CONTENT = 'page_content'
PAGE_TEXT = 'page_text'
TEXT_FROM_IMAGES = 'text_from_images'
TEXT_FROM_TABLES = 'text_from_tables'

NAME = 'name'
COMPANY = 'company'

TYPE = 'type'
TYPE_PIT = 'type_pit'
TYPE_STOK = 'type_stok'
TYPE_POD = 'type_pod'
TYPE_POV = 'type_pov'
PIT = 'Питьевая'
POV = 'Поверхностная'
POD = 'Подземная'
STOK = 'Сточная'
DATA = 'data'
DATE = 'date'
POINT = 'point'
NUMBER = 'number'

RESULT = 'results'
TEXT = 'text'
CELL = 'cell'
ZAPAH_20 = 'zapah_20'
ZAPAH_60 = 'zapah_60'
VKUS = 'vkus'
CVET = 'cvet'
MUTN = 'mutn'
VZV_VESH = 'vzv_vesh'
PH = 'ph'
PER_OKISL = 'per_okisl'
ZHESTKOST = 'zhestkost'
SUH_OST = 'suh_ost'
NEFT = 'neft'
AMMIAK = 'ammiak'
NITRIT = 'nitrit'
NITRAT = 'nitrat'
HLORID = 'hlorid'
ZHELEZO = 'zhelezo'
MARGANEC = 'marganec'
MED = 'med'
SVINEC = 'svinec'
CINK = 'cink'
ALLUM = 'allum'
ECOLI = 'ecoli'
ENT = 'ent'
OKB = 'okb'
OMCH = 'omch'
KOLIFAG = 'kolifag'
KLOSTRID = 'klostrid'
SALMONELLA = 'salmonella'
POLIFOSFAT = 'polifosfat'
APAV = 'apav'
FENOL = 'fenol'
SULFAT = 'sulfat'
RTUT = 'rtut'
BOR = 'bor'
KREMNIY = 'kremniy'
MISHYAK = 'mishyak'
FTOR = 'ftor'
BROM = 'brom'
LITIY = 'litiy'
BARIY = 'bariy'
BERILLIY = 'berilliy'
SELEN = 'selen'
STRONCIY = 'stronciy'
LINDAN = 'lindan'
D_24 = 'd_24'
NIKEL = 'nikel'
KADMIY = 'kadmiy'
GIDROKARBONAT = 'gidrokarbonat'
XPK = 'xpk'
BPK = 'bpk'
GELMINT = 'gelmint'
LYAMBLIY = 'lyambliy'
RADON = 'radon'
ALPHA = 'alpha'
BETTA = 'betta'
RASTV_KISLOROD = 'rastv_kislorod'
KOBALT = 'kobalt'
HROM = 'hrom'
MAGNIY = 'magniy'
BPK_POLN = 'BPK_poln'
CISTI = 'cisti'
ZHIZN_GELMINT = 'zhizn_gelmint'
SHELOCH = 'sheloch'

FBUZ_NSK = 'ФБУЗ г. Ноябрьск'
FBUZ_NU = 'ФБУЗ г. Новый Уренгой'
UNDEFINED = 'Неизвестный'


PROTOCOL_HEAD = {FBUZ_NSK: 'Ноябрьск, Муравленко» Юридический адрес: ул. Ямальская, 4, ',
                 FBUZ_NU: 'г. Новый Уренгой, Тазовском районе» Юридический адрес: 629008'}

FBUZ_NSK_DATA = {
    TYPE_PIT : '3. Наименование и характеристики образца испытаний (пробы): Вода питьевая',
    TYPE_POD: '3. Наименование и характеристики образца испытаний (пробы): Вода подземных водоисточников ',
    TYPE_POV: 'Lorem Ipsum',
    TYPE_STOK : 'Lorem Ipsum',
    DATE: 'ПРОТОКОЛ ИСПЫТАНИЙ',
    NUMBER: 'ПРОТОКОЛ ИСПЫТАНИЙ',
    POINT: '4. Место отбора: '
    }

FBUZ_NSK_RESULTS = {
    ZAPAH_20: {TEXT: 'Lorem Ipsum', CELL: 3},
    ZAPAH_60: {TEXT: 'Lorem Ipsum', CELL: 3},
    VKUS: {TEXT: 'Lorem Ipsum', CELL: 3},
    CVET: {TEXT: 'Lorem Ipsum', CELL: 3},
    MUTN: {TEXT: 'Lorem Ipsum', CELL: 3},
    VZV_VESH: {TEXT: 'Lorem Ipsum', CELL: 3},
    PH: {TEXT: 'Lorem Ipsum', CELL: 3},
    PER_OKISL: {TEXT: 'Lorem Ipsum', CELL: 3},
    ZHESTKOST: {TEXT: 'Lorem Ipsum', CELL: 3},
    SUH_OST: {TEXT: 'Lorem Ipsum', CELL: 3},
    NEFT: {TEXT: 'Lorem Ipsum', CELL: 3},
    AMMIAK: {TEXT: 'Lorem Ipsum', CELL: 3},
    NITRIT: {TEXT: 'Lorem Ipsum', CELL: 3},
    NITRAT: {TEXT: 'Lorem Ipsum', CELL: 3},
    HLORID: {TEXT: 'Lorem Ipsum', CELL: 3},
    ZHELEZO: {TEXT: 'Lorem Ipsum', CELL: 3},
    MARGANEC: {TEXT: 'Lorem Ipsum', CELL: 3},
    MED: {TEXT: 'Lorem Ipsum', CELL: 3},
    SVINEC: {TEXT: 'Массовая концентрация свинца/Свинец', CELL: 3},
    CINK: {TEXT: 'Массовая концентрация цинка/Цинк|мг/дм3', CELL: 3},
    ALLUM: {TEXT: 'Lorem Ipsum', CELL: 3},
    ECOLI: {TEXT: 'Escherichia coli', CELL: 3},
    OMCH: {TEXT: 'Общее микробное число (ОМЧ)', CELL: 3},
    OKB: {TEXT: 'Общие колиформные бакте- рии', CELL: 3},
    ENT: {TEXT: 'Энтерококки', CELL: 3},
    KOLIFAG: {TEXT: 'Lorem Ipsum', CELL: 3},
    KLOSTRID: {TEXT: 'Lorem Ipsum', CELL: 3},
    SALMONELLA: {TEXT: 'Lorem Ipsum', CELL: 3},
    POLIFOSFAT: {TEXT: 'Lorem Ipsum', CELL: 3},
    APAV: {TEXT: 'Массовая концентрация АПАВ/АПАВ', CELL: 3},
    FENOL: {TEXT: 'Массовая концентрация фе- нолов /Фенол', CELL: 3},
    SULFAT: {TEXT: 'Lorem Ipsum', CELL: 3},
    RTUT: {TEXT: 'Массовая концентрация ртути/Ртуть', CELL: 3},
    BOR: {TEXT: 'Lorem Ipsum', CELL: 3},
    KREMNIY: {TEXT: 'Lorem Ipsum', CELL: 3},
    MISHYAK: {TEXT: 'Lorem Ipsum', CELL: 3},
    FTOR: {TEXT: 'Lorem Ipsum', CELL: 3},
    BROM: {TEXT: 'Lorem Ipsum', CELL: 3},
    LITIY: {TEXT: 'Lorem Ipsum', CELL: 3},
    BARIY: {TEXT: 'Lorem Ipsum', CELL: 3},
    BERILLIY: {TEXT: 'Lorem Ipsum', CELL: 3},
    SELEN: {TEXT: 'Lorem Ipsum', CELL: 3},
    STRONCIY: {TEXT: 'Lorem Ipsum', CELL: 3},
    LINDAN: {TEXT: 'Lorem Ipsum', CELL: 3},
    D_24: {TEXT: 'Lorem Ipsum', CELL: 3},
    NIKEL: {TEXT: 'Lorem Ipsum', CELL: 3},
    KADMIY: {TEXT: 'Lorem Ipsum', CELL: 3},
    GIDROKARBONAT: {TEXT: 'Lorem Ipsum', CELL: 3},
    XPK: {TEXT: 'Lorem Ipsum', CELL: 3},
    BPK: {TEXT: 'Lorem Ipsum', CELL: 3},
    GELMINT: {TEXT: 'Lorem Ipsum', CELL: 3},
    LYAMBLIY: {TEXT: 'Lorem Ipsum', CELL: 3},
    RADON: {TEXT: 'Удельная активность 222 Rn/Радон (222Rn)', CELL: 3},
    ALPHA: {TEXT: 'Суммарная альфа-актив- ность', CELL: 3},
    BETTA: {TEXT: 'Суммарная бета-активность', CELL: 3},
    RASTV_KISLOROD: {TEXT: 'Lorem Ipsum', CELL: 3},
    KOBALT: {TEXT: 'Lorem Ipsum', CELL: 3},
    HROM: {TEXT: 'Lorem Ipsum', CELL: 3},
    MAGNIY: {TEXT: 'Lorem Ipsum', CELL: 3},
    BPK_POLN: {TEXT: 'Биохимическое потребление кислорода после n-дней инкубации / БПК полн', CELL: 3},
    CISTI: {TEXT: 'Цисты кишечных простейших', CELL: 3},
    ZHIZN_GELMINT: {TEXT: 'Жизнеспособные яйца гельминтов (аскарид, власоглав, токсокар, фасциол), онкосферы тениид и жизнеспособные цисты патогенных кишечных простейших', CELL: 3},
    SHELOCH: {TEXT: 'Lorem Ipsum', CELL: 3}
}

FBUZ_NU_DATA = {
    TYPE_PIT : 'Вода питьевая',
    TYPE_POD: 'Вода подземных водоисточников',
    TYPE_POV: 'Вода природная (поверхностная)',
    TYPE_STOK : 'Сточная вода',
    DATE: 'Дата утверждения',
    NUMBER: 'ПРОТОКОЛ ИСПЫТАНИЙ',
    POINT: '4. Место отбора: '
    }


#TODO Сульфаты и сультфат-ион разделить (протоколы 4339, 1481)
FBUZ_NU_RESULTS = {
    ZAPAH_20: {TEXT: 'Запах при 20 °С', CELL: 3},
    ZAPAH_60: {TEXT: 'Запах при 60 °С', CELL: 3},
    VKUS: {TEXT: 'Интенсивность вкуса и привкуса', CELL: 3},
    CVET: {TEXT: 'Цветность', CELL: 3},
    MUTN: {TEXT: 'Мутность', CELL: 3},
    VZV_VESH: {TEXT: 'Взвешенные вещества', CELL: 3},
    PH: {TEXT: 'Водородный показатель рН', CELL: 3},
    PER_OKISL: {TEXT: 'Перманганатная окисляемость', CELL: 3},
    ZHESTKOST: {TEXT: 'Жесткость', CELL: 3},
    SUH_OST: {TEXT: 'Сухой остаток', CELL: 3},
    NEFT: {TEXT: 'Нефтепродукты', CELL: 3},
    AMMIAK: {TEXT: 'Аммиак и ионы аммония', CELL: 3},
    NITRIT: {TEXT: 'Нитриты', CELL: 3},
    NITRAT: {TEXT: 'Нитраты', CELL: 3},
    HLORID: {TEXT: 'Хлориды', CELL: 3},
    ZHELEZO: {TEXT: 'Общее железо', CELL: 3},
    MARGANEC: {TEXT: 'Марганец', CELL: 3},
    MED: {TEXT: 'Медь', CELL: 3},
    SVINEC: {TEXT: 'Свинец', CELL: 3},
    CINK: {TEXT: 'Цинк', CELL: 3},
    ALLUM: {TEXT: 'Алюминий', CELL: 3},
    ECOLI: {TEXT: 'Escherichia coli', CELL: 3},
    OMCH: {TEXT: 'Общее микробное число', CELL: 3},
    OKB: {TEXT: 'Общие (обобщенные) колиформные бактерии', CELL: 3},
    ENT: {TEXT: 'Энтерококки', CELL: 3},
    KOLIFAG: {TEXT: 'Колифаги.', CELL: 3},
    KLOSTRID: {TEXT: 'Сульфитредуцирующие клостридии.', CELL: 3},
    SALMONELLA: {TEXT: 'Сальмонеллы.', CELL: 3},
    POLIFOSFAT: {TEXT: 'Фосфат-ион', CELL: 3},
    APAV: {TEXT: 'АПАВ', CELL: 3},
    FENOL: {TEXT: 'Фенолы', CELL: 3},
    SULFAT: {TEXT: 'Сульфат', CELL: 3},
    RTUT: {TEXT: 'Ртуть', CELL: 3},
    BOR: {TEXT: 'Массовая концентрация бора', CELL: 3},
    KREMNIY: {TEXT: 'Lorem Ipsum', CELL: 3},
    MISHYAK: {TEXT: 'Мышьяк', CELL: 3},
    FTOR: {TEXT: 'Фторид-ион', CELL: 3},
    BROM: {TEXT: 'Lorem Ipsum', CELL: 3},
    LITIY: {TEXT: 'Ионы лития', CELL: 3},
    BARIY: {TEXT: 'Lorem Ipsum', CELL: 3},
    BERILLIY: {TEXT: 'Lorem Ipsum', CELL: 3},
    SELEN: {TEXT: 'Lorem Ipsum', CELL: 3},
    STRONCIY: {TEXT: 'Lorem Ipsum', CELL: 3},
    LINDAN: {TEXT: 'Lorem Ipsum', CELL: 3},
    D_24: {TEXT: 'Lorem Ipsum', CELL: 3},
    NIKEL: {TEXT: 'Массовая концентрация никеля', CELL: 3},
    KADMIY: {TEXT: 'Кадмий', CELL: 3},
    GIDROKARBONAT: {TEXT: 'Lorem Ipsum', CELL: 3},
    XPK: {TEXT: 'ХПК', CELL: 3},
    BPK: {TEXT: 'Lorem Ipsum', CELL: 3},
    GELMINT: {TEXT: 'Яйца, личинки гельминтов', CELL: 3},
    LYAMBLIY: {TEXT: 'Цисты лямблий', CELL: 3},
    RADON: {TEXT: 'Удельная активность Rn-222', CELL: 3},
    ALPHA: {TEXT: 'Удельная суммарная альфа- активность', CELL: 3},
    BETTA: {TEXT: 'Удельная суммарная бета- активность', CELL: 3},
    RASTV_KISLOROD: {TEXT: 'Растворенный кислород', CELL: 3},
    KOBALT: {TEXT: 'Массовая концентрация кобальта', CELL: 3},
    HROM: {TEXT: 'Хром общий', CELL: 3},
    MAGNIY: {TEXT: 'Ионы магния', CELL: 3},
    BPK_POLN: {TEXT: 'Биохимическое потребление кислорода после n-дней инкубации / БПК полн', CELL: 3},
    CISTI: {TEXT: 'Цисты кишечных простейших', CELL: 3},
    ZHIZN_GELMINT: {TEXT: 'Жизнеспособные яйца гельминтов (аскарид, власоглав, токсокар, фасциол), онкосферы тениид и жизнеспособные цисты патогенных кишечных простейших', CELL: 3},
    SHELOCH: {TEXT: 'Lorem Ipsum', CELL: 3}
}

