# Scenario Analysis for Unsafe Control Actions: Brake Control

## Unsafe by Not Providing

### UCA-6.1: Apollo does not provide the brake control action when relative velocity and distance to an obstacle mean that a collision is imminent.

#### True statement from UCA context: The vehicle is approaching an obstacle with a velocity and acceleration vector that indicate a collision

Belief:

 - Apollo <u>incorrectly</u> believes that the relative velocity is lower
        than in reality so that there is no need to brake

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to accurately determine the relative velocity

      -   <u>How this could happen given the true statement above:</u>

          -   The radar sensor (doppler) / lidar sensor (point cloud)
              is compromised
          -   A data error on the vehicle CAN bus prevents accurate,
              up-to-date data being received
          -   The process model receives stale relative speed (e.g.
              doppler information) and fails to correlate the changing
              point-position of the object with a dangerous relative
              velocity

Type 1 scenario:

   - <u>Controller receives correct feedback but interprets it
          incorrectly or ignores it:</u>

      -   Information received: At least one sensor presents an accurate distance measurement, but it is overridden by the process model

      -   <u>How this could occur given the true statement above</u>

          -  A malfunctioning sensor yielding an incorrect value leads to the true value being overwritten, overridden, or distorted

Belief:

- Apollo incorrectly believes that the relative distance is higher
      than in reality

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to accurately determine the relative distance

      -   <u>How this could occur given the true statement above:</u>

          -   The rangefinding or object tracking sensors are
              compromised, [HOW-1]

              -   Roof mounted optics are vulnerable to collision with
                  a variety of unexpected obstacles, and could
                  therefore have their optical alignment and focus
                  compromised
              -   Environmental or load-shed debris such as leaves or
                  plastic bags could block or distort the images /
                  beams
              -   The relevant sensor suffers an internal failure

Type 1 scenario:

   - <u>Controller receives correct feedback but interprets it
          incorrectly or ignores it:</u>

      -   Information received: The feedback received has a conflict

          -   Apollo was presented with accurate data from at least
              one sensor, but it was discarded due to a process model
              conflict

Belief:

- Apollo incorrectly believes that the obstacle will clear the
      vehicle’s path

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: Feedback indicates that the obstacle
          and vehicle will not cross paths

      -   <u>How this could occur given the true statement above:</u>

          -   The sensors used to determine the relative distance /
              paths or the obstacles are compromised, similar to
              [HOW-1]

#### True statement from UCA context: The vehicle is approaching an obstacle with a velocity and acceleration vector that indicate a collision will occur given *adverse weather or environmental conditions*

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo does not believe that adverse conditions that require special action exist (or else does not account for them)

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to accurately determine the current weather / environmental
          conditions

      -   <u>How this could occur given the true statement
          above: </u> [HOW-2]

          -   Cold conditions have rendered the road icy such that the
              ‘black ice’ is optically difficult to detect
          -   Standing water or water run-off can create wet road
              conditions when ‘raining’ feedback is not received
          -   The environmental condition is not weather related - a
              chemical spill, oil spill, or other shed load leads to
              conditions slippery conditions that the optical /
              environmental sensors are not calibrated to detect.
          -   Debris and slippery mud left by farm vehicles, soggy
              leaves from trees, or other commonly occurring
              substances, that are beneath the finesse of the sensors,
              reduce the vehicles traction on the road

Type 1 scenario:

   - <u>Controller receives correct feedback but interprets it
          incorrectly or ignores it:</u>

      -   <u>How this could occur given the true statement above:</u>

          -   Physical conditions could arise in any of the ways
              described in HOW-2 above
          -   The sensors present images / points / data with
              sufficient clarity to deduce the conditions, but the the
              algorithm is not equipped to look for black ice, leaves,
              water, unforeseen spillages or environmental debris

### UCA-6.2: Apollo does not provide brake control when in autonomous mode and vehicle speed exceeds limits (limits for controllability, stability, upcoming manoeuvre, speed limit, traffic flow limit, planned test limit, etc.)

#### True statement from UCA context: Vehicle is rapidly approaching / traversing a corner or bend in the road at excessive speed

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes that the vehicle is in a different location

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received does not
          indicate a vehicle location corresponding to a road-path
          manoeuvre

      -   <u>How this could happen given the true statement above:</u>

          -   GPS / GNSS / IMU sensors are offline, reporting stale
              data, or data transmission is delayed
          -   Optical systems are offline, reporting stale data, or
              transmission is delayed

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that the road path curvature radius is
      higher than in reality

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to determine the road curvature radius\[FB-2\] because
          optical equipment is misaligned, distorted, destroyed, or
          unavailable.

      -   <u>How this could happen given the true statement:</u>

          -   Roof mounted optics are vulnerable to collision with a
              variety of unexpected obstacles, and could therefore
              have their optical alignment and focus compromised
          -   Environmental or load-shed debris such as leaves or
              plastic bags could block or distort the images / beams
          -   The sensor suffers an internal failure

