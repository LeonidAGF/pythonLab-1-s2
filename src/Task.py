from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class Task:
    """
        Класс задачи
    """
    id:int
    payload:Dict[str, Any]
