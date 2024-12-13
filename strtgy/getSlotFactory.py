from models import cellStrategy
from .RandomSlot import RandomSlot


class SlotFactory:
    @staticmethod
    def getSlot(Strategy):
        if Strategy == cellStrategy.random:
            return RandomSlot()
        # if cellStrategy == cellStrategy.Lifo:
        #     return LifoSlot()
        # if cellStrategy == cellStrategy.Fifo:
        #     return FifoSlot()
        return None
