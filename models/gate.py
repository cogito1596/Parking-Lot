from .gate_type import gateType
from .gate_status import GateStatus
import uuid


class Gate:
    def __init__(
        self,
        gate_type,
        gate_number,
        gate_status,
        parking_lot,
    ):
        if isinstance(gate_type, gateType):
            self.gate_type = gate_type
        else:
            raise ValueError("Invalid gate type. Must be a gateType enum.")
        self.gate_id = uuid.uuid4()
        self.gate_status = GateStatus
        self.gate_number = gate_number
        self.parking_lot = parking_lot
