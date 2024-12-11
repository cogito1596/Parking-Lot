from abc import ABC, abstractmethod


class SlotStrategy(ABC):
    @abstractmethod
    def get_slot(self, vehicle_type, gate):
        pass
