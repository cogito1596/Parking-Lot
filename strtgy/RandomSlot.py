from .slotstrtgy import SlotStrtgy
from ..models import cell_status


class RandomSlot(SlotStrtgy):
    def __init__(self):
        pass

    def getSlot(self, vehicle_type, gate):
        for floor in gate.parking_lot.floors:
            if vehicle_type in floor.allowed_vehicles:
                for slot in floor.parking_slots:
                    if (
                        slot.vehicle_type == vehicle_type
                        and slot.status == cell_status.empty
                    ):
                        return slot
        return None
