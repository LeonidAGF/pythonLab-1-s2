from typing import Protocol, runtime_checkable
from Task import Task

@runtime_checkable
class TaskSource(Protocol):
    """

    """
    def get_tasks(self) -> list[Task]:
        """

        """
        pass
