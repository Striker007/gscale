
from abc import ABCMeta, abstractmethod, abstractproperty


class Market:
    """
    Market interface
    """
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        pass

    @abstractmethod
    def prices(self):
        pass