Type 1 scenario:

   - Controller receives information but processes it
          incorrectly / ignores it:

      -   Information received: The feedback received is sufficient to
          determine the road curvature radius\[FB-3\]

      -   <u>How this could happen given the true statement:</u>

          -   The mathematical calculations inside Apollo fail to
              process the data correctly
          -   The Apollo algorithm does not attempt to calculate road
              curvature within its process model, relying on other
              data, such as map position, deducing an incorrect
              curvature due to inaccurate positioning or an
              out-of-date map

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that the vehicle speed is lower than in
      reality

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received indicates a road
          speed lower than in reality\[FB-4\]

      -   <u>How this could occur given the true statement
          above</u> \[HOW-4\]

          -   Sensor malfunction reports a speed that is lower than in
              reality

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that the vehicle is in a unstable state
      when it is not


#### True statement from UCA context: Vehicle is approaching or traversing a corner or bend in the road at standard speed when adverse weather or environmental conditions render this speed excessive

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly identifies or ignores adverse weather / road
      conditions

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to accurately determine the current weather / environmental
          conditions

      -   <u>How this could occur given the true statement
          above: </u>

          -   *refer to HOW-2, above*

Type 1 scenario:

   - <u>Controller receives correct feedback but interprets it
          incorrectly or ignores it:</u>

      -   <u>How this could occur given the true statement above:</u>

          -   Physical conditions could arise in any of the ways
              described in HOW-2, above
          -   the algorithm is not equipped to look for black ice, leaves,
              water, unforeseen spillages or environmental debris

#### True statement from UCA context: The vehicle is travelling faster than the prevailing traffic flow limit

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes it is travelling below the traffic flow
      limit

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: Feedback received is insufficient to
          determine the traffic flow limit

      -   <u>How this could occur given the true statement above:</u>

          -   Optical / lidar sensors present insufficient data /
              F.O.V to make an accurate determination

Type 1 scenario:

   - <u>Controller receives correct feedback but interprets it
          incorrectly or ignores it:</u>

      -   Information received: Apollo receives adequate regarding
          surrounding objects, but does not process this into the a
          correct traffic flow limit

   - <u>How this could occur given the true statement above:</u>

      -   Apollo algorithm determines an inaccurate flow speed
            due to inappropriate weighting of the data
      -   Apollo lacks the processor power or process model to
            calculate the traffic flow speed

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: Apollo receives information that the
          vehicle speed is lower than in reality

          -   Sensor failure or data bus error results in incorrect
              information being presented to Apollo

#### True statement from UCA context: The vehicle is speeding above the planned test speed limit

 - <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes that there is no planned test limit

    - Controller receives no planned test limit

 - <u>How this could occur given the true statement above:</u>

    - Human pilot has failed to activate this mode

### UCA-6.3: Apollo does not provide brake control when in autonomous mode, the vehicle is stationary, and vehicle path is not clear

#### True statement from UCA context: Apollo is parked at a traffic lights at red but does not apply brakes as required by driving code *(human driver would be required to apply the handbrake)*

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      mistakenly believes the lights are at green

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to determine that the traffic lights are at red
      -   <u>How this could happen given the true statement above:</u>

          -   Debris on the camera(s) prevents traffic light state
              detection
          -   Cameras are not available
          -   Camera(s) have more than one traffic light in the field
              of view, leading to a conflicting reading on the
              appropriate traffic light state from the various sensors

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that there is no obstacle in its path

Type 2 scenario:

 - <u>Controller receives incorrect feedback / information:</u>

      - Information received: The feedback received is insufficient to determine that there is an obstacle in the vehicles path.

  -   <u>How this could occur given the true statement above:</u>

      - Sensor failure as described in [HOW-1]
      - An 'obstacle' such as a human being enters the field of view, but collapses to the floor, outside of the field of view of the sensors

Type 1 scenario:

 - <u>Inadequate control algorithm / hardware:</u>
    - Apollo processes data received too slowly, such that the
        data processed already reflects an earlier physical
        scenario that is now inappropriate
    - Incorrect reconciliation of optical and other
        range-finding techniques causes incorrect obstacle
        tracking

### UCA-6.4: Apollo does not provide brake control when in autonomous mode and the vehicle has reached the final destination

#### True statement from UCA context: The vehicle has reached the route destination

Belief:

- <u>Controller process model that could cause UCA:</u>  Apollo mistakenly believes that it has not reached the destination, and is in another location

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient to determine the vehicle location
      -   <u>How this could happen given the true statement above:</u>

          -   GPS / GNSS fault
          -   Lidar sensor failure as described in HOW-1

Type 1 scenario:

   - <u>Inadequate control algorithm:</u>

      -   The controller algorithm identifies the end of the journey, but is not programmed to provide the brake at the end of the the journey
      -   The controller receives adequate feedback but does not correctly identify the end of the journey

### UCA-6.5: Apollo does not provide brake control when in autonomous mode and collision occurs

