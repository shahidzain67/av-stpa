## UCA-6.1: Apollo does not provide brake control when relative velocity and distance to an obstacle mean that a collision is imminent

#### Type 1.1:
  - Apollo does not provide brake control when relative velocity and distance to an obstacle mean that a collision is imminent
  - The feedback does indicate that an obstacle is in the vehicle's path

#### Type 2.1:
  - The feedback does not indicate that an obstacle is in the vehicle's path
  - An obstacle is in the vehicle's path

Feedback info:
  - Inadequate vehicle speed
  - Inadequate other vehicle / object velocity
  - Inadequate other vehicle / object distance
  - Inadequate object detection

## UCA-6.2: Apollo does not provide brake control when in autonomous mode and vehicle speed exceeds limits (limits for controllability, stability, upcoming manoeuvre, speed limit, traffic flow limit, planned test limit, etc.)

#### Type 1.2:
  - Apollo does not provide brake control when in autonomous mode and vehicle speed exceeds limits (limits for controllability, stability, upcoming manoeuvre, speed limit, traffic flow limit, planned test limit, etc.)
  - The feedback does indicate that the vehicle exceeds limits

#### Type 2.2:
  - The feedback does not indicate that the vehicle exceeds limits
  - The vehicle does exceed limits

Feedback info:
  - Inadequate vehicle speed
  - Inadequate speed limits

## UCA-6.3: Apollo does not provide brake control when in autonomous mode, the vehicle is stationary, and vehicle path is not clear

#### Type 1.3:
  - Apollo does not provide brake control when in autonomous mode, the vehicle is stationary, and vehicle path is not clear
  - The feedback does indicate that the vehicle is in autonomous mode, the vehicle is stationary and the vehicle path is not clear

#### Type 2.3:
  - The feedback does not indicate that the vehicle is in autonomous mode, the vehicle is stationary and the vehicle path is not clear
  - The vehicle is in autonomous mode, the vehicle is stationary and the vehicle path is not clear

Feedback info:
  - Inadequate autonomous mode detection
  - Inadequate vehicle speed
  - Inadequate object detection
  - Inadequate traffic signal detection (red lights, give way etc.)

## UCA-6.4: Apollo does not provide brake control when in autonomous mode and the vehicle has reached the final destination

#### Type 1.4:
  - Apollo does not provide brake control when in autonomous mode and the vehicle has reached the final destination
  - The feedback does indicate is in autonomous mode and has reached its final destination

#### Type 2.4:
  - The feedback does not indicate that the vehicle is in autonomous mode and has reached its final destination
  - The vehicle is in autonomous mode and has reached its final destination

Feedback info:
  - Inadequate autonomous mode detection
  - Inadequate vehicle location
  - Inadequate destination location  

## UCA-6.6: Apollo does not provide brake control when in autonomous mode and collision occurs

#### Type 1.6:
  - Apollo does not provide brake control when in autonomous mode and collision occurs
  - The feedback does indicate that the vehicle is in autonomous mode and a collision has occurred

#### Type 2.6:
  - The feedback does not indicate that the vehicle is in autonomous mode and a collision has occurred
  - The vehicle is in autonomous mode and a collision has occurred

Feedback info:
  - Inadequate autonomous mode detection
  - Inadequate collision detection

## UCA-6.7: Apollo provides brake command with insufficient amount of braking below the minimum amount needed to avert a forward collision

#### Type 1.7:
  - Apollo provides brake command with insufficient amount of braking below the minimum amount needed to avert a forward collision
  - The feedback does indicate that the braking is insufficient to avert a forward collision

#### Type 2.7:
  - The feedback does not indicate that the braking is insufficient to avert a forward collision
  - The braking is insufficient to avert a forward collision

Feedback info:
  - Inadequate vehicle speed
  - Inadequate deceleration
  - Inadequate object distance
  - Inadequate object velocity

## UCA-6.8: Apollo provides brake control when autonomous driving is not active (off, standby, overridden, or e-stop)

#### Type 1.8:
  - Apollo provides brake control when autonomous driving is not active (off, standby, overridden, or e-stop)
  - The feedback does indicate that autonomous driving is not active

