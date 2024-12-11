from models import Ticket
from datetime import datetime
from repos import GateRepo, VehicleRepo
from models import vehicle


class TicketService:
    def __init__(self, GateRepo, VehicleRepo):
        self.GateRepo = GateRepo
        self.VehicleRepo = VehicleRepo

    def issueTicket(self, vehicle_number, owner_name, gate_id, vehicle_type):
        ticket = Ticket(
            vehicle_number="",
            owner_name="",
            gate="",
            vehicle_type="",
            entry_time=datetime.now(),
        )
        gate = self.GateRepo.getGateById(gate_id)
        if gate is None:
            raise Exception("Gate not found")
        ticket.gate = gate
        v = self.VehicleRepo.find_vehicle(vehicle_number)
        if v is None:
            vehicale = vehicle(
                vehicle_number=vehicle_number,
                owner_name=owner_name,
                vehicle_type=vehicle_type,
            )
            v = self.VehicleRepo.add_vehicle(vehicale)
        ticket.vehicle = v