#### True statement from UCA context: The vehicle has suffered a collision and must stop (if only to comply with highway registration)

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes that no collision has taken place

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>
      -   Information received: The feedback received is insufficient
          to determine that a crash has taken place

      -   <u>How this could occur given the true statement above:</u>

          -   The collision itself has compromised the sensors that were designed to detect the collision
          -   The collision has managed to happen in a manner which is not detected by the sensors, but still represents a critical failure, could include: a broken windscreen, an item impaling the engine or passenger compartment, bumper or exhaust hanging off (in the case of a rear collision)


Type 2 scenario:

   - <u>Necessary controller/feedback information does not exist</u>

      -   <u>How this could occur given the true statement above:</u>

        -   Specific collision sensors have not been built into the vehicle design
        -   Collision sensors exist, but have not been routed through the appropriate data interfaces

Type 1 scenario:

   - <u>Controller receives correct feedback but interprets it incorrectly or ignores it:</u>

      -   Information received: The vehicle sensors report a collision or critical vehicle damage state
      -   <u>How this could happen given the true statement above:</u>

          -   No collision contingency exists i.e. the vehicle is not programmed to brake, then engage neutral followed by the parking brake (standard emergency stop procedure in the UK)
          -   Failure to stop after a collision is an offence in most countries, therefore the vehicle should be brought to rest, and then manoeuvred to a safe position if required

## Unsafe by providing

### UCA-6.7: Apollo provides brake command with insufficient amount of braking below the minimum amount needed to avert a forward collision

#### True statement from UCA context: The vehicle is approaching an obstacle with a velocity and acceleration vector such that the vehicle will not be brought to rest in time to avert a collision

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes that the relative velocity is lower than in reality

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>
      -   Information received: The feedback received is insufficient
          to accurately determine the relative velocity

      -   <u>How this could occur given the true statement above:</u>

          -   The radar sensor (doppler) is compromised
          -   *also refer to [HOW-1]*

Type 1 scenario:

   - <u>Controller receives correct feedback but interprets it
          incorrectly or ignores it:</u>

      -   Information received: The sensors presented some accurate
          information, but one sensor has failed and presents
          inaccurate information
      -   <u>How this could happen given the true statement above:</u>

          -   Apollo was presented with accurate data from at least
              one sensor, but it was discarded due to a process model
              conflict

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes that the relative distance is higher than in reality

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to accurately determine the relative distance

      -   <u>How this could occur given the true statement above:</u>

          -   The rangefinding or object tracking sensors are
              compromised, similar to [HOW-1]

Type 2 scenario:

   - <u>Controller does not receive feedback/information when needed:</u>

      -   Information received: the current data reflects a time when
          the distance to the obstacle was greater
      -   <u>How this could occur given the true statement above:</u>

          -   The data from the sensors is delayed at source due to
              poor sensor performance
          -   The data is delayed in transmission due to insufficient
              transmission medium bandwidth
          -   The data is delayed entering into the Apollo software
              due to a data bottleneck in the hardware platform

Type 1 scenario:

   - <u>Controller receives correct feedback but interprets it
          incorrectly or ignores it:</u>

      -   Information received: The feedback received is sufficient to
          accurately determine the relative velocity

          -   Apollo was presented with accurate data from at least
              one sensor, but it was discarded due to a process model
              conflict

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly determines the deceleration needed

Type 1 scenario:

   - <u>Controller receives correct feedback but interprets it
          incorrectly or ignores it:</u>

      -   Information received: All the necessary feedback to
          calculate the relevant trajectories was received

      -   <u>How this could occur given the true statement above:</u>

          -   The control algorithm does not adapt sufficiently
              quickly to calculate the obstacle dynamics, where an
              obstacle decelerates rapidly, so that the braking
              amount is underestimated

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes that it is applying an amount of
      deceleration different to reality

Type 1 scenario:

-   <u>Inadequate control algorithm:</u>

    -   Apollo algorithm brake percentage is not correctly
        calibrated for the vehicle, and does not adapt
        heuristically as a human would
    -   Vehicle mass is much higher than normal due to heavy
        loading, which is not accounted for in the algorithm
    -   A mechanical failure causes incorrect braking but the
        algorithm does not account for this by increasing the
        braking amount

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes that the obstacle will clear the vehicle’s path

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: Feedback indicates that the obstacle
          and vehicle will not cross paths

      -   <u>How this could occur given the true statement above:</u>

          -   The sensors used to determine the relative distance /
              paths or the obstacles are compromised, similar to [HOW-1]

Type 1 scenario:

- <u>Inadequate control algorithm:</u>

    -   The feedback received is sufficient to predict the
        obstacle and vehicle paths – some lag in processing
        coupled with a sudden change in direction of the
        obstacle lead to insufficient braking being calculated

#### True statement from UCA context: The vehicle is approaching an obstacle with a velocity and acceleration vector such that the vehicle will not be brought to rest in time to avert a collision *in adverse weather conditions*

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly identifies adverse weather / road conditions, and
      therefore incorrectly believes that it is applying an amount of
      deceleration different to reality

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to accurately determine the current weather / environmental
          conditions

      -   <u>How this could occur given the true statement above:</u>

          -   *Weather conditions are imperceptible to sensors,
              similar to description* [HOW-2]