##### Type 2.8:
  - The feedback indicates that autonomous driving is active
  - Autonomous driving is not active

Feedback info:
  - Inadequate autonomous detection

## UCA-6.9: Apollo provides brake control when vehicle speed does not exceed limits (speed limit, traffic flow limit, manoeuvre limit, planned test limit, etc.), there is no obstacle, no faults, destination is reachable, and vehicle has not reached destination

#### Type 1.9:
  - Apollo provides brake control when vehicle speed does not exceed limits (speed limit, traffic flow limit, manoeuvre limit, planned test limit, etc.), there is no obstacle, no faults, destination is reachable, and vehicle has not reached destination
  - The feedback does indicate that the vehicle does not exceed limits, there is no obstacle, no faults, destination is reachable and the vehicle has not reached the destination

#### Type 2.9:
  - The feedback indicates that the vehicle exceeds limits, there is an obstacle, a fault, the destination is not reachable or the vehicle has reached its destination
  - The vehicle does not exceed limits, there is no obstacle, no faults, destination is reachable and the vehicle has not reached the destination

Feedback info:
  - Inadequate vehicle speed
  - Inadequate speed limits
  - Inadequate object detection
  - Inadequate fault detection
  - Inadequate vehicle location
  - Inadequate destination location

## UCA-6.10: Apollo provides brake control when driver is providing throttle

#### Type 1.10:
  - Apollo provides brake control when driver is providing throttle
  - The feedback does indicate that the driver is providing throttle

#### Type 2.10:
  - The feedback does not indicate that the driver is providing throttle
  - The driver is providing throttle

Feedback info:
  - Inadequate driver throttle detection  

## UCA-6.11: Apollo provides excessive brake command when wheel lock has occurred and lateral control is needed (rationale: ABS may not work below 5mph or other situations)

#### Type 1.11:
  - Apollo provides excessive brake command when wheel lock has occurred and lateral control is needed
  - The feedback does indicate that wheel lock has occurred and lateral control is needed

#### Type 2.11:
  - The feedback does not indicate that wheel lock has occurred and lateral control is needed
  - Wheel lock has occurred and lateral control is needed

Feedback info:
  - Inadequate wheel lock detection

## UCA-6.12: Apollo provides brake command with insufficient amount of braking to reduce vehicle speed within limits (limits for controllability, stability, upcoming manoeuvre, speed limit, traffic flow limit, planned test limit, etc.)

#### Type 1.12:
  - Apollo provides brake command with insufficient amount of braking to reduce vehicle speed within limits
  - The feedback does indicate that the braking is insufficient to reduce vehicle speed to within limits

#### Type 2.12:
  - The feedback indicates that the braking is sufficient to reduce vehicle speed to within limits
  - The braking is insufficient to reduce vehicle speed to within limits

Feedback info:
  - Inadequate vehicle speed
  - Inadequate deceleration
  - Inadequate speed limits

## UCA-6.13: Apollo provides brake control that is excessive beyond physical limits for passengers

#### Type 1.13:
  - Apollo provides brake control that is excessive beyond physical limits for passengers
  - The feedback does indicate that the braking is excessive beyond physical limits for passengers

#### Type 2.13:
  - The feedback does not indicate that the braking is excessive beyond physical limits for passengers
  - The braking is excessive beyond physical limits for passengers

Feedback info:
  - Inadequate deceleration

## UCA-6.14: Apollo provides brake control too late (> TBD seconds) after relative velocity and distance to an obstacle mean that a collision is imminent

#### Type 1.14:
  - Apollo provides brake control too late (> TBD seconds) after relative velocity and distance to an obstacle mean that a collision is imminent
  - The feedback does indicate that there is an imminent collision and is received on time

#### Type 2.14:
  - The feedback is received too late to avoid an imminent collision
  - There is an imminent collision

Feedback info:
  - Too late feedback (as per Type 2.1)

## UCA-6.15: Apollo provides brake control too late (> TBD seconds) prior to manoeuvre

#### Type 1.15:
  - Apollo provides brake control too late (> TBD seconds) prior to manoeuvre
  - The feedback does indicate that there is an upcoming manoeuvre and is on time

