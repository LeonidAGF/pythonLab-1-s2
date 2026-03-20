from src.Source import TaskSource
from src.Task import Task

def task_manager(source: TaskSource) -> list[Task]:
    """
        Функция получения задач из источника любого типа
    """
    if isinstance(source, TaskSource):
        return source.get_tasks()
    raise TypeError
