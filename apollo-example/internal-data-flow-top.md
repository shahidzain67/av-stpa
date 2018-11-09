# Internal data flows in the IPC

## Routing

### HMI : Routing

#### Commands Information from HMI to Routing

- Change map
- Change / request route (waypoints)
- Start / Stop routing module

#### Feedback Information from Routing to HMI

- Detailed routing information (lane segments, passage markers)

## Planning

### HMI : Planning

#### Commands from HMI

- Start / End Automatic mode
- Start / Start planning module

#### Feedback to HMI

- software module operation
- trajectory information

### Planning : Routing

#### Command from planning

- Request updated route based on present location

#### Feedback information from Routing

- Detailed routing information (lane segments, passage markers)

### Planning : Localization (via Common)

#### Command

- update vehicleState

#### Feedback

- vehicleState is updated with position, velocity, acceleration, attitude, and rate-of-change of attitude

#### Feedback

- vehicle state is updated with Gear and DrivingMode information and Speed (mps) information

### Planning : Common

#### Command

EstimateFuturePosition()

#### Feedback

Estimated future position vector

### Planning : Prediction

#### Command

There are no commands to prediction from planning - however, the latest planning trajectory is sent to the 

#### Feedback

Trajectories of external obstacles - with probabilities - planning module uses the obstacles to calculate if a collision will occur, and recalculate if necessary. _Trajectories are made up of trajectory points, which include position and instantaneous velocity and acceleration._

### Planning : Perception

#### Command

There are no commands to perception from planning.

#### Feedback

Perception will handle send traffic light detection information. This means the position, id, and state of the traffic light.

## Prediction

### Commands

Prediction sends no commands, it only receives information and sends information.

### Prediction : Planning

#### Feedback from Planning

The latest calculated vehicle trajectory

### Prediction : Perception

#### Feedback from perception

Perception obstacles data - point obstacle position / type / velocity characteristics - data regarding the obstacles that will be processed into trajectories by the prediction module.
*This data is sent from the Perception Fusion subnode*

### Prediction : Localization

 - pulls in updated vehicle state information OnLocalization

## Perception

### Perception : localization

#### Feedback

 - pulls in updated vehicle state information OnLocalization

### Perception (fusion) : Perception (Lidar subnode)

#### Feedback

 - lidar raw information (point cloud) is transferred into objects
 - objects are created, tracked, and fused
 - publishes events to an event manager, to which fusion subscribes

### Perception (fusion) : Perception (radar subnode)

#### Feedback

 - Subnode process identifies objects from raw data
 - New objects detected are 'created'
 - existing objects are tracked with updated radar information
 - publishes events to fusion

### Perception (fusion subnode)

 - takes objects from multiple sensors, and outputs 'fused' sensor objects
 - updates the sensor objects 'tracks' with information from the corresponding lidar / radar objects as it comes in
 - composes the data in a 'pose'
 - puts tracked objects into frames
 - Publishes its results to the adapter manager

### Perception (traffic lights subnode)

#### Preprocessor subnode

 - Gets short focus image data
 - Gets long focus image data
 - passed to TL subnode

#### Perception : TL subnode

 - after some additional processing, TL detection results are published

### Perception : Environmental Sensors

#### Long/Short Focal length cameras

 - these provide image data to the TL preprocessor submodule

#### Radar

 - Provides raw observations to the Perception radar subnode

#### Lidar 

 - Provides point cloud data to the Perception Lidar subnode


## Localization

### Localization : Canbus

 - Receives Gear, velocity information from the canbus module - it pulls this through the chassis struct methods in the adapter manager

### Localization : GPS/GNSS sensor

 - inertial data
 - GPS and GNSS position and pose data

### Localization : Lidar Sensor

 - point cloud position data (can be used in conjuction with HD map to identify position)

## Control

### Control : Canbus module

#### commands

 - Brake
 - Throttle
 - Steer
 - Shift
 - Parking Brake
 - Headlights
 - Horn
 - Turn Signal

#### Feedback









## Canbus Module

### Canbus : Dataspeed

#### commands

*The canbus module acts as a protocol converter to send correctly formatted commands to the canbus driver*

 - Brake
 - Throttle
 - Steer
 - Shift
 - Parking Brake
 - Headlights
 - Horn
 - Turn Signal

#### feedback

 - vehicle fault status
 - steering state
 - propulsion state
 - braking state
 - watchdog fault state
