from level import Level
from vehicle import Vehicle
from vehicle_type import VehicleType
from typing import List
class ParkingLot:
    _instance = None
    
    # Singleton Class
    def __init__(self):
        if self._instance is not None:
            raise Exception('Use get_instance(), This class is a singleton class!')

        ParkingLot._instance = self
        self.levels : List[Level] = []
    
    # Method to create an instance of the ParkingLot
    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance
    
    def add_level(self, level: Level):
        self.levels.append(level)
    
    def park_vehicle(self, vehicle: Vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
            
        return False
    
    def unpark_vehicle(self, vehicle: Vehicle):
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        
        return False

    def display_availability(self):
        for level in self.levels:
            level.display_availability()
            
        
        