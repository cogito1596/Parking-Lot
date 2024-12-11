import uuid
from .cells import cell
from .floor_status import floor_status
from .vehicle_type import vehicle_type


class floor:
    def __init__(
        self,
        floor_number: int,
        floor_status: floor_status,
        parking_slots,
        allowed_vehicle_types: list[vehicle_type],
    ):
        self.id = uuid.uuid4()
        self.floor_status = floor_status
        self.floor_number = floor_number
        self.parking_slots = parking_slots
        self.allowed_vehicle_types = allowed_vehicle_types