#### Type 2.15:
  - The feedback is received too late to avoid a collision
  - There is an upcoming manoeuvre

Feedback info:
  - Too late feedbcak (as per Type 2.2)  

## UCA-6.16: Apollo provides brake control too late before (< TBD sec before) limits are exceeded (limits for upcoming manoeuvre, controllability, stability, speed limit, traffic flow limit, planned test limit, etc.)

#### Type 1.16:
  - Apollo provides brake control too late before (< TBD sec before) limits are exceeded
  - The feedback does indicate that limits are exceeded and is on time

#### Type 2.16:
  - The feedback is received too late to avoid exceeding limits
  - The limits have been / will be exceeded

Feedback info:
  - Too late feedback (as per Type 2.2)  

## UCA-6.17: Apollo removes brake control too early when relative velocity and distance to an obstacle mean that a collision will occur

#### Type 1.17:
  - Apollo removes brake control too early when relative velocity and distance to an obstacle mean that a collision will occur
  - The feedback does indicate that a collision will occur and that the brake control is needed for longer

#### Type 2.17:
  - The feedback no longer shows that a collision will occur
  - A collision will occur if the brake control is removed

Feedback info:
  - As per type 2.1

## UCA-6.18: Apollo removes brake control too early (> TBD seconds) prior to/during manoeuvre

#### Type 1.18:
  - Apollo removes brake control too early (> TBD seconds) prior to/during manoeuvre
  - The feedback does indicate that there is an upcoming manoeuvre and that the brake control is needed for longer

#### Type 2.18:
  - The feedback no longer shows that there is an upcoming manoeuvre
  - There is an upcoming manoeuvre and brake control is needed to slow the vehicle to the correct speed

Feedback info:
  - As per type 2.2

## UCA-6.19: Apollo stops applying brake control when in autonomous mode before (> TBD seconds before) vehicle slows to acceptable speed (speed limit, traffic flow limit, manoeuvre limit, planned test limit, limits for controllability, stability, etc.)

#### Type 1:
  - Apollo stops applying brake control when in autonomous mode before (> TBD seconds before) vehicle slows to acceptable speed
  - The feedback does indicate that the vehicle needs to slow down

#### Type 2:
  - The feedback shows that brake control is no longer needed to slow the vehicle to an acceptable speed
  - The vehicle still needs to decelerate

Feedback info:
  - As per type 2.2

## UCA-6.20: Apollo continues applying brake control too long (> TBD seconds) after vehicle slows to acceptable speed (speed limit, traffic flow limit, manoeuvre limit, planned test limit, limits for controllability, stability, etc.)

#### Type 1.20:
  - Apollo continues applying brake control too long (> TBD seconds) after vehicle slows to acceptable speed
  - The feedback does indicate the vehicle has reached an acceptable speed

#### Type 2.20:
  - The feedback does not show that the vehicle has reached an acceptable speed
  - The vehicle has reached an acceptable speed

Feedback info:
  - As per 2.2

## UCA-6.21: Apollo stops applying brake control too soon at end of test before driver has resumed control (e.g. manual braking)

#### Type 1.21:
  - Apollo stops applying brake control too soon at end of test before driver has resumed control
  - The feedback does indicate that the driver has not resumed control

#### Type 2.21:
  - The feedback indicates that the driver has resumed control
  - The driver has not resumed control

Feedback info:
  - Inadequate driver input

## UCA-6.22: Apollo stops applying brake control when collision occurs and driver has not resumed control (e.g. manual braking)

#### Type 1.22:
  - Apollo stops applying brake control when collision occurs and driver has not resumed control
  - The feedback does indicate that a collision has occurred and that the driver has not resumed control

#### Type 2.22:
  - The feedback does not indicate that a collision has occurred or it indicates that the driver has resumed control
  - A collision has occurred and the driver has not resumed control

Feedback info:
  - Inadequate collision detection
  - Inadequate driver input

## Type 3 & 4

  * Type 3:
    - Apollo does provide brake control
    - The vehicle's brake system does not receive brake control action from Apollo

  * Type 4:
    - The vehicle's brake system receives a brake control
    - The vehicle does not decelerate
