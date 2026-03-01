from SourceFromFile import SourceFromFile
from SourceFromGenerator import SourceFromGenerator
from SourceFromWeb import SourceFromWeb
from task_manager import task_manager


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    source_from_web = SourceFromWeb("telegram.com")
    source_from_file = SourceFromFile("./text.txt")
    source_from_generators = SourceFromGenerator(1)

    print("Tasks from web:")

    for el in task_manager(source_from_web):
        print(el)

    print("\n","Tasks from file:")

    for el in task_manager(source_from_file):
        print(el)

    print("\n","Tasks from generators:")

    for el in task_manager(source_from_generators):
        print(el)



if __name__ == "__main__":
    main()