Type 1 scenario:

-   <u>Inadequate control algorithm:</u>

    -   Control model does not account for adverse weather
        conditions when determining the amount of braking to
        apply, and does not heuristically account for the
        deficit

### UCA-6.8: Apollo provides brake command when autonomous driving is not active (off, standby, overridden, or e-stop)

#### True statement from UCA context: The vehicle is moving and the human driver takes control, but Apollo continues to brake

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that autonomous mode is (should be) active

Type 2 scenario:

   - <u>Controller does not receive feedback/information when
          needed:</u>

      -   Information received: vehicle overrides were external to
          Apollo – Apollo is unaware of override conditions

      -   <u>How this could occur given the true statement above:</u>

          -   The human driver has overridden control on one or more
              control paths, but this does not include the brakes and
              so braking commands are still sent
          -   After an emergency override of all controls, no feedback
              is presented to Apollo, such that when the mode is
              disengaged Apollo will issue controls without autonomous
              mode being reactivated

### UCA-6.9: Apollo provides brake control when vehicle speed does not exceed limits (speed limit, traffic flow limit, manoeuvre limit, planned test limit, etc.), there is no obstacle, no faults, destination is reachable, and vehicle has not reached destination

#### True statement from UCA context: there is no need to apply the brakes – no obstacles, the speed limit has not changed, and the vehicle is not going down hill

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes that an obstacle is present in the roadway

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback is a sensor ghost,
          corresponding to a forward obstacle

      -   <u>How this could occur given the true statement above:</u>

          -   A sensor error is causing a ‘ghost’ object to appear,
              where delayed or cached feedback is sent to Apollo
              describing an object that is no longer there

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes that it has entered a new speed
      limit zone

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to accurately determine the vehicle position

      -   <u>How this could occur given the true statement above:</u>

          -   A GNSS / GPS / lidar fault has caused data corresponding
              a new speed limit zone
          -   The position data is correct but the map (containing
              speed zone information) itself is incorrect

      -   Information received: The feedback is insufficient to
          accurately identify and read a speed limit display or
          sign

      -   <u>How this could occur given the true statement above:</u>

          -   Apollo systems misread some object as a speed limit sign
              / display due to poor data
          -   Apollo systems misread a valid speed limit sign /
              display due to poor data

Type 2 scenario:

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes that the vehicle is going down hill

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received corresponds to
          some rate of change of altitude

      -   <u>How this could occur given the true statement above:</u>

          -   Barometric / IMU / pitch sensors present information
              corresponding to descent which is either incorrect or
              cannot be resolved correctly

#### True statement from UCA context: there is no need to apply the brakes – the speed limit zone has changed, but the speed restriction does not apply at the current time (for example, a school zone on a Saturday).

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes that it has entered a new speed
      limit zone

Type 1 scenario:

- <u>Inadequate control algorithm:</u>

    -   Map data held is incorrect, or holds incorrect time
        dependencies for zones
    -   Apollo slows down for e.g. a school zone outside of the
        school’s operating hours, because the algorithm does not
        account for the time dependency of speed limit zones

### UCA-6.10: Apollo provides brake control when driver is providing throttle

#### True statement from UCA context: The human driver feels it best to accelerate e.g. for safety reasons

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes that it is safe to apply the brakes
      while the driver is accelerating

Type 2 scenario:

   - <u>Controller does not receive feedback/information when
          needed:</u>

      -   Information received: Apollo is not aware that the driver is
          accelerating

      -   <u>How this could occur given the true statement above:</u>

          -   The feedback that a manual acceleration is taking place
              is not passed to Apollo

Type 1 scenario:

   - Apollo disregards human actions and applies the brakes
          anyway

### UCA-6.11: Apollo provides excessive brake command when wheel lock has occurred and lateral control is needed  (rationale: ABS may not work below 5mph or other situations)

#### True statement from UCA context: Apollo is applying brakes to slow down, in the context of an ABS failure to activate while the wheels are slipping

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes applying maximum brake will lead to the quickest deceleration

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: Apollo receives feedback that ABS is healthy

      -   <u>How this could occur given the true statement above:</u>

          -  The ABS actuator unit is supplying incorrect feedback
          -  The ABS actuator has failed but its state is not monitored in the feedback chain

Type 1 scenario:

   - <u>Inadequate control algorithm / hardware:</u>

      -   Information received: The feedback is received that ABS has failed, but does not take this into account

      -   <u>How this could occur given the true statement above:</u>

          -  The algorithm does not account for ABS failure in its brake calculations


### UCA-6.12: Apollo provides brake command with insufficient amount of braking to reduce vehicle speed within limits (limits for controllability, stability, upcoming manoeuvre, speed limit, traffic flow limit, planned test limit, etc.)

