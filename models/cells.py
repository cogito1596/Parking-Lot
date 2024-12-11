from .vehicle_type import vehicle_type
from .cell_status import cell_status
import uuid


class cell:
    def __int__(self, floor_id):
        self.id = uuid.uuid4()
        self.floor_id = floor_id
        self.vehicle = None
        self.status = cell_status.empty

    def get_status(self):
        return self.status

    def set_status(self, status):
        if isinstance(status, cell_status):
            self.status = status
        else:
            raise ValueError("Invalid status. Must be a cell_status enum.")

    def assign_vehicle(self, vehicle):
        if isinstance(vehicle, vehicle_type):
            if self.status == cell_status.empty:
                self.vehicle = vehicle
                self.status = cell_status.occupied
            else:
                raise ValueError("Cell is already occupied.")
        else:
            raise ValueError("Invalid vehicle type. Must be a vehicle_type enum.")
