from pathlib import Path


def change_file_permissions(file_path, mode):
    file_path = Path(file_path)
    try:
        file_path.chmod(mode)
        print(f"Права доступа к файлу {file_path} успешно изменены на {oct(mode)}")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except PermissionError:
        print(f"Нет прав для изменения прав доступа к файлу {file_path}.")


if __name__ == '__main__':

    # Установить права на чтение, запись и выполнение для владельца, только чтение для группы и других
    change_file_permissions('/Volumes/big4photo-4/selenium_downloads/keyword__KSP_016778/KSP_016778_00109_1h.jpg', 0o777)
