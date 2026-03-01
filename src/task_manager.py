import Source
from Task import Task

def task_manager(source: Source.TaskSource) -> list[Task]:
    """

    """
    if isinstance(source, Source.TaskSource):
        return source.get_tasks()
    raise TypeError
