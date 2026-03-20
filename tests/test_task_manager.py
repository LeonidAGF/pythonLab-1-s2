from src.Task import Task
from src.SourceFromFile import SourceFromFile
from src.SourceFromGenerator import SourceFromGenerator
from src.SourceFromWeb import SourceFromWeb
from src.task_manager import task_manager

def test_task_manager():
    """
        Тесты для task_manager
    """
    source_from_web = SourceFromWeb("https://ru.wikipedia.org/wiki/Python")
    source_from_file = SourceFromFile("text")
    source_from_generators = SourceFromGenerator(1)
    task:Task = Task(1,{})

    try:
        task_manager(source_from_web)
        task_manager(source_from_file)
        task_manager(source_from_generators)
        assert True
    except Exception:
        assert False

    try:
        task_manager(task)
        assert False
    except Exception:
        assert True
