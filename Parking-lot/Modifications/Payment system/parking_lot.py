from level import Level
from vehicle import Vehicle
from vehicle_type import VehicleType
from typing import List
from receipt import Receipt
from datetime import datetime
class ParkingLot:
    _instance = None
    
    # Singleton Class
    def __init__(self):
        if self._instance is not None:
            raise Exception('Use get_instance(), This class is a singleton class!')

        ParkingLot._instance = self
        self.levels : List[Level] = []
        self.receipts :  List[Receipt] = []
    
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
    @staticmethod
    def parking_fee_calculator(entry_timestamp, exit_timestamp, vehicle_type):
        """Calculate Parking Fee"""
        vehicle_type_fee_multipler_dict = {
            VehicleType.CAR: 1,
            VehicleType.MOTOR_CYCLE: 0.7,
            VehicleType.TRUCK: 1.5
        }
        
        no_of_hours = (exit_timestamp - entry_timestamp).seconds // 3600
        
        if no_of_hours < 1:
            hour_multiplier = 10
        elif no_of_hours < 3:
            hour_multiplier = 8
        elif no_of_hours < 7:
            hour_multiplier = 7
        else:
            hour_multiplier = 6
        
        fee = hour_multiplier*no_of_hours*vehicle_type_fee_multipler_dict[vehicle_type]
        
        return fee
    
    def unpark_vehicle(self, vehicle: Vehicle):
        for level in self.levels:
            parking_spot, entry_timestamp, level_number = level.unpark_vehicle(vehicle)
            if parking_spot is not None:
                # Calculate Parking Fee
                fee = self.parking_fee_calculator(entry_timestamp, datetime.now(), vehicle.get_type())
                current_receipt = Receipt(vehicle.license_plate, vehicle.get_type(), entry_timestamp, datetime.now()
                        , fee, parking_spot, level_number)
                current_receipt.print_receipt()
                self.receipts.append(current_receipt)
                return True
        return False


    def display_availability(self):
        for level in self.levels:
            level.display_availability()
            
        
        