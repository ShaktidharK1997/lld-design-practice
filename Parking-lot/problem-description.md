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
1) Parking lot class (Singleton pattern) -> only one instance of parking lot created 
    - Park function (type of car)-> 
        Iterate over all the level objects part of lot and check for avail
        If avail, then call park_level fn (type of car)

2) A level class which will be part of the parking lot class as a list of levels 
    - Park level fn - handles parking within that level

3) A parking spot class which will be part of levels class as a list of spots 
    - tracks avail and parked vehicle 

4) Vehicle type as an Enum with 3 types (motorcycle, truck and car)
PL -> Level -> Spot 

