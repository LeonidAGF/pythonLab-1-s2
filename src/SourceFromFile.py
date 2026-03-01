import random
from Task import Task
from cat_function import cat


class SourceFromFile:
    """

    """
    def __init__(self,path:str,seed=None) -> None:
        """

        """
        self.path = path
        self.seed = seed

    def get_tasks(self) -> list[Task]:
        """

        """
        tasks: list[Task] = []
        random.seed(None)
        if self.seed is not None:
            random.seed(self.seed)
        try:
            data = {}
            data["text"] =cat(self.path)
            task = Task(random.randint(10000, 99999), data)
            tasks.append(task)
        except Exception:
            random.seed(None)
            raise Exception
        random.seed(None)
        return tasks
