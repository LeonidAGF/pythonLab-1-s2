from Task import Task
import random
import requests

class SourceFromWeb:
    """

    """
    def __init__(self,path:str,seed=None) -> None:
        """

        """
        self.path = path
        self.seed = seed


    def get_tasks(self) -> list[Task] | None:
        """

        """

        random.seed(None)
        if self.seed is not None:
            random.seed(self.seed)

        try:

            tasks:list[Task] = []

            for col in range(0,random.randint(1, 3)):
                data = {}
                response = requests.get(self.path)
                try:
                    data["data"] = response.json()
                except Exception:
                    data["data"] = response.text
                el = Task(random.randint(10000, 99999),data)
                tasks.append(el)

            random.seed(None)
        except Exception:
            random.seed(None)
            return None

        return tasks
