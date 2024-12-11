from .vehicle_type import vehicle_type
import uuid


class Vehicle:
    def __init__(
        self, id: int, owner_name: str, vehicle_type: vehicle_type, vehicle_number: str
    ):
        self.id = uuid.uuid4()
        self.owner_name = owner_name
        self.vehicle_type = vehicle_type
        self.vehicle_number = vehicle_number
