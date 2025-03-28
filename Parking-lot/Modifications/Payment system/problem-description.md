Implement a payment system:

Add parking rates based on vehicle type and duration
Implement a billing system that calculates fees when a vehicle exits


- User gets billed when he unparks the car
    - Details required for calculating amount : time parked, type of vehicle 
- For this, add additional details during parking in parking spot object while successfully parked 


Classes, Interfaces and Enumerations

1. Parking Spot Class 
    - We will add an attribute entry_time that holds the timestamp when customer has parked in the spot 
    - During park_vehicle fn, we will add the entry time during datetime 
    - During unpark_vehicle fn, we will return the details of the details of entry time, parking spot number, with success bool flag
    - Display the entry time along with vehicle details for display_parked_vehicle fn
2. Level Class
    - Changes in unpark_vehicle method where we return the details of entry time, parking spot number, level number along with success bool flag 
3. Parking Lot Class 
    - During unpark, we will take the details of the entry time and use that along with vehicle type to calculate the fees using a payment calculator @staticmethod 
    - After calculating, we will create a receipt class object with the details of the vehicle, entry timestamp and fees 
    - We will add it to a list of receipts in the Parking lot instance 
4. Receipt class 
    - Attributes : Vehicle license plate, Vehicle entry time, Vehicle type, Fees for parking, parking spot number
    - Methods : Print receipt, verify receipt 


Clarifying questions:
1) receipt in only USD and how to handle rounding off ? 
2) 