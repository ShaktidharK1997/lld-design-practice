from vehicle import Vehicle
from vehicle_type import VehicleType

class ParkingSpot:
    def __init__(self, spot_number: int, vehicle_type: VehicleType):
        self.vehicle_type = vehicle_type if vehicle_type is not None else VehicleType.CAR 
        self.parked_vehicle = None
        self.spot_number = spot_number
    
    def is_available(self):
        return self.parked_vehicle is None
    
    def park_vehicle(self, vehicle: Vehicle):
        if not self.is_available():
            raise Exception('Parking spot is not available')

        if vehicle.get_type()!= self.vehicle_type:
            raise Exception('Vehicle type is not allowed')
        
        self.parked_vehicle = vehicle

    def unpark_vehicle(self):
        if self.is_available():
            raise Exception('Parking Spot is empty')

        self.parked_vehicle = None
    
    def get_parked_vehicle(self):
        return self.parked_vehicle
    
    def get_vehicle_type(self):
        return self.vehicle_type

    