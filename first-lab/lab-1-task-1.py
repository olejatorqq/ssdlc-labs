import psutil
import json
import os
import xml.etree.ElementTree as ET
import zipfile

def separator():
    print("-" * 40)

def print_task_header(task_number, task_description):
    print(f"Задание {task_number}. {task_description}")

# 1. Вывести информацию в консоль о логических дисках, именах, метке тома, размере и типе файловой системы
def get_disk_info():
    separator()
    print_task_header(1, "Информация о дисках")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print("Устройство:", partition.device)
        print("Точка монтирования:", partition.mountpoint)
        print("Тип файловой системы:", partition.fstype)
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            total_gb = partition_usage.total / (1024 ** 3)
            used_gb = partition_usage.used / (1024 ** 3)
            free_gb = partition_usage.free / (1024 ** 3)
            print("Общий размер:", round(total_gb, 2), "ГБ")
            print("Использовано:", round(used_gb, 2), "ГБ")
            print("Свободно:", round(free_gb, 2), "ГБ")
            print("Процент использования:", round(partition_usage.percent, 2), "%")
        except PermissionError:
            print("Отказано в доступе к", partition.mountpoint)
    separator()

# 2. Работа с файлами
def file_operations():
    separator()
    print_task_header(2, "Работа с файлами")
    # Запрашиваем у пользователя имя файла
    file_name = input("Введите имя файла (включая расширение): ")

    try:
        if "." not in file_name:
            raise ValueError("Имя файла должно включать расширение (например, '.txt')")
        # Создаем файл
        with open(file_name, "w") as file:
            print("Файл создан:", file_name)
        # Записываем в файл строку, введенную пользователем
        user_input = input("Введите строку для записи в файл: ")
        with open(file_name, "a") as file:
            file.write(user_input + "\n")
            print("\nСтрока записана в файл")
        # Читаем файл и выводим его содержимое в консоль
        with open(file_name, "r") as file:
            file_contents = file.read()
            print("\nСодержимое файла:")
            print(file_contents)

        delete_file = input("\nУдалить файл? (да/нет): ").lower()
        if delete_file == 'да':
            os.remove(file_name)
            print(f"Файл '{file_name}' удален.")
        else:
            print(f"Файл '{file_name}' не удален.")
    except ValueError as e:
        print(f"Ошибка: {e}")
    separator()

# 3. Работа с форматом JSON
def json_operations():
    separator()
    print_task_header(3, "Работа с форматом JSON")

    while True:
        user_data = {}
        user_data["name"] = input("Введите Имя: ")
        user_data["age"] = input("Введите Возраст: ")
        user_data["city"] = input("Введите Город: ")

        try:
            if not user_data["name"].isalpha():
                raise ValueError("Ошибка: Имя должно состоять только из букв.")
            if not user_data["age"].isdigit():
                raise ValueError("Ошибка: Возраст должен быть целым числом.")
            if not user_data["city"].isalpha():
                raise ValueError("Ошибка: Город должен состоять из букв.")

            break
        except ValueError as e:
            print(f"\n{e}")

    json_file_name = "user_data.json"

    with open(json_file_name, "w") as json_file:
        json.dump(user_data, json_file, indent=4)
        print(f"\nJSON-файл создан: {json_file_name}")

    with open(json_file_name, "r") as json_file:
        loaded_data = json.load(json_file)
        print("\nСодержимое JSON-файла:")
        for key, value in loaded_data.items():
            print(f"{key}: {value}")

    delete_file = input("\nУдалить JSON-файл? (да/нет): ").lower()
    if delete_file == 'да':
        os.remove(json_file_name)
        print(f"JSON-файл '{json_file_name}' удален.")
    else:
        print(f"JSON-файл '{json_file_name}' не удален.")

    separator()

