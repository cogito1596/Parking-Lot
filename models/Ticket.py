import uuid
from .cells import cell


class Ticket:
    def __init__(
        self, vehicle_number, owner_name, gate, vehicle_type, entry_time, cell: cell
    ):
        self.ticket_id = uuid.uuid4()
        self.vehicle_number = vehicle_number
        self.owner_name = owner_name
        self.gate = gate
        self.vehicle_type = vehicle_type
        self.entry_time = entry_time
        self.cell = cell
