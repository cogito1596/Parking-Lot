class ParkingLotrepo:
    def __init__(self):
        self.__parking_lot = {}

    def update_parking_lot(self, parking_lot):
        parking_lot.capacity -= 1
        self.__parking_lot[parking_lot.id] = parking_lot
        return parking_lot