#### True statement from UCA context: The vehicle is coming upon a corner or other path feature that requires a lower speed for safe manoeuvre

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that the vehicle is in a different location

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received indicates a
          greater distance to the path manoeuvre than in reality
      -   <u>How this could occur given the true statement above:</u>

          -   Sensor failure similar to [HOW-1] causes road features
              to be miscalculated
          -   A GPS / GNSS fault causes the manoeuvre distance to be
              fed back incorrectly

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that the path manoeuvre itself is required
      in a different location than in reality

Type 2 scenario:

   - Information received: Apollo receives feedback or
          information indicating that the manoeuvre is in an incorrect
          location

      -   <u>How this could occur given the true statement above:</u>

          -   The GPS / GNSS data received is correct, but out-of-date
              map data indicates the manoeuvre in an incorrect
              location because the road layout or right-of-way has
              changed
          -   Temporary roadworks / path diversions are not marked on
              the HD map such that Apollo will not slow down for, or
              avoid, a static obstacle until it is physically detected
          -   Sensor failure as described in [HOW-1] leads to
              failure to detect the correct road path

Type 1 scenario:

- <u>Inadequate control algorithm:</u>

    -   Apollo has not been programmed or calibrated to respond
        to changes in the right-of-way, or temporary road
        layouts

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that the road path curvature radius is
      higher than in reality

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to determine the road curvature radius
      -   <u>How this could occur given the true statement above:</u>

          -   Sensors are compromised, similar to [HOW-1]
          -   The physical route has been revised, but the HD map was
              not updated – which could itself be caused by a network
              or technician error
Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes that the vehicle speed is lower than
      in reality

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to determine the vehicle speed

      -   <u>How this could occur given the true statement above:</u>

          -   Speed sensor error or feedback failure from the vehicle
              chassis

#### True statement from UCA context: The vehicle is coming upon a corner or other path feature that requires a lower speed for safe manoeuvre due to *adverse weather conditions*

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly identifies adverse weather / road conditions, and
      therefore incorrectly believes that it is applying an amount of
      deceleration different to reality

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to accurately determine the current weather / environmental
          conditions

      -   <u>How this could occur given the true statement above:</u>

          -   *Weather conditions are imperceptible to sensors,
              similar to description* [HOW-2]

Type 1 scenario:

-   <u>Inadequate control algorithm:</u>

    -   Control model does not account for adverse weather
        conditions when determining the amount of braking to
        apply, and does not heuristically account for the
        deficit


#### True statement from UCA context: The vehicle is coming upon a corner or other path feature that requires a lower speed for safe manoeuvre

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that the safe manoeuvre speed is higher
      than in reality because it has failed to identify adverse
      weather / road conditions

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to accurately determine the current weather / environmental
          conditions

      -   <u>How this could occur given the true statement above:</u>

          -   Weather conditions are imperceptible to sensors,
              similar to description [HOW-2]

Type 1 scenario:

- <u>Inadequate control algorithm:</u>

    -   Control model does not account for adverse weather
        conditions of the prevailing type when determining the
        safe speed limit for the upcoming manoeuvre

#### True statement from UCA context: The vehicle suffers a momentary instability which requires the reduction in the braking amount that is then rectified

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes that the vehicle is in a unstable
      state when it is not

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback is insufficient to
          determine that the vehicle is / has become stable

      -   <u>How this could occur given the true statement above:</u>

          -   Feedback from stability sensors lead to the brakes being
              released, but these were ‘locked’ in state leading to
              Apollo continuing to refrain from braking when it would
              now be safer to do so
          -   The stability sensors have failed leading to stale or
              inaccurate feedback

Type 1 scenario:

- <u>Inadequate control algorithm:</u>

    -   Apollo incorrectly amalgamates sensor data leading it to
        believe that the vehicle has become unstable


### UCA-6.13: A provides a brake command that is excessive beyond the physical limit of the passengers

#### True statement from UCA context: Apollo causes the vehicle to decelerate rapidly enough to cause physical injury to the occupants, when it is unnecessary in the context of averting a worse collision

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo applies
      normal braking

Type 1 scenario:

- <u>Inadequate control algorithm:</u>

    -   Apollo is incorrectly calibrated such that applying
        brakes normally results in excessive braking

Type 3:

- Actuators respond inadequately:

    -   The brake actuators receive a ‘reasonable’ brake
        percentage command, proportional to the circumstances,
        but due to a physical or electronic error apply
        excessive force
    -   Following feedback: Apollo fails to respond by
        decreasing the brake percentage, or releasing the
        control

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that a collision far worse is about to take
      place, full brakes are applied

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: Feedback corresponding to a collision
          is received

      -   <u>How this could occur given the true statement above:</u>

          -   Near miss collision data is interpreted as a collision due
              to slight time stamp errors, meaning that a moving
              vehicle in front is interpreted as static

Type 1 scenario:

- <u>Inadequate control algorithm / hardware:</u>

    -   Apollo miscalculates collision parameters due to time
        pressure, resulting in avoidable injury
    -   Trajectory calculations incorrectly account for vehicle
        deceleration

