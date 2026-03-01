def cat(path: str) -> str:
    """
    функция реализующая команду cat, которая выводит в консоль текст файла
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    file_text:str = ''
    try:
        file = open(path, 'r')
        file_text = file.read()
        file.close()
    except Exception:
        return 'error'
    return file_text
