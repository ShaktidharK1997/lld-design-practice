from parking_spot import ParkingSpot
from vehicle import Vehicle
from vehicle_type import VehicleType

class Level:
    def __init__(self, level_number:int, number_of_spots:int):
        self.level_number = level_number
        self.number_of_spots = number_of_spots
        self.parking_spots = [ParkingSpot(i, VehicleType.CAR) for i in range(number_of_spots)]
        self.available_spots = number_of_spots
        self.spot_vehicle_map = {}
    
    def park_vehicle(self, vehicle: Vehicle):
        if self.available_spots == 0:
            return False

        for spot in self.parking_spots:
            if spot.is_available() and spot.get_vehicle_type() == vehicle.get_type():
                spot.park_vehicle(vehicle)
                self.spot_vehicle_map[vehicle.license_plate] = spot
                self.available_spots -= 1
                return True
        return False
    
    def unpark_vehicle(self, vehicle: Vehicle):
        if vehicle.license_plate not in self.spot_vehicle_map:
            return None, None
        
        spot = self.spot_vehicle_map[vehicle.license_plate]
        spot_number, entry_timestamp = spot.unpark_vehicle()
        self.available_spots += 1
        del self.spot_vehicle_map[vehicle.license_plate]
        return spot_number, entry_timestamp, self.level_number

    def display_availability(self):
        for spot in self.parking_spots:
            print(f'Spot Number: {spot.spot_number} is available: {spot.is_available()}')