Type 2 scenario:

   - <u>Controller does not receive feedback/information when
          needed:</u>

      -   Information received: Information corresponding to an
          obstacle is received late, requiring that the vehicle brake
          much more severely than would have been required had the
          information been received promptly.

#### True statement from UCA context: The vehicle is in a location where stopping is never appropriate when the path is open, such as a motorway / highway, when another vehicle has unavoidably stopped due to a brake down

Type 1 scenario:

- <u>Inadequate control algorithm / hardware:</u>

    -   Bulk traffic tracking fails: The vehicle pulls up behind
        a broken down vehicle rather than evading it,
        exacerbating the dangerous traffic build up

#### True statement from UCA context: The vehicle is in a location where stopping is never appropriate when the path is open, such as a motorway / highway

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that there is an obstacle configuration
      that constitutes ‘an emergency’

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Feedback received: Apollo receives feedback corresponding to
          a stationary / rapidly decelerating traffic ahead, in the
          bulk of the road

      -   <u>How this could occur given the true statement above:</u>

          -   Sensor failure similar to [HOW-1]

## Too Early / Too late

### UCA-6.14: Apollo provides brake control too late (TBD sec) after relative velocity and distance to an obstacle mean that a collision is imminent

#### True statement from UCA context: An opportunity to brake in order to avoid a collision with an obstacle is being missed

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that there is no present need to brake

Type 2 scenario:

   - <u>Controller does not receive feedback/information when
          needed:</u>

   - Apollo receives feedback of an upcoming obstacle too late

      -   <u>How this could occur given the true statement above:</u>

          -   Feedback is delayed due to internal processing or lag of
              the sensors themselves
          -   Feedback is delayed due to limited or unavailability of
              transmission bandwidth

Type 1 scenario:

- <u>Inadequate control algorithm / hardware:</u>

    -   Apollo processes data received too slowly, such that the
        data processed already reflects an earlier physical
        scenario that is now inappropriate

        -   Apollo has insufficient processor resources to
            process the data
        -   Apollo processor resources are unavailable

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: is insufficient to accurately
          determine the correct time to brake

      -   <u>How this could occur given the true statement above:</u>

          -   Compromised sensors present an inaccurate / unavailable
              range data due to reasons similar to [HOW-1]

Type 1 scenario:

- <u>Inadequate control algorithm / hardware:</u>

    -   Tracking failure: A vehicle travelling at a relatively
        slow speed is temporarily obscured by a faster moving
        vehicle pulling in front of it, since visual contact is
        lost Apollo fails to slow down
    -   Fundamental programming error

### UCA-6.15: Apollo provides braking control too late (> tbd seconds) prior to manoeuvre.

#### True statement from UCA context: An opportunity to brake in order to avoid a collision with an obstacle is being missed

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that there is no present need to brake

Type 2 scenario:

   - <u>Controller does not receive feedback/information when
          needed:</u>

      -   Information received: Apollo receives feedback about an
          obstacle too late

      -   <u>How this could occur given the true statement above:</u>

-  - Feedback is delayed due to internal processing or lag of
              the sensors themselves
          -   Feedback is delayed due to limited or unavailability of
              transmission bandwidth

Type 1 scenario:

- <u>Inadequate control algorithm / hardware:</u>

    -   Apollo processes data received too slowly, such that the
        data processed already reflects an earlier physical
        scenario that is now inappropriate

        -   Apollo has insufficient processor resources to
            process the data
        -   Apollo processor resources are unavailable

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: is insufficient to accurately
          determine the correct time to brake

      -   <u>How this could occur given the true statement above:</u>

          -   Compromised sensors present an inaccurate / unavailable
              range data due to reasons similar to [HOW-1]

Type 1 scenario:

- <u>Inadequate control algorithm / hardware:</u>

    -   Tracking failure: A vehicle travelling at a relatively
        slow speed is temporarily obscured by a faster moving
        vehicle pulling in front of it, since visual contact is
        lost Apollo fails to slow down
    -   Fundamental programming error

### UCA-6.16: Apollo provides brake control too late before (< TBD sec before) limits are exceeded (limits for upcoming manoeuvre, controllability, stability, speed limit, traffic flow limit, planned test limit, etc.)

#### True statement from UCA context: The vehicle is passing through the point where gentle braking will suffice, such that the vehicle has not begun to brake and more severe braking or stability compromise will ensue

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that there is no present need to brake

Type 2 scenario:

   - <u>Controller does not receive feedback/information when
          needed:</u>

      -   Information received: Apollo receives feedback about an
          obstacle too late

      -   <u>How this could occur given the true statement above:</u>


-  - Feedback is delayed due to internal processing or lag of
              the sensors themselves
          -   Feedback is delayed due to limited or unavailability of
              transmission bandwidth

Type 1 scenario:

