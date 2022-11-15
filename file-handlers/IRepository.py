import abc



class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self):
        pass
    @abc.abstractmethod
    def list(self):
        pass
    @abc.abstractmethod
    def update(self):
        pass
    @abc.abstractmethod
    def delete(self):
        pass







