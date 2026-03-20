from typing import Dict, Any
from requests import Response
from src.Task import Task
import random
import requests

class SourceFromWeb:
    """
        Источник задач из интернета
    """

    def __init__(self, path: str, seed=None) -> None:
        """
            Инициализатор источника задач из интернета
        """
        self.path = path
        self.seed = seed

    def get_tasks(self) -> list[Task] | None:
        """
            Функция получения задач из интернета
        """

        random.seed(None)
        if self.seed is not None:
            random.seed(self.seed)

        try:
            tasks: list[Task] = []
            for col in range(0, random.randint(1, 3)):
                data: Dict[str, Any] = {}
                response: Response = requests.get(self.path)
                try:
                    data["data"] = response.json()
                except Exception:
                    data["data"] = response.text
                el: Task = Task(random.randint(10000, 99999), data)
                tasks.append(el)
            random.seed(None)
            return tasks
        except Exception:
            random.seed(None)
            return None
