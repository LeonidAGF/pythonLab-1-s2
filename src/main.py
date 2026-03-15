from SourceFromFile import SourceFromFile
from SourceFromGenerator import SourceFromGenerator
from SourceFromWeb import SourceFromWeb
from task_manager import task_manager

def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    source_from_web1 = SourceFromWeb("https://my.meteoblue.com/packages/basic-1h_basic-day?apikey=bOico7hWTVAzPQYM&lat=55.752&lon=37.6178&asl=155&format=json")
    source_from_web2 = SourceFromWeb("https://ru.wikipedia.org/wiki/Python")
    source_from_file = SourceFromFile("text")
    source_from_generators = SourceFromGenerator(1)

    print("Tasks from web:")

    for el in task_manager(source_from_web1):
        print(el)

    for el in task_manager(source_from_web2):
        print(el)

    print("\n","Tasks from file:")

    for el in task_manager(source_from_file):
        print(el)

    print("\n","Tasks from generators:")

    for el in task_manager(source_from_generators):
        print(el)

if __name__ == "__main__":
    main()
