from models import Ticket, cell_status
from datetime import datetime
from repos import GateRepo, VehicleRepo, SlotRepo, ParkingLotRepo, TicketRepo
from models import vehicle
from ..strtgy import getSlotFactory


class TicketService:
    def __init__(
        self,
        GateRepo: GateRepo,
        VehicleRepo: VehicleRepo,
        SlotRepo: SlotRepo,
        parkingLotRepo: ParkingLotRepo,
        TicketRepo: TicketRepo,
    ):
        self.gateRepo = GateRepo
        self.vehicleRepo = VehicleRepo
        self.SlotRepo = SlotRepo
        self.parkingLotRepo = parkingLotRepo
        self.TicketRepo = TicketRepo

    def issueTicket(
        self,
        vehicle_number,
        owner_name,
        gate_id,
        vehicle_type,
    ):
        ticket = Ticket(
            vehicle_number="",
            owner_name="",
            gate="",
            vehicle_type="",
            entry_time=datetime.now(),
        )
        gate = self.gateRepo.getGateById(gate_id)
        if gate is None:
            raise Exception("Gate not found")
        ticket.gate = gate
        v = self.vehicleRepo.find_vehicle(vehicle_number)
        if v is None:
            vehicale = vehicle(
                vehicle_number=vehicle_number,
                owner_name=owner_name,
                vehicle_type=vehicle_type,
            )
            v = self.VehicleRepo.add_vehicle(vehicale)
        ticket.vehicle = v

        cell = getSlotFactory.getSlot(gate.parking_lot.assignment_strategy)

        if cell is None:
            raise Exception("Strategy failed to allocate slot")

        cell = cell.get_slot(vehicle.vehicle_type, gate)

        if cell is None:
            raise Exception("No slot available")

        ticket.cell = cell

        self.SlotRepo.updateSlot(cell, cell_status.occupied)
        self.parkingLotRepo.updateParkingLot(gate.parking_lot)
        return self.TicketRepo.add_ticket(ticket)
