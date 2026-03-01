from Task import Task
import random

from generator import get_new_str


class SourceFromWeb:
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

        random.seed(None)
        if self.seed is not None:
            random.seed(self.seed)

        tasks:list[Task] = []

        for col in range(0,random.randint(5, 25)):
            data = {}
            data["name"] = get_new_str()
            el = Task(random.randint(10000, 99999),data)
            tasks.append(el)

        random.seed(None)

        return tasks
