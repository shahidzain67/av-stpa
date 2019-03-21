# Type 2 Scenario Refinement

## Inadequate vehicle speed feedback and deceleration

Refined scenarios:
- Sensor(s) used to detect vehicle speed fail
- Sensor(s) used to detect vehicle speed have inadequate resolution, accuracy, update frequency etc.

Requirements:
- Apollo must receive feedback that indicates vehicle speed
- Apollo must have means to detect vehicle speed in event of sensor failure
- Vehicle speed feedback must be updated every TBD ms
- Vehicle speed feedback must be accurate to within x mph

## Inadequate object detection, object distance detection and object velocity detection

Refined scenarios:
- Sensor(s) used to detect object fail
- Sensor(s) used to detect object position fail
- Sensor(s) have inadequate resolution, update frequency, accuracy to detect object position and velocity

Requirements:
- Apollo must receive feedback that indicates obstacles positions
- Apollo must have means to detect objects in event of sensor failure
- Object detection feedback must be updated every TBD ms
- Object detection feedback must be accurate to within x m

## Inadequate vehicle location

Refined scenarios:
- Sensor(s) used to detect location fail
- Sensor(s) used to detect location have inadequate resolution, accuracy, update frequency etc.

Requirements:
- Apollo must receive feedback that indicates vehicle location
- Apollo must have means to detect vehicle location in event of sensor failure
- Vehicle location feedback must be updated every TBD ms
- Vehicle location feedback must be accurate to within x m

## Inadequate limits (speed limit, traffic flow limit, manoeuvre limit, planned test limit, etc.)

Refined scenarios:
- Traffic flow limit : object velocity detection (as above)
- Speed limit : Location (as above)
- Map information regarding speed limit is incorrect / lacks sufficient detail
- Optical sensor(s) fail
- Optical sensor(s) have inadequate resolution, update frequency etc.

Requirements:
- Apollo must receive optical feedback which is adequate to see necessary road signs and obstacles
- Apollo must have means to detect optical sensor failure
- Optical feedback must be updated every TBD ms
- Optical feedback must have x resolution
- Apollo must receive dynamic (i.e. not from a map file) information that indicates any speed limits it must adhere to

## Inadequate autonomous mode detection, driver input and driver throttle detection

Refined scenarios:
- Dataspeed feedback fails
- Information from safety monitor (autonomous mode on / off) fails (not received, incorrect)

Requirements:
- Apollo must receive information from Dataspeed which indicates if the driver has taken control of the vehicle (pressed throttle, brake, etc.)
- Apollo must receive information from the driver which indicates if they want to take control

## Inadequate traffic signal detection (red lights, give way etc.)

Refined scenarios:
- Location : as above
- Map information regarding traffic signal location is incorrect / lacks sufficient detail
- Optical : as above

Requirements:
- Apollo must receive dynamic (i.e. not from a map file) information that indicates any traffic signals it must adhere to

## Inadequate destination location

Refined scenarios:
- Map file is incorrect / lack sufficient detail
- Route waypoints are incorrect / lack sufficient detail

Requirements:
- Apollo must receive up to date map information, which is detailed to x m
- Apollo must receive route waypoint information which is accurate to x m

## Inadequate collision detection

Refined scenarios:
- Sensor(s) used to detect collisions fail
- Sensor(s) used to detect collision have inadequate resolution, accuracy, update frequency etc.

Requirements:
- Apollo must receive feedback that indicates whether the vehicle has been in a collision
- Apollo must have means to detect collisions in event of single sensor failure

## Inadequate fault detection

## Inadequate wheel lock detection

Refined scenarios:
- Sensor(s) used to detect wheel lock fail

Requirements:
- Apollo must have means of detecting whether wheel lock has occurred