# 4. Работа с форматом XML
def xml_operations():
    separator()
    print_task_header(4, "Работа с форматом XML")

    while True:
        user_data = {}
        user_data["name"] = input("Введите Имя: ")
        user_data["age"] = input("Введите Возраст: ")
        user_data["city"] = input("Введите Город: ")

        try:
            if not user_data["name"].isalpha():
                raise ValueError("Ошибка: Имя должно состоять только из букв.")
            if not user_data["age"].isdigit():
                raise ValueError("Ошибка: Возраст должен быть целым числом.")
            if not user_data["city"].isalpha():
                raise ValueError("Ошибка: Город должен состоять из букв.")

            break
        except ValueError as e:
            print(f"\n{e}")

    xml_file_name = "user_data.xml"
    root = ET.Element("user_data")

    for key, value in user_data.items():
        element = ET.SubElement(root, key)
        element.text = value

    tree = ET.ElementTree(root)
    tree.write(xml_file_name)
    print(f"\nXML-файл создан: {xml_file_name}")

    tree = ET.parse(xml_file_name)
    root = tree.getroot()
    print("\nСодержимое XML-файла:")
    for element in root:
        print(f"{element.tag}: {element.text}")

    delete_file = input("\nУдалить XML-файл? (да/нет): ").lower()
    if delete_file == 'да':
        os.remove(xml_file_name)
        print(f"XML-файл '{xml_file_name}' удален.")
    else:
        print(f"XML-файл '{xml_file_name}' не удален.")

    separator()


# 5. Работа с форматом ZIP
def zip_operations():
    separator()
    print_task_header(5, "Работа с форматом ZIP")
    # Создать архив в формате ZIP
    zip_file_name = "user_archive.zip"
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        pass  # Создаем пустой архив
    print(f"ZIP-архив создан: {zip_file_name}\n")
    # Ввод имени файла для добавления в архив
    user_file_name = input("Введите имя файла для добавления в архив: ")
    if "." not in user_file_name:
        print("Ошибка: Имя файла должно включать расширение (например, '.txt')\n")
        separator()
        return
    # Если файл не существует, создаем его
    if not os.path.exists(user_file_name):
        print(f"Файл '{user_file_name}' не существует. Создаем файл...\n")
        with open(user_file_name, 'w') as new_file:
            pass  # Создаем пустой файл
    # Добавить файл в архив
    with zipfile.ZipFile(zip_file_name, 'a') as zipf:
        zipf.write(user_file_name, os.path.basename(user_file_name))
    print(f"Файл '{user_file_name}' добавлен в архив.")
    # Разархивировать файл и вывести данные о нем
    with zipfile.ZipFile(zip_file_name, 'r') as zipf:
        zipf.extractall()
        extracted_file_name = os.path.basename(user_file_name)
        print(f"Файл '{extracted_file_name}' разархивирован в текущий каталог\n")
        # Выводим информацию о разархивированном файле
        if os.path.exists(extracted_file_name):
            file_size = os.path.getsize(extracted_file_name)
            print(f"Размер разархивированного файла: {file_size} байт\n")
            delete_file = input("Удалить разархивированный файл? (да/нет): ").lower()
            if delete_file == 'да':
                os.remove(extracted_file_name)
                print(f"Файл '{extracted_file_name}' удален.")
            else:
                print(f"Файл '{extracted_file_name}' не удален.")
        else:
            print(f"Файл '{extracted_file_name}' не найден.")
    
    # Удалить ZIP-архив
    os.remove(zip_file_name)
    print(f"ZIP-архив удален: {zip_file_name}")
    separator()

# Главное меню с выбором функции
def main_menu():
    while True:
        print("Главное меню:")
        print("1. Информация о дисках")
        print("2. Работа с файлами")
        print("3. Работа с JSON")
        print("4. Работа с XML")
        print("5. Работа с ZIP")
        print("6. Выход")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == '1':
            get_disk_info()
        elif choice == '2':
            file_operations()
        elif choice == '3':
            json_operations()
        elif choice == '4':
            xml_operations()
        elif choice == '5':
            zip_operations()
        elif choice == '6':
            break
        else:
            print("Некорректный выбор. Выберите пункт от 1 до 6.")

if __name__ == "__main__":
    main_menu()
