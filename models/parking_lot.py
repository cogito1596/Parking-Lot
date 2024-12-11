import uuid
from .floors import floor
from .parking_lot_status import parkingLotStatus
from .gate import Gate
from .vehicle_type import vehicle_type
from .Assignment_strategy import AssignmentStrategy


class parkingLot:
    def __init__(
        self,
        name,
        floor: list[floor],
        parkingLotStatus: parkingLotStatus,
        gates: list[Gate],
        allowed_vehicles: list[vehicle_type],
        capacity: int,
        assignment_strategy: AssignmentStrategy,
    ):
        self.floors = floor
        self.id = uuid.uuid4()
        self.status = parkingLotStatus
        self.name = name
        self.gates = gates
        self.allowed_vehicles = allowed_vehicles
        self.capacity = capacity
        self.assignment_strategy = assignment_strategy
