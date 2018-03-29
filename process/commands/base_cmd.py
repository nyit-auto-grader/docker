from abc import ABC, abstractmethod
from typing import List


class Command(ABC):

    @property
    @abstractmethod
    def fields(self) -> List[str]:
        pass

    def __init__(self, **kwargs):
        for field in self.fields:
            setattr(self, field, kwargs.get(field))
        self.setup()

    def setup(self):
        pass

    @abstractmethod
    def execute(self):
        pass
