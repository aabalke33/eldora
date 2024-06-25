from abc import ABC, abstractmethod

class Form(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def get_json(self):
        pass