- <u>Inadequate control algorithm / hardware:</u>

  -   Apollo processes data received too slowly, such that the
      data processed already reflects an earlier physical
      scenario that is now inappropriate

      -   Apollo has insufficient processor resources to
          process the data
      -   Apollo processor resources are unavailable

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: is insufficient to accurately
          determine the correct time to brake

      -   <u>How this could occur given the true statement above:</u>

-  - Compromised sensors present an inaccurate / unavailable
              range data due to reasons similar to [HOW-1]

Type 1 scenario:

- <u>Inadequate control algorithm / hardware:</u>

    -   The control algorithm does not account for vehicle
        stability prior to arriving at the apex, treating the
        curve as a discrete point rather than a contiguous path

#### True statement from UCA context: The vehicle is approaching the point where the vehicle would normally brake, but adverse weather conditions (road traction) require that the braking should begin earlier than normal

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that the point at which braking is
      required is as normal, because has failed to identify adverse
      weather / road conditions that will reduce the effectiveness of
      applied braking

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to accurately determine the current weather / environmental
          conditions

     -   <u>How this could occur given the true statement above:</u>

          -   Weather conditions are imperceptible to sensors,
              similar to description [HOW-2]

Type 1 scenario:

- <u>Inadequate control algorithm:</u>

      -   Control model does not account for adverse weather
          conditions of the prevailing type when determining the
          deceleration limit when braking for the upcoming
          manoeuvre

## Stopped too soon, applied too long

### UCA-6.17: Apollo removes brake control too early when relative velocity and distance to an obstacle mean that a collision will occur

#### True statement from UCA context: The vehicle is approaching an obstacle, and slows down to some extent but then removes the braking control

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that it has achieved a vehicle target
      velocity consistent with the planned reduction in relative
      velocity

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to accurately determine the vehicle velocity

      -   <u>How this could occur given the true statement above:</u>

          -   Sensor failure / failure to retrieve speed data from the
              vehicle, or retrieves an incorrect value

Type 1 scenario:

- <u>Inadequate control algorithm:</u>

    -   Assumed deceleration is used to calculate braking
        duration rather than monitoring the actual vehicle
        velocity
    -   Apollo was presented with accurate data from at least
        one sensor, but it was discarded due to a process model
        conflict

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      miscalculates the target velocity

Type 1 scenario:

- <u>Inadequate control algorithm / hardware:</u>

    -   Apollo miscalculates due to a programming fault
    -   Incorrect reconciliation of optical and other
        range-finding techniques causes incorrect obstacle
        tracking

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that the relative distance is higher than
      in reality

    -   The feedback received is insufficient to accurately
        determine the relative distance

        -   Environmental sensors are compromised

#### True statement from UCA context: The original target velocity was achieved but a changing obstacle path now requires further action

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that the original reduction in velocity was
      sufficient

Type 2 scenario:

   - <u>Controller does not receive feedback/information when
          needed:</u>
      -   Information received: The feedback is insufficiently prompt
          to allow the process model to be updated in time to take
          action

      -   <u>How this could occur given the true statement above:</u>

          -   Sensor lag causes the updated data to be presented too
              slowly
          -   Communication bandwidth is insufficient to allow the
              data to be received quickly enough

Type 1 scenario:

- <u>Inadequate control algorithm / hardware:</u>

    -   Insufficient resources such that the cycle between
        receipt of the new sensor data implying the need for
        further braking and a command being sent is too long
    -   Excessive weight is placed on previous calculations
        leading to a trajectory that does not decelerate rapidly
        enough

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that the obstacle will clear the vehicle’s
      path

Type 2 scenario:

- <u>Controller receives incorrect feedback / information:</u>

  -   Information received: The feedback received is insufficient
      to accurately predict obstacle’s path

  -   <u>How this could occur given the true statement above:</u>

      -   The vehicle was originally on trajectory to leave the
          lane but e.g. has swerved back suddenly
      -   Environmental sensors are compromised
      -   The GPS / GNSS, lidar or canbus is compromised

### UCA-6.18: Apollo removes brake control too early (> TBD seconds) prior to/during manoeuvre

- *6.18 should be merged with 6.19, below*


### UCA-6.19: Apollo stops applying brake control when in autonomous mode before (> TBD seconds before) vehicle slows to acceptable speed (speed limit, traffic flow limit, manoeuvre limit, planned test limit, limits for controllability, stability, etc.)

#### True statement from UCA context: The vehicle was decelerating at an appropriate rate in order to enter the manoeuvre

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that it has achieved a vehicle target
      velocity consistent with the planned manoeuvre

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   The feedback received is insufficient to accurately
          determine the vehicle velocity

      -   <u>How this could occur given the true statement above:</u>

          -   Environmental sensors are compromised
          -   The GPS / GNSS, lidar or canbus is compromised

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes it has entered the corner, apex, or exited
      the corner

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to accurately determine the current position relative to the
          manoeuvre being executed

      -   <u>How this could occur given the true statement above:</u>

          -   Feedback parameters are distorted due to equipment
              failure or damage
          -   Apollo is misdirected by out-of-date map information
          -   Apollo miscalculates its position and planned trajectory

