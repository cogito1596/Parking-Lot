class VehicleRepo:
    def __init__(self):
        self.__vehicles = {}

    def add_vehicle(self, vehicle_id, vehicle):
        self.__vehicles[vehicle_id] = vehicle
        return vehicle

    def find_vehicle(self, vehicle_id):
        if vehicle_id in self.__vehicles:
            return self.__vehicles[vehicle_id]
        return None
