from abc import ABC, abstractmethod
from vehicle_type import VehicleType

class Vehicle(ABC):
    def __init__(self, license_plate: str ,VehicleType: VehicleType):
        self.vehicle_type = VehicleType
        self.license_plate = license_plate
    
    def get_type(self):
        return self.vehicle_type
    