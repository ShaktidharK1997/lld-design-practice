Requirements : 
1) Are we designing a system for a particular parking lot or parking lots in general ? 
one particular parking lot 
2) Does the parking lot have multiple levels to it ? 
Yes, multiple levels to it 
3) Does the parking lot have different type of parking spots for different type of vehicles? Ex : Truck, car, motorcycle? If so, can you tell me or can I take the liberty to specify some types?
Yes 3 different types (truck, car and motorcycle)
4) The system will block a spot upon successful reservation and unblock the spot when the car leaves the parking lot 
5) Do we need to keep track of real-time information like parking spots availability etc? 
Yes, real-time info required
6) Who reserves the parking spot? the customer or a parking lot agent ?
Parking lot agent 
7) do we need to return a reservation Id with parking spot number? 

Classes, Interfaces and Enumerations 
1) Parking Lot Class 
    - Singleton class, only one instance of Parking Lot possible
    - Parking lot has a private attribute levels which contains a list of Level objects
    - Has methods park_vehicle and unpark_vehicle which park and unpark vehicle in corresponding level according to availability

2) Level Class
    - Level class contains attribute level_number which holds the level of the Parking Lot and list variable called Spots which holds a list of parking spots of a pre-defined type 
    - Methods Park_vehicle and unpark_vehicle which do the operations for that level. Methods return spot object if success or None if not success
    - It also has a mapping object that maps the vehicle to the parking spot in order to reduce the time taken to find spot to unpark vehicle 
    - Method display_availability that displays the availability of all the parking spots in that level

3) Parking Spot class 
    - Has attributes parked_vehicle (holds instance of parked vehicle), spot_number (unique identification) and vehicle type enum for marking it with a type of vehicle 
    - Methods park_vehicle and unpark_vehicle 
    - Method get_vehicle_type to return its type 
    - Method get_parked_vechile to get parked vechile type 

4) Vehicle type as an Enum with 3 types (motorcycle, truck and car)


