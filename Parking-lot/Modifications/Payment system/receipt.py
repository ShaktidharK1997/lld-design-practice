from vehicle_type import VehicleType
from datetime import datetime

class Receipt:
    def __init__(self, license_number:str, vehicle_type: VehicleType
                 , entry_timestamp: datetime, exit_timestamp: datetime,
                 billing_amount: float, parking_spot_number: int, level_number: int):
        self.license_number = license_number
        self.vehicle_type = vehicle_type
        self.entry_timestamp = entry_timestamp
        self.exit_timestamp = exit_timestamp
        self.billing_amount = billing_amount
        self.parking_spot_number = parking_spot_number
        self.level_number = level_number
    
    def __str__(self):
        return f'License Number: {self.license_number}, Vehicle Type: {self.vehicle_type}, Entry Time: {self.entry_timestamp}, Exit Time: {self.exit_timestamp}, Billing Amount: {self.billing_amount}, Parking Spot Number: {self.parking_spot_number}, Level Number: {self.level_number}'
    
    def print_receipt(self):
        print(self.__str__())
        
    