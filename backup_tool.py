import os
import shutil
import datetime

def create_backup(source_dir, backup_dir):
    """
    Функція для створення резервної копії вказаної директорії у форматі ZIP.
    """
    # Перевіряємо, чи існує папка, яку ми хочемо скопіювати
    if not os.path.exists(source_dir):
        print(f"Помилка: Вихідна папка '{source_dir}' не знайдена.")
        return

    # Перевіряємо, чи існує папка для збереження копій. Якщо ні — створюємо її
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print(f"Створено нову директорію для резервних копій: '{backup_dir}'")

    # Отримуємо поточну дату та час для унікальної назви файлу
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Витягуємо базову назву вихідної папки
    base_folder_name = os.path.basename(os.path.normpath(source_dir))
    if not base_folder_name:
        base_folder_name = "backup"
    
    # Формуємо повний шлях та назву майбутнього архіву
    archive_name = f"{base_folder_name}_{current_time}"
    archive_path = os.path.join(backup_dir, archive_name)

    print(f"Починаю створення резервної копії для директорії '{source_dir}'...")
    
    # Виконуємо архівування з обробкою можливих помилок
    try:
        shutil.make_archive(base_name=archive_path, format='zip', root_dir=source_dir)
        print(f"Успіх! Резервну копію збережено за адресою: {archive_path}.zip")
    except Exception as e:
        print(f"Виникла помилка під час архівування: {e}")

if __name__ == "__main__":
    # Налаштовуємо назви папок для нашого практичного прикладу
    test_source = "my_project_files"
    test_backup = "my_backups"
    
    # Створюємо тестові дані, щоб скрипт мав реальні файли для копіювання
    if not os.path.exists(test_source):
        os.makedirs(test_source)
        with open(os.path.join(test_source, "example_data.txt"), "w", encoding="utf-8") as file:
            file.write("Це тестовий файл для перевірки роботи нашого скрипта резервного копіювання.")
        print(f"Створено тестову папку '{test_source}' з файлом всередині.")
    
    # Виклик головної функції
    create_backup(test_source, test_backup)