#### True statement from UCA context: The vehicle has decelerated approaching a manoeuvre, but deceleration has ceased prior to achieving a safe speed with which to execute the manoeuvre

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that the safe speed for the manoeuvre is
      higher than in reality

Type 2 scenario:

-   The feedback received is insufficient to determine the
    required manoeuvre velocity

-   <u>How this could occur given the true statement above:</u>

    -   The change in perspective as the vehicle begins to enter
        the bend leads to an underestimation of the remaining
        curvature, due to limited field-of-view

#### True statement from UCA context: The vehicle has completed ‘standard’ deceleration for the manoeuvre, but further deceleration is required because of adverse weather / road conditions

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes that the safe manoeuvre speed is higher
      than in reality because it has failed to identify adverse
      weather / road conditions

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to accurately determine the current weather / environmental
          conditions

      -   <u>How this could occur given the true statement above:</u>

          -   Weather conditions are imperceptible to sensors,
              similar to description [HOW-2]

Type 1 scenario:

- <u>Inadequate control algorithm:</u>

    -   Weather conditions that lead to a slight slipping of the
        vehicle, and therefore reduced g-force, are interpreted
        as lower radius of curvature or a higher maximum speed

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      incorrectly believes it has become unstable – is rolling,
      slipping on ice, etc

Type 1 scenario:

- <u>Inadequate control algorithm:</u>

  -   Information received: Feedback leads to incorrect assessment
      of the stability state of the vehicle

  -   <u>How this could occur given the true statement above:</u>

      -   Undulations in the road, coupled with fluctuations in
          the road surface texture and deviations in the road
          relative to a circular arc (that have been ‘splined out’
          in the planned trajectory), and these deviations are
          misinterpreted as vehicle slippage

### UCA-6.20: Apollo continues applying brake control too long (> TBD seconds) after vehicle slows to acceptable speed (speed limit, traffic flow limit, manoeuvre limit, planned test limit, limits for controllability, stability, etc.)

#### True statement from UCA context: The vehicle has approached a e.g. a corner, slowed down, but is now slowing down to a speed that is below the expectations of other driver and (for example) the UK highway code for 'progress'

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo incorrectly believes that the vehicle is travelling faster than in reality

Type 2 scenario:

   - <u>Controller receives incorrect feedback / information:</u>

      -   Information received: The feedback received is insufficient
          to accurately determine the vehicle speed

      -   <u>How this could occur given the true statement above:</u>

          -   sensor failure
          -   data transmission failure

   - <u>inadequate control algorithm:</u>

      -   The algorithm is actually excessively cautious, leading to the vehicle making an unexpected lack of progress, with the possible consequence of rear-end collision, or the flowing traffic having to evade the vehicle as if it were an obstacle


### UCA-6.21: Apollo stops applying brake control too soon at end of test before driver has resumed control (e.g. manual braking)

#### True statement from UCA context: The vehicle comes to a halt at some predesignated position, but the brakes have not been engaged prior to the human driver resuming control.

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo
      mistakenly believes that the human driver has taken control

Type 1 scenario:

   - <u>Inadequate control algorithm:</u> The control state transitions
          to human control mode

      -   <u>How this could occur given the true statement above:</u>

          -   Apollo automatically drops to human control without the
              human’s knowledge

      -   <u>Inadequate control algorithm:</u>

          -   Apollo does not account for the end of the test period
              and apply brakes (either a standard continuous brake
              command, or a transition to ‘Park’ mode)

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo mistakenly believes it is supplying sufficient brake

Type 2 scenario:

   - <u>Controller does not receive feedback/information when
          needed:</u>

      -   The feedback is insufficient to determine the correct level
          of braking

          -   Information such as the local angle of the road
              (relative to the vertical action of gravity) is either
              not fed back to the process model, or it is not taken
              into account

Type 1 scenario:

   - <u>Inadequate control algorithm:</u>

      -   Apollo does not account for enhanced braking requirement

          -   Due to being located on a hill, particularly if the
              local gradient is higher than that of the road generally
              in that location

### UCA-6.22: Apollo stops applying brake control when collision occurs and driver has not resumed control (e.g. manual braking)

#### True statement from UCA context: The vehicle has been brought to rest, but the vehicle drops out of automatic mode following a collision - leaving the vehicle free to move on e.g. a hill, or if further collisions take place

Belief:

- <u>Controller process model that could cause UCA:</u> Apollo mistakenly believes that the human driver has taken control

Type 1 scenario:

   - <u>Inadequate control algorithm:</u> The control state transitions to human control mode

      -   <u>How this could occur given the true statement above:</u>

          -   Following a collision and being brought to rest, automatic mode is simply ended without 'Park' being engaged.
          -   The collision and associated trajectory change are misinterpreted as a human override, leading to drop out of automatic mode


          -   The algorithm attempts to slow down to avoid a collision, but the algorithm does not recognise a post collision scenario, and therefore simply carries
