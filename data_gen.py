"""
FAKE DATA GEN - Fake data generator using Faker library.
Version: 1.0
by k1y0miiii (◕‿◕)
"""

import os
import sys
import csv
import requests
from faker import Faker
from pyfiglet import Figlet
from colorama import Fore, Style, init


# Установка размера консоли для Windows, Linux и macOS
if os.name == "nt":
    os.system("mode con: cols=110 lines=44")
elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
    os.system('printf "\033[8;44;110t"')

init(autoreset=True)


def determine_menu_language():
    """
    Определяет язык для меню по IP-адресу.
    Если страна — Россия, возвращается "ru".
    Если Китай — "zh".
    Если Корея — "ko".
    Для остальных стран — "en".
    Если интернет недоступен, запрашивает выбор языка у пользователя.
    """
    try:
        response = requests.get("http://ip-api.com/json/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            country_code = data.get("countryCode", "").upper()
            print("IP:", data.get("country", "Неизвестно"))
            if country_code == "RU":
                return "ru"
            elif country_code == "CN":
                return "zh"
            elif country_code == "KR":
                return "ko"
            else:
                return "en"
        else:
            raise Exception("Error receiving data")
    except Exception:
        print("There is no internet connection or an error occurred in country detection.")
        print("Please select the language manually:")
        print("1 - Русское меню")
        print("2 - English menu")
        print("3 - 中文菜单")
        print("4 - 한국어 메뉴")
        user_input = input("Enter your choice: ").strip()
        if user_input == "1":
            return "ru"
        elif user_input == "2":
            return "en"
        elif user_input == "3":
            return "zh"
        elif user_input == "4":
            return "ko"
        else:
            print("Incorrect selection, English default is used.")
            return "en"


def print_banner():
    """Выводит баннер с названием программы."""
    f = Figlet(font="big")
    print(Fore.MAGENTA + "-" * 80 + Style.RESET_ALL)
    print(" ")
    print(Fore.CYAN + f.renderText("FAKE DATA GEN"))
    print(Fore.YELLOW + "v 1.0" + " " * 10 + "by k1y0miiii (◕‿◕)\n")
    print(Fore.MAGENTA + "-" * 80 + Style.RESET_ALL)


def show_menu_ru():
    """Выводит меню на русском языке."""
    menu_items = [
        ("1", "ФИО"), ("2", "Муж ФИО"), ("3", "Жен ФИО"),
        ("4", "Профессия"), ("5", "Номер телефона"), ("6", "Сайт"),
        ("7", "Почта"), ("8", "Ссылка"), ("9", "Компания"),
        ("10", "Муж префикс"), ("11", "Муж фамилия"), ("12", "Муж имя"),
        ("13", "Муж отчество"), ("14", "Жен префикс"), ("15", "Жен фамилия"),
        ("16", "Жен имя"), ("17", "Жен отчество"), ("18", "Индекс"),
        ("19", "Название улицы"), ("20", "Адрес на улице"),("21", "Название страны"),
        ("22", "Название города"), ("23", "Полный адрес"),("-h", "Помощь")
    ]
    col_width = 30
    separator = Fore.BLUE + "│" + Fore.WHITE
    horizontal_line = Fore.BLUE + "╟" + "─" * (col_width * 3 + 1) + "╢"
    print(Fore.BLUE + "╓" + "─" * (col_width * 3 + 1) + "╖")
    print(
        Fore.BLUE + "║" + Fore.CYAN +
        " Выберите данные для генерации:".center(col_width * 3 + 1) +
        Fore.BLUE + "║"
    )
    print(horizontal_line)
    for i in range(0, len(menu_items), 4):
        row = []
        for item in menu_items[i:i + 4]:
            if item:
                num, text = item
                cell = f"{Fore.YELLOW}{num}{Fore.WHITE}. {text}"
                row.append(cell.ljust(col_width))
            else:
                row.append(" " * col_width)
        line = separator.join(row)
        print(Fore.BLUE + "║ " + Fore.WHITE + line + Fore.BLUE + " " * 6 + " ║")
        if i + 3 < len(menu_items):
            print(horizontal_line)
    print(Fore.BLUE + "╙" + "─" * (col_width * 3 + 1) + "╜" + Style.RESET_ALL)


def show_menu_en():
    """Выводит меню на английском языке."""
    menu_items = [
        ("1", "Full Name"), ("2", "Male Full Name"), ("3", "Female Full Name"),
        ("4", "Profession        "), ("5", "Phone Number"), ("6", "Website"),
        ("7", "Email"), ("8", "Link              "), ("9", "Company"),
        ("10", "Male Prefix"), ("11", "Male Last Name"), ("12", "Male First Name  "),
        ("13", "Male Patronymic"), ("14", "Female Prefix"), ("15", "Female Last Name"),
        ("16", "Female First Name"), ("17", "Female Patronymic"), ("18", "ZIP Code"),
        ("19", "Street Name"), ("20", "Street Address"), ("21", "Country Name"),
        ("22", "City Name"), ("23", "Full Address"), ("-h", "Help             ")
    ]
    col_width = 30
    separator = Fore.BLUE + "│" + Fore.WHITE
    horizontal_line = Fore.BLUE + "╟" + "─" * (col_width * 3 + 1) + "╢"
    print(Fore.BLUE + "╓" + "─" * (col_width * 3 + 1) + "╖")
    print(
        Fore.BLUE + "║" + Fore.CYAN +
        " Select data for generation:".center(col_width * 3 + 1) +
        Fore.BLUE + "║"
    )
    print(horizontal_line)
    for i in range(0, len(menu_items), 4):
        row = []
        for item in menu_items[i:i + 4]:
            if item:
                num, text = item
                cell = f"{Fore.YELLOW}{num}{Fore.WHITE}. {text}"
                row.append(cell.ljust(col_width))
            else:
                row.append(" " * col_width)
        line = separator.join(row)
        print(Fore.BLUE + "║ " + Fore.WHITE + line + Fore.BLUE + " " * 5 + " ║")
        if i + 3 < len(menu_items):
            print(horizontal_line)
    print(Fore.BLUE + "╙" + "─" * (col_width * 3 + 1) + "╜" + Style.RESET_ALL)


def show_menu_cn():
    """Выводит меню на китайском языке."""
    menu_items = [
        ("1", "全名"), ("2", "男性全名"), ("3", "女性全名"),
        ("4", "职业"), ("5", "电话号码"), ("6", "网站"),
        ("7", "电子邮件"), ("8", "链接"), ("9", "公司"),
        ("10", "男性前缀"), ("11", "男性姓氏"), ("12", "男性名字"),
        ("13", "男性父称"), ("14", "女性前缀"), ("15", "女性姓氏"),
        ("16", "女性名字"), ("17", "女性父称"), ("18", "邮政编码"),
        ("19", "街道名称"), ("20", "街道地址"), ("21", "国家名称"),
        ("22", "城市名称"), ("23", "完整地址"), ("-h", "帮助")
    ]
    col_width = 30
    separator = Fore.BLUE + "│" + Fore.WHITE
    horizontal_line = Fore.BLUE + "╟" + "─" * (col_width * 3 + 1) + "╢"
    print(Fore.BLUE + "╓" + "─" * (col_width * 3 + 1) + "╖")
    print(
        Fore.BLUE + "║" + Fore.CYAN +
        " 请选择要生成的数据:".center(col_width * 3 + 1)
    )
    print(horizontal_line)
    for i in range(0, len(menu_items), 4):
        row = []
        for item in menu_items[i:i + 4]:
            if item:
                num, text = item
                cell = f"{Fore.YELLOW}{num}{Fore.WHITE}. {text}"
                row.append(cell.ljust(col_width))
            else:
                row.append(" " * col_width)
        line = separator.join(row)
        print(Fore.BLUE + "║ " + Fore.WHITE + line + Fore.BLUE + "")
        if i + 3 < len(menu_items):
            print(horizontal_line)
    print(Fore.BLUE + "╙" + "─" * (col_width * 3 + 1) + "╜" + Style.RESET_ALL)


def show_menu_kr():
    """Выводит меню на корейском языке."""
    menu_items = [
        ("1", "전체 이름"), ("2", "남성 전체 이름"), ("3", "여성 전체 이름"),
        ("4", "직업"), ("5", "전화번호"), ("6", "웹사이트"),
        ("7", "이메일"), ("8", "링크"), ("9", "회사"),
        ("10", "남성 호칭"), ("11", "남성 성"), ("12", "남성 이름"),
        ("13", "남성 부칭"), ("14", "여성 호칭"), ("15", "여성 성"),
        ("16", "여성 이름"), ("17", "여성 부칭"), ("18", "우편번호"),
        ("19", "거리 이름"), ("20", "거리 주소"), ("21", "국가 이름"),
        ("22", "도시 이름"), ("23", "전체 주소"), ("-h", "도움말")
    ]
    col_width = 30
    separator = Fore.BLUE + "│" + Fore.WHITE
    horizontal_line = Fore.BLUE + "╟" + "─" * (col_width * 3 + 1) + "╢"
    print(Fore.BLUE + "╓" + "─" * (col_width * 3 + 1) + "╖")
    print(
        Fore.BLUE + "║" + Fore.CYAN +
        " 생성을 위한 데이터를 선택하세요:".center(col_width * 3)
    )
    print(horizontal_line)
    for i in range(0, len(menu_items), 4):
        row = []
        for item in menu_items[i:i + 4]:
            if item:
                num, text = item
                cell = f"{Fore.YELLOW}{num}{Fore.WHITE}. {text}"
                row.append(cell.ljust(col_width))
            else:
                row.append(" " * col_width)
        line = separator.join(row)
        print(Fore.BLUE + "║" + Fore.WHITE + line + Fore.BLUE + "")
        if i + 2 < len(menu_items):
            print(horizontal_line)
    print(Fore.BLUE + "╙" + "─" * (col_width * 3 + 1) + "╜" + Style.RESET_ALL)


FIELD_FUNCTIONS_RU = {
    "1": ("ФИО", lambda fake: fake.name()),
    "2": ("Муж ФИО", lambda fake: fake.name()),
    "3": ("Жен ФИО", lambda fake: fake.name()),
    "4": ("Профессия", lambda fake: fake.job()),
    "5": ("Номер телефона", lambda fake: fake.phone_number()),
    "6": ("Сайт", lambda fake: fake.url()),
    "7": ("Почта", lambda fake: fake.email()),
    "8": ("Ссылка", lambda fake: fake.url()),
    "9": ("Компания", lambda fake: fake.company()),
    "10": ("Муж префикс", lambda fake: fake.prefix()),
    "11": ("Муж фамилия", lambda fake: fake.last_name()),
    "12": ("Муж имя", lambda fake: fake.first_name()),
    "13": ("Муж отчество", lambda fake: fake.name()),
    "14": ("Жен префикс", lambda fake: fake.prefix()),
    "15": ("Жен фамилия", lambda fake: fake.last_name()),
    "16": ("Жен имя", lambda fake: fake.first_name()),
    "17": ("Жен отчество", lambda fake: fake.name()),
    "18": ("Индекс", lambda fake: fake.postcode()),
    "19": ("Название улицы", lambda fake: fake.street_name()),
    "20": ("Адрес на улице", lambda fake: fake.street_address()),
    "21": ("Название страны", lambda fake: fake.country()),
    "22": ("Название города", lambda fake: fake.city()),
    "23": ("Полный адрес", lambda fake: fake.address()),
}

FIELD_FUNCTIONS_EN = {
    "1": ("Full Name", lambda fake: fake.name()),
    "2": ("Male Full Name", lambda fake: fake.name()),
    "3": ("Female Full Name", lambda fake: fake.name()),
    "4": ("Profession", lambda fake: fake.job()),
    "5": ("Phone Number", lambda fake: fake.phone_number()),
    "6": ("Website", lambda fake: fake.url()),
    "7": ("Email", lambda fake: fake.email()),
    "8": ("Link", lambda fake: fake.url()),
    "9": ("Company", lambda fake: fake.company()),
    "10": ("Male Prefix", lambda fake: fake.prefix()),
    "11": ("Male Surname", lambda fake: fake.last_name()),
    "12": ("Male First Name", lambda fake: fake.first_name()),
    "13": ("Male Patronymic", lambda fake: fake.name()),
    "14": ("Female Prefix", lambda fake: fake.prefix()),
    "15": ("Female Surname", lambda fake: fake.last_name()),
    "16": ("Female First Name", lambda fake: fake.first_name()),
    "17": ("Female Patronymic", lambda fake: fake.name()),
    "18": ("ZIP Code", lambda fake: fake.zipcode()),
    "19": ("Street Name", lambda fake: fake.street_name()),
    "20": ("Street Address", lambda fake: fake.street_address()),
    "21": ("Country Name", lambda fake: fake.country()),
    "22": ("City Name", lambda fake: fake.city()),
    "23": ("Full Address", lambda fake: fake.address()),
}

FIELD_FUNCTIONS_CN = {
    "1": ("姓名", lambda fake: fake.name()),
    "2": ("男士姓名", lambda fake: fake.name()),
    "3": ("女士姓名", lambda fake: fake.name()),
    "4": ("职业", lambda fake: fake.job()),
    "5": ("电话号码", lambda fake: fake.phone_number()),
    "6": ("网站", lambda fake: fake.url()),
    "7": ("邮箱", lambda fake: fake.email()),
    "8": ("链接", lambda fake: fake.url()),
    "9": ("公司", lambda fake: fake.company()),
    "10": ("男士前缀", lambda fake: fake.prefix()),
    "11": ("男士姓氏", lambda fake: fake.last_name()),
    "12": ("男士名字", lambda fake: fake.first_name()),
    "13": ("男士父名", lambda fake: fake.name()),
    "14": ("女士前缀", lambda fake: fake.prefix()),
    "15": ("女士姓氏", lambda fake: fake.last_name()),
    "16": ("女士名字", lambda fake: fake.first_name()),
    "17": ("女士父名", lambda fake: fake.name()),
    "18": ("邮政编码", lambda fake: fake.postcode()),
    "19": ("街道名称", lambda fake: fake.street_name()),
    "20": ("街道地址", lambda fake: fake.street_address()),
    "21": ("国家名称", lambda fake: fake.country()),
    "22": ("城市名称", lambda fake: fake.city()),
    "23": ("完整地址", lambda fake: fake.address()),
}

FIELD_FUNCTIONS_KO = {
    "1": ("성명", lambda fake: fake.name()),
    "2": ("남성 성명", lambda fake: fake.name()),
    "3": ("여성 성명", lambda fake: fake.name()),
    "4": ("직업", lambda fake: fake.job()),
    "5": ("전화번호", lambda fake: fake.phone_number()),
    "6": ("웹사이트", lambda fake: fake.url()),
    "7": ("이메일", lambda fake: fake.email()),
    "8": ("링크", lambda fake: fake.url()),
    "9": ("회사", lambda fake: fake.company()),
    "10": ("남성 접두사", lambda fake: fake.prefix()),
    "11": ("남성 성", lambda fake: fake.last_name()),
    "12": ("남성 이름", lambda fake: fake.first_name()),
    "13": ("남성 아버지 이름", lambda fake: fake.name()),
    "14": ("여성 접두사", lambda fake: fake.prefix()),
    "15": ("여성 성", lambda fake: fake.last_name()),
    "16": ("여성 이름", lambda fake: fake.first_name()),
    "17": ("여성 아버지 이름", lambda fake: fake.name()),
    "18": ("우편번호", lambda fake: fake.postcode()),
    "19": ("거리 이름", lambda fake: fake.street_name()),
    "20": ("거리 주소", lambda fake: fake.street_address()),
    "21": ("국가 이름", lambda fake: fake.country()),
    "22": ("도시 이름", lambda fake: fake.city()),
    "23": ("전체 주소", lambda fake: fake.address()),
}

FIELD_FUNCTIONS = {
    "ru": FIELD_FUNCTIONS_RU,
    "en": FIELD_FUNCTIONS_EN,
    "zh": FIELD_FUNCTIONS_CN,
    "ko": FIELD_FUNCTIONS_KO
}


def generate_data(fake, field_choices, num_records, lang="ru"):
    """
    Генерирует список записей с фейковыми данными.
    :param fake: объект Faker
    :param field_choices: список выбранных номеров полей (строк)
    :param num_records: количество записей
    :param lang: язык ("ru", "en", "zh", "ko")
    :return: список словарей с данными
    """
    data = []
    field_functions = FIELD_FUNCTIONS.get(lang, FIELD_FUNCTIONS_EN)
    for _ in range(num_records):
        record = {}
        for field in field_choices:
            if field in field_functions:
                label, func = field_functions[field]
                record[label] = func(fake)
        data.append(record)
    return data


def export_data(data, export_format):
    """
    Экспортирует данные в выбранном формате.
    Поддерживаемые форматы: csv, txt, mysql, sqlite, postgresql.
    Создаёт папку "gen_data" на рабочем столе и сохраняет в ней файл.
    """
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    output_dir = os.path.join(desktop, "gen_data")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if export_format == "csv":
        file_path = os.path.join(output_dir, "data.csv")
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            if data:
                writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
                writer.writeheader()
                writer.writerows(data)
        print("CSV файл сохранён:", file_path)
    elif export_format == "txt":
        file_path = os.path.join(output_dir, "data.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            for record in data:
                f.write(str(record) + "\n")
        print("TXT файл сохранён:", file_path)
    elif export_format in ("mysql", "sqlite", "postgresql"):
        table_name = "fake_data"
        file_path = os.path.join(output_dir, f"data_{export_format}.sql")
        quote = '"' if export_format == "postgresql" else "`"
        with open(file_path, "w", encoding="utf-8") as f:
            if data:
                columns = list(data[0].keys())
                col_defs = ", ".join(f"{quote}{col}{quote} TEXT" for col in columns)
                f.write(f"CREATE TABLE {table_name} ({col_defs});\n\n")
                for record in data:
                    cols = ", ".join(f"{quote}{col}{quote}" for col in record.keys())
                    vals = ", ".join("'" + str(val).replace("'", "''") + "'" for val in record.values())
                    f.write(f"INSERT INTO {table_name} ({cols}) VALUES ({vals});\n")
        print(f"{export_format.upper()} файл сохранён:", file_path)
    else:
        print("Неизвестный формат экспорта.")



# Текстовые сообщения для разных языков
MESSAGES = {
    "ru": {
        "menu_prompt": "Введите выбор языка (или -h / -help для списка): ",
        "not_found": "Язык не найден. Вы хотите посмотреть настройки языка? (y/n): ",
        "generated": "Сгенерированное имя:",
        "fields_prompt": "Введите номера полей через запятую (например, 1,7,8): ",
        "fields_error": "Некорректный ввод. Попробуйте снова.",
        "num_records_prompt": "Сколько записей сгенерировать? ",
        "num_records_error": "Введите корректное число.",
        "export_format_prompt": "Выберите формат экспорта:",
        "export_format_input": "Введите номер формата: "
    },
    "en": {
        "menu_prompt": "Enter language choice (or -h / -help for list): ",
        "not_found": "Language not found. Do you want to see language settings? (y/n): ",
        "generated": "Generated name:",
        "fields_prompt": "Enter field numbers separated by commas (e.g., 1,7,8): ",
        "fields_error": "Invalid input. Please try again.",
        "num_records_prompt": "How many records to generate? ",
        "num_records_error": "Enter a valid number.",
        "export_format_prompt": "Select export format:",
        "export_format_input": "Enter the format number: "
    },
    "zh": {
        "menu_prompt": "请输入语言选择（或 -h / -help 查看列表）: ",
        "not_found": "未找到语言。您想查看语言设置吗？(y/n): ",
        "generated": "生成的姓名:",
        "fields_prompt": "请输入字段编号，以逗号分隔（例如：1,7,8）: ",
        "fields_error": "输入无效，请重试。",
        "num_records_prompt": "生成多少条记录？ ",
        "num_records_error": "请输入正确的数字。",
        "export_format_prompt": "请选择导出格式:",
        "export_format_input": "请输入格式编号: "
    },
    "ko": {
        "menu_prompt": "언어 선택을 입력하세요 (-h / -help 목록 표시): ",
        "not_found": "언어를 찾을 수 없습니다. 언어 설정을 보시겠습니까? (y/n): ",
        "generated": "생성된 이름:",
        "fields_prompt": "쉼표로 구분된 필드 번호를 입력하세요 (예: 1,7,8): ",
        "fields_error": "잘못된 입력입니다. 다시 시도하세요.",
        "num_records_prompt": "생성할 레코드 수를 입력하세요: ",
        "num_records_error": "올바른 숫자를 입력하세요.",
        "export_format_prompt": "내보내기 형식을 선택하세요:",
        "export_format_input": "형식 번호를 입력하세요: "
    }
}


def generate_faker_data(lang_choice):
    """
    Возвращает объект Faker на основе выбора языка.
    Если пользователь вводит '-h' или '-help', выводится справочное меню
    и запрашивается новый ввод.
    """
    lang_choice = str(lang_choice).lower().strip()

    if lang_choice in ("-h", "-help"):
        print("\nДоступные языки:")
        mapping = {
            # Арабский
            ("1", "عام", "ar_aa"): "ar_AA",
            ("2", "الإمارات العربية المتحدة", "ar_ae"): "ar_AE",
            ("3", "البحرين", "ar_bh"): "ar_BH",
            ("4", "مصر", "ar_eg"): "ar_EG",
            ("5", "الأردن", "ar_jo"): "ar_JO",
            ("6", "فلسطين", "ar_ps"): "ar_PS",
            ("7", "المملكة العربية السعودية", "ar_sa"): "ar_SA",
            # Азербайджанский
            ("8", "Azərbaycan dili", "az_az"): "az_AZ",
            # Болгарский
            ("9", "български", "bg_bg"): "bg_BG",
            # Бенгальский
            ("10", "বাংলা", "bn_bd"): "bn_BD",
            # Боснийский
            ("11", "bosanski jezik", "bs_ba"): "bs_BA",
            # Чешский
            ("12", "čeština", "cs_cz"): "cs_cz",
            # Датский
            ("13", "dansk", "da_dk"): "da_dk",
            # Немецкий
            ("14", "Deutsch", "de"): "de",
            ("15", "Deutsch (Österreich)", "de_at"): "de_at",
            ("16", "Deutsch (Schweiz)", "de_ch"): "de_ch",
            ("17", "Deutsch (Deutschland)", "de_de"): "de_de",
            # Греческий
            ("18", "ελληνικά (Κύπρος)", "el_cy"): "el_cy",
            ("19", "ελληνικά (Ελλάδα)", "el_gr"): "el_gr",
            # Английский
            ("20", "english", "en"): "en",
            ("21", "english (australia)", "en_au"): "en_au",
            ("22", "english (bangladesh)", "en_bd"): "en_bd",
            ("23", "english (canada)", "en_ca"): "en_ca",
            ("24", "english (united kingdom)", "en_gb", "uk"): "en_gb",
            ("25", "english (ireland)", "en_ie"): "en_ie",
            ("26", "english (india)", "en_in"): "en_in",
            ("27", "english (montserrat)", "en_ms"): "en_ms",
            ("28", "english (new zealand)", "en_nz"): "en_nz",
            ("29", "english (philippines)", "en_ph"): "en_ph",
            ("30", "english (pakistan)", "en_pk"): "en_pk",
            ("31", "english (thailand)", "en_th"): "en_th",
            ("32", "english (united states)", "en_us", "usa", "united states"): "en_us",
            # Испанский
            ("33", "español", "es"): "es",
            ("34", "español (argentina)", "es_ar"): "es_ar",
            ("35", "español (canadá)", "es_ca"): "es_ca",
            ("36", "español (chile)", "es_cl"): "es_cl",
            ("37", "español (colombia)", "es_co"): "es_co",
            ("38", "español (españa)", "es_es", "espana"): "es_es",
            ("39", "español (méxico)", "es_mx"): "es_mx",
            # Эстонский
            ("40", "eesti keel", "et_ee"): "et_ee",
            # Персидский
            ("41", "فارسی", "fa_ir"): "fa_ir",
            # Финский
            ("42", "suomi", "fi_fi"): "fi_fi",
            # Филиппинский
            ("43", "filipino", "fil_ph"): "fil_ph",
            # Французский
            ("44", "français (belgique)", "fr_be"): "fr_be",
            ("45", "français (canada)", "fr_ca"): "fr_ca",
            ("46", "français (suisse)", "fr_ch"): "fr_ch",
            ("47", "français (france)", "fr_fr"): "fr_fr",
            ("48", "français (québec)", "fr_qc"): "fr_qc",
            # Ирландский (гэльский)
            ("49", "gaeilge", "ga_ie"): "ga_ie",
            # Гуджарати
            ("50", "ગુજરાતી", "gu_in"): "gu_in",
            # Иврит
            ("51", "עברית", "he_il"): "he_il",
            # Хинди
            ("52", "हिन्दी", "hi_in"): "hi_in",
            # Хорватский
            ("53", "hrvatski", "hr_hr"): "hr_hr",
            # Венгерский
            ("54", "magyar", "hu_hu"): "hu_hu",
            # Армянский
            ("55", "հայերեն", "hy_am"): "hy_am",
            # Индонезийский
            ("56", "bahasa indonesia", "id_id"): "id_id",
            # Итальянский (Швейцария)
            ("57", "italiano (svizzera)", "it_ch"): "it_ch",
            # Итальянский (Италия)
            ("58", "italiano (italia)", "it_it"): "it_it",
            # Японский
            ("59", "日本語", "ja_jp"): "ja_jp",
            # Грузинский
            ("60", "ქართული", "ka_ge"): "ka_ge",
            # Корейский
            ("61", "한국어", "ko_kr"): "ko_kr",
            # Латинский
            ("62", "latina", "la"): "la",
            # Люксембургский
            ("63", "lëtzebuergesch", "lb_lu"): "lb_lu",
            # Литовский
            ("64", "lietuvių", "lt_lt"): "lt_lt",
            # Латышский
            ("65", "latviešu", "lv_lv"): "lv_lv",
            # Мальтийский
            ("66", "malti", "mt_mt"): "mt_mt",
            # Непальский
            ("67", "नेपाली", "ne_np"): "ne_np",
            # Нидерландский (Бельгия)
            ("68", "nederlands (belgië)", "nl_be"): "nl_be",
            # Нидерландский (Нидерланды)
            ("69", "nederlands (nederland)", "nl_nl"): "nl_nl",
            # Норвежский
            ("70", "norsk", "no_no"): "no_no",
            # Одиа
            ("71", "ଓଡ଼ିଆ", "or_in"): "or_in",
            # Польский
            ("72", "polski", "pl_pl"): "pl_pl",
            # Португальский (Бразилия)
            ("73", "português (brasil)", "pt_br"): "pt_br",
            # Португальский (Португалия)
            ("74", "português (portugal)", "pt_pt"): "pt_pt",
            # Румынский
            ("75", "română", "ro_ro"): "ro_ro",
            # Русский
            ("76", "русский", "ru_ru"): "ru_ru",
            # Словацкий
            ("77", "slovenčina", "sk_sk"): "sk_sk",
            # Словенский
            ("78", "slovenščina", "sl_si"): "sl_si",
            # Албанский
            ("79", "shqip", "sq_al"): "sq_al",
            # Шведский
            ("80", "svenska", "sv_se"): "sv_se",
            # Суахили
            ("81", "kiswahili", "sw"): "sw",
            # Тамильский
            ("82", "தமிழ்", "ta_in"): "ta_in",
            # Тайский
            ("83", "ไทย", "th"): "th",
            ("84", "ไทย (ประเทศไทย)", "th_th"): "th_th",
            # Тагальский
            ("85", "tagalog", "tl_ph"): "tl_ph",
            # Турецкий
            ("86", "türkçe", "tr_tr"): "tr_tr",
            # Тви
            ("87", "twi", "tw_gh"): "tw_gh",
            # Украинский
            ("88", "українська", "uk_ua"): "uk_ua",
            # Узбекский
            ("89", "oʻzbek", "uz_uz"): "uz_uz",
            # Вьетнамский
            ("90", "tiếng việt", "vi_vn"): "vi_vn",
            # Йоруба
            ("91", "ède yorùbá", "yo_ng"): "yo_ng",
            # Китайский (упрощённый)
            ("92", "简体中文", "zh_cn"): "zh_cn",
            # Китайский (традиционный)
            ("93", "繁體中文", "zh_tw"): "zh_tw",
            # Зулусский
            ("94", "isizulu", "zu_za"): "zu_za",
        }
        for keys, locale in sorted(mapping.items(), key=lambda x: x[1]):
            print(f"{locale:7}  —  {', '.join(keys)}")
        print()  # Пустая строка после таблицы
        new_input = input("Введите ваш выбор языка: ")
        return generate_faker_data(new_input)

    mapping = {
        # Тот же словарь, что и выше
        ("1", "عام", "ar_aa"): "ar_AA",
        ("2", "الإمارات العربية المتحدة", "ar_ae"): "ar_AA",
        ("3", "البحرين", "ar_bh"): "ar_BH",
        ("4", "مصر", "ar_eg"): "ar_EG",
        ("5", "الأردن", "ar_jo"): "ar_JO",
        ("6", "فلسطين", "ar_ps"): "ar_PS",
        ("7", "المملكة العربية السعودية", "ar_sa"): "ar_SA",
        ("8", "Azərbaycan dili", "az_az"): "az_AZ",
        ("9", "български", "bg_bg"): "bg_BG",
        ("10", "বাংলা", "bn_bd"): "bn_BD",
        ("11", "bosanski jezik", "bs_ba"): "bs_BA",
        ("12", "čeština", "cs_cz"): "cs_cz",
        ("13", "dansk", "da_dk"): "da_dk",
        ("14", "Deutsch", "de"): "de",
        ("15", "Deutsch (Österreich)", "de_at"): "de_at",
        ("16", "Deutsch (Schweiz)", "de_ch"): "de_ch",
        ("17", "Deutsch (Deutschland)", "de_de"): "de_de",
        ("18", "ελληνικά (Κύπρος)", "el_cy"): "el_cy",
        ("19", "ελληνικά (Ελλάδα)", "el_gr"): "el_gr",
        ("20", "english", "en"): "en",
        ("21", "english (australia)", "en_au"): "en_au",
        ("22", "english (bangladesh)", "en_bd"): "en_bd",
        ("23", "english (canada)", "en_ca"): "en_ca",
        ("24", "english (united kingdom)", "en_gb", "uk"): "en_gb",
        ("25", "english (ireland)", "en_ie"): "en_ie",
        ("26", "english (india)", "en_in"): "en_in",
        ("27", "english (montserrat)", "en_ms"): "en_ms",
        ("28", "english (new zealand)", "en_nz"): "en_nz",
        ("29", "english (philippines)", "en_ph"): "en_ph",
        ("30", "english (pakistan)", "en_pk"): "en_pk",
        ("31", "english (thailand)", "en_th"): "en_th",
        ("32", "english (united states)", "en_us", "usa", "united states"): "en_us",
        ("33", "español", "es"): "es",
        ("34", "español (argentina)", "es_ar"): "es_ar",
        ("35", "español (canadá)", "es_ca"): "es_ca",
        ("36", "español (chile)", "es_cl"): "es_cl",
        ("37", "español (colombia)", "es_co"): "es_co",
        ("38", "español (españa)", "es_es", "espana"): "es_es",
        ("39", "español (méxico)", "es_mx"): "es_mx",
        ("40", "eesti keel", "et_ee"): "et_ee",
        ("41", "فارسی", "fa_ir"): "fa_ir",
        ("42", "suomi", "fi_fi"): "fi_fi",
        ("43", "filipino", "fil_ph"): "fil_ph",
        ("44", "français (belgique)", "fr_be"): "fr_be",
        ("45", "français (canada)", "fr_ca"): "fr_ca",
        ("46", "français (suisse)", "fr_ch"): "fr_ch",
        ("47", "français (france)", "fr_fr"): "fr_fr",
        ("48", "français (québec)", "fr_qc"): "fr_qc",
        ("49", "gaeilge", "ga_ie"): "ga_ie",
        ("50", "ગુજરાતી", "gu_in"): "gu_in",
        ("51", "עברית", "he_il"): "he_il",
        ("52", "हिन्दी", "hi_in"): "hi_in",
        ("53", "hrvatski", "hr_hr"): "hr_hr",
        ("54", "magyar", "hu_hu"): "hu_hu",
        ("55", "հայերեն", "hy_am"): "hy_am",
        ("56", "bahasa indonesia", "id_id"): "id_id",
        ("57", "italiano (svizzera)", "it_ch"): "it_ch",
        ("58", "italiano (italia)", "it_it"): "it_it",
        ("59", "日本語", "ja_jp"): "ja_jp",
        ("60", "ქართული", "ka_ge"): "ka_ge",
        ("61", "한국어", "ko_kr"): "ko_kr",
        ("62", "latina", "la"): "la",
        ("63", "lëtzebuergesch", "lb_lu"): "lb_lu",
        ("64", "lietuvių", "lt_lt"): "lt_lt",
        ("65", "latviešu", "lv_lv"): "lv_lv",
        ("66", "malti", "mt_mt"): "mt_mt",
        ("67", "नेपाली", "ne_np"): "ne_np",
        ("68", "nederlands (belgië)", "nl_be"): "nl_be",
        ("69", "nederlands (nederland)", "nl_nl"): "nl_nl",
        ("70", "norsk", "no_no"): "no_no",
        ("71", "ଓଡ଼ିଆ", "or_in"): "or_in",
        ("72", "polski", "pl_pl"): "pl_pl",
        ("73", "português (brasil)", "pt_br"): "pt_br",
        ("74", "português (portugal)", "pt_pt"): "pt_pt",
        ("75", "română", "ro_ro"): "ro_ro",
        ("76", "русский", "ru_ru"): "ru_ru",
        ("77", "slovenčina", "sk_sk"): "sk_sk",
        ("78", "slovenščina", "sl_si"): "sl_si",
        ("79", "shqip", "sq_al"): "sq_al",
        ("80", "svenska", "sv_se"): "sv_se",
        ("81", "kiswahili", "sw"): "sw",
        ("82", "தமிழ்", "ta_in"): "ta_in",
        ("83", "ไทย", "th"): "th",
        ("84", "ไทย (ประเทศไทย)", "th_th"): "th_th",
        ("85", "tagalog", "tl_ph"): "tl_ph",
        ("86", "türkçe", "tr_tr"): "tr_tr",
        ("87", "twi", "tw_gh"): "tw_gh",
        ("88", "українська", "uk_ua"): "uk_ua",
        ("89", "oʻzbek", "uz_uz"): "uz_uz",
        ("90", "tiếng việt", "vi_vn"): "vi_vn",
        ("91", "ède yorùbá", "yo_ng"): "yo_ng",
        ("92", "简体中文", "zh_cn"): "zh_cn",
        ("93", "繁體中文", "zh_tw"): "zh_tw",
        ("94", "isizulu", "zu_za"): "zu_za",
    }
    for keys, locale in mapping.items():
        if lang_choice in keys:
            return Faker(locale)
    return Faker("en")


def query_data_fields(msg):
    """
    Запрашивает у пользователя номера полей для генерации и количество записей.
    :param msg: словарь с текстовыми сообщениями для выбранного языка
    :return: кортеж (список выбранных полей, количество записей)
    """
    while True:
        fields_input = input(msg["fields_prompt"])
        field_choices = [s.strip() for s in fields_input.split(",") if s.strip()]
        if field_choices:
            break
        else:
            print(msg["fields_error"])
    while True:
        try:
            num_records = int(input(msg["num_records_prompt"]))
            break
        except ValueError:
            print(msg["num_records_error"])
    return field_choices, num_records


def query_export_format(msg):
    """Запрашивает у пользователя формат экспорта данных."""
    print(msg["export_format_prompt"])
    print("1 - CSV")
    print("2 - TXT")
    print("3 - MySQL")
    print("4 - SQLite")
    print("5 - PostgreSQL")
    choice = input(msg["export_format_input"]).strip()
    mapping = {
        "1": "csv",
        "2": "txt",
        "3": "mysql",
        "4": "sqlite",
        "5": "postgresql"
    }
    return mapping.get(choice, "csv")


# Текстовые сообщения для финального вывода и запросов по языкам
MESSAGES = {
    "ru": {
        "menu_prompt": "Введите выбор языка (или -h / -help для списка): ",
        "not_found": "Язык не найден. Вы хотите посмотреть настройки языка? (y/n): ",
        "generated": "Сгенерированное имя:",
        "fields_prompt": "Введите номера полей через запятую (например, 1,7,8): ",
        "fields_error": "Некорректный ввод. Попробуйте снова.",
        "num_records_prompt": "Сколько записей сгенерировать? ",
        "num_records_error": "Введите корректное число.",
        "export_format_prompt": "Выберите формат экспорта:",
        "export_format_input": "Введите номер формата: "
    },
    "en": {
        "menu_prompt": "Enter language choice (or -h / -help for list): ",
        "not_found": "Language not found. Do you want to see language settings? (y/n): ",
        "generated": "Generated name:",
        "fields_prompt": "Enter field numbers separated by commas (e.g., 1,7,8): ",
        "fields_error": "Invalid input. Please try again.",
        "num_records_prompt": "How many records to generate? ",
        "num_records_error": "Enter a valid number.",
        "export_format_prompt": "Select export format:",
        "export_format_input": "Enter the format number: "
    },
    "zh": {
        "menu_prompt": "请输入语言选择（或 -h / -help 查看列表）: ",
        "not_found": "未找到语言。您想查看语言设置吗？(y/n): ",
        "generated": "生成的姓名:",
        "fields_prompt": "请输入字段编号，以逗号分隔（例如：1,7,8）: ",
        "fields_error": "输入无效，请重试。",
        "num_records_prompt": "生成多少条记录？ ",
        "num_records_error": "请输入正确的数字。",
        "export_format_prompt": "请选择导出格式:",
        "export_format_input": "请输入格式编号: "
    },
    "ko": {
        "menu_prompt": "언어 선택을 입력하세요 (-h / -help 목록 표시): ",
        "not_found": "언어를 찾을 수 없습니다. 언어 설정을 보시겠습니까? (y/n): ",
        "generated": "생성된 이름:",
        "fields_prompt": "쉼표로 구분된 필드 번호를 입력하세요 (예: 1,7,8): ",
        "fields_error": "잘못된 입력입니다. 다시 시도하세요.",
        "num_records_prompt": "생성할 레코드 수를 입력하세요: ",
        "num_records_error": "올바른 숫자를 입력하세요.",
        "export_format_prompt": "내보내기 형식을 선택하세요:",
        "export_format_input": "형식 번호를 입력하세요: "
    }
}


def main():
    print_banner()
    lang = determine_menu_language()
    print(f"Menu lang: {lang}")

    current_lang = lang if lang in MESSAGES else "en"

    # Отобразим меню в зависимости от выбранного языка
    if current_lang == "ru":
        show_menu_ru()
    elif current_lang == "zh":
        show_menu_cn()
    elif current_lang == "ko":
        show_menu_kr()
    else:
        show_menu_en()

    # Запрашиваем выбор языка для генерации данных в цикле
    while True:
        user_choice = input(MESSAGES[current_lang]["menu_prompt"])
        if user_choice == "-q":
            print("byebye...")
            sys.exit(0)
        fake = generate_faker_data(user_choice)
        if fake is not None:
            break
        else:
            answer = input(MESSAGES[current_lang]["not_found"]).lower().strip()
            if answer == "-q":
                print("byebye...")
                sys.exit(0)
            if answer == "y":
                fake = generate_faker_data("-h")
                if fake is not None:
                    break


    print(f"{MESSAGES[current_lang]['generated']} {fake.name()}")

    # Запрашиваем, какие данные генерировать и их количество
    field_choices, num_records = query_data_fields(MESSAGES[current_lang])

    # Генерируем данные (используем текущий язык для выбора функций)
    data = generate_data(fake, field_choices, num_records, current_lang)

    # Запрашиваем формат экспорта
    export_format = query_export_format(MESSAGES[current_lang])

    # Экспортируем данные
    export_data(data, export_format)


if __name__ == "__main__":
    main()
