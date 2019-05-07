# Level 2 Scenario Analysis

## Controls

### Brakes

#### CA-6.1: Apollo provides the brake command in a prompt, correct manner when it is both safe and necessary to do so (rendered unsafe by not providing)

**True Statement from the CA context: It is necessary for the vehicle to brake, and Apollo sends the correct brake command**

Type 3 Scenario:

   -  Apollo sends the brake command and it is received by the actuator, but not applied to the controlled process

       - Improper execution: The brake actuator has failed and cannot apply braking

       - How this could occur given the true statement above:

           - A mechanical fault causes the physical part of the brake actuator to sieze

               - **REQUIREMENT REQ-1: Physical brake actuators must be designed must be designed and tested to be operationally reliable**


Type 3 Scenario:

   -  Apollo sends the brake command and it is received by the actuator, but not applied to the controlled process

       - Improper Execution: The actuator does not respond due to loss of power

       - How this could occur given the true statement above:

           - Battery / alternator system failure

               - **REQUIREMENT REQ-2: The battery / alternator power system must be designed and tested to be operationally**

           - Mechanical damage to the power supply route

               - **REQUIREMENT REQ-3: The power supply route to the brake actuators must be redundant if practicable**

           - A power supervisory system has incorrectly ordered the actuator to 'sleep'

               - **REQUIREMENT REQ-4: The power supply system must not issue brake actuator 'sleep' commands during normal operation**


Type 3 Scenario:

   -  Apollo sends the brake command and it is received by the actuator, but not applied to the controlled process

       - Improper Execution: The actuator does not respond due to data / buffer overload in the actuator

       - How this could occur given the true statement above:

           - The command transmission rate is too high and the message is discarded due to a buffer overflow

               - **REQUIREMENT REQ-5: The brake command transmission rate should not exceed the rate at which the brake actuators can process commands**

           - The command was about to be processed, but the buffer was purged due to a buffer overflow

               - **REQUIREMENT REQ-5: The brake command transmission rate should not exceed the rate at which the brake actuators can process commands**


               - **REQUIREMENT REQ-6: Any brake actuator buffers should routinely purge data on a FIFO basis**


Type 3 Scenario:

   -  Apollo sends the brake command and it is received by the actuator, but not applied to the controlled process

       - Improper Execution: due to incorrect priority scheme used by the actuator

       - How this could occur given the true statement above:

           - The brake actuator is locked out by an unterminated command

               - **REQUIREMENT REQ-7: The brake commands should not be implemented on a select-exectute model**

           - The actuator processes a command from another system that should have been disregarded

               - **REQUIREMENT REQ-8: All system commands must be mainted in a master I/O schedule that, where practicable, uses unique addressing for each component and command**

           - The actuator is time-stamp priority aware, but incorrect time synchronisation renders this priority scheme ineffective

               - **REQUIREMENT REQ-9: All vehicle systems must be time synchronised via an on-board clock master, rather than 'dialing out' to an off-vehicle source**


Type 3 Scenario:

   -  Apollo sends brake command but command it is not received by the actuator

       - Improper Execution: Transmission medium error prevents the command being received

       - How this could occur given the true statement above:

           - A primary transmission medium reports healthy but has a fault

               - **REQUIREMENT REQ-10: Transmission media should be polled regularly where practicable to ensure that false positives are not reported**

           - A primary path is severed by collision or other mechanical fault, and there is no redundant path

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - A redundant command transmission medium is incorrectly installed or parameterized, which is not revealed until primary route failure

               - **REQUIREMENT REQ-12: All transmission media should be polled or tested automatically, including secondary routes**

           - A redundant pathway performs correctly upon failure of the primary, but a conflict occurs on the restoration primary when one or more systems fail to revert

               - **REQUIREMENT REQ-13: All systems using the transmission media must determine the currently active route prior to commencing normal operation**


Type 3 Scenario:

   -  Apollo sends brake command but command it is not received by the actuator

       - Improper Execution: The command is not received due to a data / signal collision or overflow

       - How this could occur given the true statement above:

           - A buffering mechanism, combined with a temporary route loss, causes a route to be flooded with stale commands

               - **REQUIREMENT REQ-14: Buffered transmission must be accomplanied by a buffer purge when the route fails for longer > than TBD seconds**

           - The use of persistent send / send upon analogue change causes a rate of transmission that overloads the transmission medium

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**


               - **REQUIREMENT REQ-16: Analogue values should be transmitted cyclically, or a change threshold should be applied**

           - The use of excessive bandwidth by other systems on a shared transmission medium overloads the transmission medium

               - **REQUIREMENT REQ-17: Critical systems should take priority over non-critical systems when using the transmission media**


Type 4 Scenario:

   -  Apollo sends the command which is executed by the actuator, but the contolled process does not respond correctly

       - Improper Process response: the wheels hydroplane so no braking is applied

       - How this could occur given the true statement above:

           - The road is covered with standing water; the tyres loose contact with the ashphalt

               - **REQUIREMENT REQ-18: The autonomous system must be equipped with sensors and algorithms capable of detecting standing water, in order to slow down before entering**

           - An oil / water mix is present after a heavy shower; the tyres loose contact with the ashphalt

               - **REQUIREMENT REQ-19: The autonomous system must be capable of detecting when there is or has been heavy rain, in order to accound for reduced traction**


Type 4 Scenario:

   -  Apollo sends the command which is executed by the actuator, but the contolled process does not respond correctly

       - Improper Process response: the controlled process does not respond due to an auxiliary systems failure

       - How this could occur given the true statement above:

           - An critical auxiliary system, not on the control path, such as a hydraulic pump, compressor, or fluid line has failed

               - **REQUIREMENT REQ-20: Critical auxiliary systems must be designed and tested for operational reliability**


**True Statement from the CA context: It is necessary for the vehicle to brake, Apollo sends the correct command when a DataSpeed override is active - the human driver does not intercede**

Belief:

*The human driver believes that Apollo has command control of the vehicle - Apollo believes it has command control of the vehicle*

Type 3 Scenario:

   -  Apollo sends brake command but command it is not received by the actuator

       - Command rejection: the command is not received because it is discarded by DataSpeed

       - How this could occur given the true statement above:

           - The human driver pressed the brake previously, but believes that they pressed the brake below the override threshold

               - **REQUIREMENT REQ-21: The human driver should be warned (acoustically or visually) when they are about to exceed the override threshold**


               - **REQUIREMENT REQ-22: The human driver / monitor should be informed (acoustically or visually) when a channel override is activated or deactivated**

           - The human driver stands ready with their foot resting on the brake pedal, but is not aware that they pushed it at all

               - **REQUIREMENT REQ-21: The human driver should be warned (acoustically or visually) when they are about to exceed the override threshold**


               - **REQUIREMENT REQ-22: The human driver / monitor should be informed (acoustically or visually) when a channel override is activated or deactivated**

           - The safety monitor has pushed the e-stop button, but the human driver is not aware of this

               - **REQUIREMENT REQ-23: Both the driver and safety driver e-stop buttons should activate a klaxon or other warning device to signal all channels are overridden**

           - Short term, incorrect feedback from the vehicle triggers a brake channel override

               - **REQUIREMENT REQ-22: The human driver / monitor should be informed (acoustically or visually) when a channel override is activated or deactivated**

           - Incorrect parameters in a non braking system, cause other system feedback to be misinterpretted as a brake feedback - DataSpeed engages override

               - **REQUIREMENT REQ-8: All system commands must be mainted in a master I/O schedule that, where practicable, uses unique addressing for each component and command**


Belief:

*The human driver is aware of the DataSpeed override, but believes that the Safety Monitor has disengaged it*

Type 3 Scenario:

   -  Apollo sends brake command but command it is not received by the actuator

       - Command rejection: the command is not received because it is discarded by DataSpeed

       - How this could occur given the true statement above:

           - The safety monitor believes that s/he has disengaged the override, but the command was unsuccessful

               - **REQUIREMENT REQ-22: The human driver / monitor should be informed (acoustically or visually) when a channel override is activated or deactivated**

           - The safety monitor attempts to disengage the override, but the driver e-stop has not been disengaged

               - **REQUIREMENT REQ-24: E-stop controls should be non-latching since DataSpeed requires the override to be manually disabled already**

           - The safety monitor attempts to disengage the override, but their own own e-stop has not been disengaged

               - **REQUIREMENT REQ-24: E-stop controls should be non-latching since DataSpeed requires the override to be manually disabled already**


**True Statement from the CA context: It is necessary for the vehicle to brake, Apollo sends the correct command when an override is active - the override was previously disengaged**

Belief:

*The human driver is aware of the DataSpeed override and the Safety Monitors attempts to disengage it, but is not aware that this disengagement has already occurred*

Type 3 Scenario:

   -  Apollo sends brake command but command it is not received by the actuator

       - Command rejection: the command is not received because it is discarded by DataSpeed

       - How this could occur given the true statement above:

           - The safety monitor disengages the override, but the human driver is unaware of this and brakes - this re-engages this override

               - **REQUIREMENT REQ-22: The human driver / monitor should be informed (acoustically or visually) when a channel override is activated or deactivated**


#### CA-6.2: Apollo does not provide the brake command when it is unsafe to do so (later rendered unsafe by providing)

**True Statement from the CA context: It is unsafe to provide the brake control**

Type 3 scenario:

   -  Apollo does not send a braking command, but the actuator receives a braking command

       - Improper Execution: A command is received due to an error in the transmission medium

       - How this could occur given the true statement above:

           - A protocol converter or relay performs an incorrect operation or inversion on a transmitted signal

               - **REQUIREMENT REQ-25: Data types and formats should be kept consistent from command source through to actuator; unnecessary protocol conversion should be eliminated**

           - A mechanical fault causes cross talk between transmission media

               - **REQUIREMENT REQ-26: Transmission media should be rigorously isolated and designed and tested for operational reliability**


Type 3 scenario:

   -  Apollo does not send a braking command, but the actuator receives a braking command

       - Improper Execution: A transmitter sends a buffered command following communication loss or power outage

       - How this could occur given the true statement above:

           - A buffering mechanism causes a route to be flooded with stale commands that result in the brakes responding to a historical command

               - **REQUIREMENT REQ-14: Buffered transmission must be accomplanied by a buffer purge when the route fails for longer > than TBD seconds**


Type 3 scenario:

   -  The actuator does not receive a braking command, but the actuator applies braking

       - Improper Execution: The brakes are applied in error with no command received

       - How this could occur given the true statement above:

           - A clock resynchronisation causes a finite discontinuity in the actuator; a historical command is executed

               - **REQUIREMENT REQ-6: Any brake actuator buffers should routinely purge data on a FIFO basis**

           - An unknown command state occurs; the default action is to apply the brakes

               - **REQUIREMENT REQ-27: The brake actuators must not default to braking upon an unknown command state**

           - A electronic / mechanical failure causes the brakes to apply arbitrarily

               - **REQUIREMENT REQ-1: Physical brake actuators must be designed must be designed and tested to be operationally reliable**


Type 3 scenario:

   -  Apollo does not send a braking command, but the actuator receives a braking command

       - Improper Execution:  Another controller sends a brake command in error

       - How this could occur given the true statement above:

           - An incorrectly configured controller activates the brakes in error

               - **REQUIREMENT REQ-8: All system commands must be mainted in a master I/O schedule that, where practicable, uses unique addressing for each component and command**

           - The human driver activates the brakes in error

               - **REQUIREMENT REQ-28: The human driver should be constantly alert but should not cover the pedals unless braking may be likely**


#### CA-6.3: Apollo provides the braking command at the necessary level to ensure vehicle safety (later rendered unsafe by insufficient / excessive provision)

**True statement from the CA context: A specific level of braking is required, but it is not applied by the acutuator**

Type 4 Scenario:

   -  Apollo sends the command which is executed by the actuator, but the contolled process does not respond correctly

       - Improper Process response: the controlled process does not respond due to an auxiliary systems failure

       - How this could occur given the true statement above:

           - An critical auxiliary system, not on the control path, such as a hydraulic pump, compressor, or fluid line has failed

       - Improper process response: The wheels hydroplane or skid, leading to reduced braking effectiveness

       - How this could occur given the true statement above:

           - The road is covered with standing water; the tyres loose contact with the ashphalt

               - **REQUIREMENT REQ-18: The autonomous system must be equipped with sensors and algorithms capable of detecting standing water, in order to slow down before entering**

           - An oil / water mix is present after a heavy shower; the tyres loose contact with the ashphalt

               - **REQUIREMENT REQ-19: The autonomous system must be capable of detecting when there is or has been heavy rain, in order to accound for reduced traction**


Type 3 scenario:

   -  Apollo sends the braking command correctly, but insufficient / excessive braking is applied by the actuator

       - Improper execution: The actuator applies insufficicient / excessive braking due to incorrect configuration

       - How this could occur given the true statement above:

           - An incorrect configuration becomes active when the actuator's primary configuration storage medium fails

               - **REQUIREMENT REQ-29: Factory configuration should be used in the brake actuators with scaling changes applied in the controller, where practicable**

           - A firmware over the air update is not executed correctly, and an incorrect configuration becomes active

               - **REQUIREMENT REQ-30: All FOTA methods should have a cyclic check and automatic roll-back method in the event of a failed download**

           - A scaling or knee-point is applied incorrectly, resulting in an incorrect braking level

               - **REQUIREMENT REQ-29: Factory configuration should be used in the brake actuators with scaling changes applied in the controller, where practicable**


Type 3 scenario:

   -  Apollo sends the braking command correctly, but insufficient / excessive braking is applied by the actuator

       - Improper execution: The actuator receives and incorrect command due to corruption in the transmission medium

       - How this could occur given the true statement above:

           - A protocol converter or relay performs an incorrect operation or inversion on a transmitted signal

               - **REQUIREMENT REQ-26: Transmission media should be rigorously isolated and designed and tested for operational reliability**

           - A mechanical fault causes cross talk between transmission media

               - **REQUIREMENT REQ-26: Transmission media should be rigorously isolated and designed and tested for operational reliability**

           - A buffering mechanism causes a route to be flooded with stale commands that result in the brakes responding to a historical command

               - **REQUIREMENT REQ-6: Any brake actuator buffers should routinely purge data on a FIFO basis**


#### CA-6.4: Apollo provides the braking command at the correct time to ensure vehicle safety

**True statement from the CA context: The braking command is issued prompty, but braking is applied too late**

Type 3 scenario:

   -  Apollo sends the braking command correctly, but the command is received too late by the actuator

       - Improper Execution: Transmission medium error causes the command to be received too late

       - How this could occur given the true statement above:

           - A primary command pathway suffers an intermittent fault; oscillation of the in-service transmitters and pathways delays command reception

               - **REQUIREMENT REQ-31: A primary command pathway should not automatically activate on restoration if the secondary has not failed and the routes are otherwise identical**

           - A primary command pathway has failed; the secondary pathway has an incorrectly parameterised capacity / baud rate, delaying command reception

               - **REQUIREMENT REQ-12: All transmission media should be polled or tested automatically, including secondary routes**

           - Transmission medium fault causes intermittent data loss that slows down overall performance below the required specification

               - **REQUIREMENT REQ-32: A transmission media that has degraded to the point where it impacts safety must be considered failed**


       - Improper Execution: The command is received too slowly due to a data / signal collision or overflow

       - How this could occur given the true statement above:

           - A buffering mechanism, combined with a temporary route loss, causes a route to be flooded with stale commands

               - **REQUIREMENT REQ-14: Buffered transmission must be accomplanied by a buffer purge when the route fails for longer > than TBD seconds**

           - The use of persistent send / send upon analogue change causes a rate of transmission that overloads the transmission medium

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - The use of excessive bandwidth by other systems on a shared transmission medium overloads the transmission medium

               - **REQUIREMENT REQ-17: Critical systems should take priority over non-critical systems when using the transmission media**


Type 3 scenario:

   -  Apollo sends the braking command correctly, but the command is applied too late by the actuator

       - Improper Execution: The actuator responds too slowly due to data / buffer overload in the actuator

       - How this could occur given the true statement above:

           - The actuator continues to process / discard now out-of-date commands, the buffered command is not reached in time

               - **REQUIREMENT REQ-5: The brake command transmission rate should not exceed the rate at which the brake actuators can process commands**


               - **REQUIREMENT REQ-6: Any brake actuator buffers should routinely purge data on a FIFO basis**


       - Improper execution: The actuator responds too slowly due to a power system under voltage

       - How this could occur given the true statement above:

           - Battery / alternator system failure

               - **REQUIREMENT REQ-2: The battery / alternator power system must be designed and tested to be operationally**

           - Mechanical damage to the power supply route

               - **REQUIREMENT REQ-3: The power supply route to the brake actuators must be redundant if practicable**


       - Improper execution: The actuator responds too slowly due to a mechanical fault

       - How this could occur given the true statement above:

           - A mechanical fault causes the physical part of the actuator to respond too slowly

               - **REQUIREMENT REQ-1: Physical brake actuators must be designed must be designed and tested to be operationally reliable**


#### CA-6.5: Apollo provides the braking command for the correct duration in order to ensure vehicle safety

**True statement from the CA context: The application of braking is ended too quickly**

Type 3 scenario:

   -  Apollo applies the brake command for the correct duration, but the actuator stops too early

       - Improper Execution: The actuator does not respond due to data / buffer overload in the actuator

       - How this could occur given the true statement above:

           - A buffer overflow in the actuator triggers a command purge that results in the command ending too soon

               - **REQUIREMENT REQ-6: Any brake actuator buffers should routinely purge data on a FIFO basis**


       - Improper execution: The actuator has failed and cannot sustain braking

       - How this could occur given the true statement above:

           - A mechanical fault causes the brakes to release too soon

               - **REQUIREMENT REQ-1: Physical brake actuators must be designed must be designed and tested to be operationally reliable**


**True statement from the CA context: The application of braking goes on too long**

Type 3 scenario:

   -  Apollo applies the brake command for the correct duration, but the actuator releases the brakes too late

       - Improper Execution: The actuator does not respond due to data / buffer overload in the actuator

       - How this could occur given the true statement above:

           - Queued commands in the actuator continue to be executed beyond the required duration of the command

               - **REQUIREMENT REQ-5: The brake command transmission rate should not exceed the rate at which the brake actuators can process commands**


               - **REQUIREMENT REQ-6: Any brake actuator buffers should routinely purge data on a FIFO basis**


       - Improper execution: The actuator has failed releases braking too slowly

       - How this could occur given the true statement above:

           - A mechanical fault causes the physical part of the brake actuator to sieze

               - **REQUIREMENT REQ-1: Physical brake actuators must be designed must be designed and tested to be operationally reliable**


#### UCA-6.1: Apollo does not provide the brake control action when relative velocity and distance to an obstacle mean that a collision is imminent.[H-2] [H-3] [H-4]

**True statement from UCA context: The vehicle is approaching an obstacle with a velocity and acceleration vector that indicate a collision**

Belief:

*Apollo incorrectly believes that the relative velocity is lower than in reality*

Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: The feedback received has a conflict

       - How this could occur given the true statement above:

           - Apollo was presented with accurate data from at least one sensor, but it was discarded, distorted or overwritten due to an incorrect priority scheme or process model conflict

               - **REQUIREMENT REQ-33: Priority schemes must be designed with voting systems, consistency checks  and redundancy, rather than crude averages or simple hierarchies**


Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the relative velocity

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


Belief:

*Apollo incorrectly believes that the relative distance is higher than in reality*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the relative distance

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: The feedback received has a conflict

       - How this could occur given the true statement above:

           - Apollo was presented with accurate data from at least one sensor, but it was discarded, distorted or overwritten due to an incorrect priority scheme or process model conflict

               - **REQUIREMENT REQ-33: Priority schemes must be designed with voting systems, consistency checks  and redundancy, rather than crude averages or simple hierarchies**


Belief:

*Apollo incorrectly believes that the obstacle will clear the vehicle’s path*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: Feedback indicates that the obstacle and vehicle will not cross paths

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**


Belief:

*Apollo incorrectly believes that there is no obstacle in its path*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to determine that there is an obstacle in the vehicles path

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - Optical systems are offline, reporting stale data, or transmission is delayed

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**

           - An 'obstacle' such as a human being enters the field of view, but collapses to the floor, outside of the field of view of the sensors

               - **REQUIREMENT REQ-44: Apollo and its sensors must be capable of detecting fallen pedestrians in order to prevent fatality**


**True statement from UCA context: The vehicle is approaching an obstacle with a velocity and acceleration vector that indicate a collision will occur given *adverse weather or environmental conditions***

Belief:

*Apollo incorrectly identifies or ignores adverse weather / environmental conditions*

Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: Feedback is sufficient to determine the current weather / environmental conditions

       - How this could occur given the true statement above:

           - The sensors present images / points / data with sufficient clarity to deduce the conditions, but the the algorithm is not equipped to look for black ice, leaves, water, unforeseen spillages or environmental debris

               - **REQUIREMENT REQ-36: Apollo must be able to deduce and account for all reasonabely probable sustances that could affect vehicle traction such as black ice, standing water, oil / chemical  spills, and excessive mud, dust or rotting leaves**


Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the current weather / environmental conditions

       - How this could occur given the true statement above:

           - Sensors are not calibrated to distinguish snow, ice, 'black' ice, standing water, chemical spills, oils spills, slippery mud left by farm vehicles, soggy leaves or other commonly occuring substances

               - **REQUIREMENT REQ-37: Sensors must be calibrated to detect all reasonabely probable sustances that could affect vehicle traction such as black ice, standing water, oil / chemical  spills, and excessive mud, dust or rotting leaves**


#### UCA-6.2: Apollo does not provide brake control when in autonomous mode and vehicle speed exceeds limits (limits for controllability, stability, upcoming manoeuvre, speed limit, traffic flow limit, planned test limit, etc.)[H-1] [H-2] [H-3] [H-4] [H-6]

**True statement from UCA context: Vehicle is rapidly approaching / traversing a corner or bend in the road at excessive speed**

Belief:

*Apollo incorrectly believes that the vehicle is in a different location*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received does not indicate a vehicle location corresponding to a road-path manoeuvre

       - How this could occur given the true statement above:

           - GPS / GNSS / IMU sensors are offline, reporting stale data, or data transmission is delayed

               - **REQUIREMENT REQ-38: The overall geolocation system must be robust enough to cope with momentary communication losses, and have some form of backup**

           - Optical systems are offline, reporting stale data, or transmission is delayed

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


Belief:

*Apollo incorrectly believes that the road path curvature radius is higher than in reality*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Infromation received: The feedback received is insufficient to determine the road curvature radius

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: The feedback received is sufficient to determine the road curvature radius

       - How this could occur given the true statement above:

           - Apollo was presented with accurate data from at least one sensor, but it was discarded, distorted or overwritten due to an incorrect priority scheme or process model conflict

               - **REQUIREMENT REQ-33: Priority schemes must be designed with voting systems, consistency checks  and redundancy, rather than crude averages or simple hierarchies**

           - The mathematical calculations inside Apollo fail to process the data correctly

               - **REQUIREMENT REQ-39: Apollo must be able to resolve complex 3D structures from the sensor data with which it is provided**

           - The Apollo algorithm does not attempt to calculate road curvature within its process model, relying on other data, such as map position, deducing an incorrect curvature due to inaccurate positioning or an out-of-date map

               - **REQUIREMENT REQ-40: Apollo and its sensors must be capable of determining the correct right of way, including route curvature, from sensors alone**


Belief:

*Apollo incorrectly believes that the vehicle speed is lower than in reality*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the determine the vehicle velocity

       - How this could occur given the true statement above:

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - Vehicle speed sensors suffer an internal failure

               - **REQUIREMENT REQ-41: The vehicle speed sensors are critical and must be redundant and designed and test for operational reliability**

           - GPS / GNSS / IMU sensors are offline, reporting stale data, or data transmission is delayed

               - **REQUIREMENT REQ-39: Apollo must be able to resolve complex 3D structures from the sensor data with which it is provided**


**Vehicle is approaching or traversing a corner or bend in the road at standard speed when adverse weather or environmental conditions render this speed excessive**

Belief:

*Apollo incorrectly identifies or ignores adverse weather / environmental conditions*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the current weather / environmental conditions

       - How this could occur given the true statement above:

           - Sensors are not calibrated to distinguish snow, ice, 'black' ice, standing water, chemical spills, oils spills, slippery mud left by farm vehicles, soggy leaves or other commonly occuring substances

               - **REQUIREMENT REQ-37: Sensors must be calibrated to detect all reasonabely probable sustances that could affect vehicle traction such as black ice, standing water, oil / chemical  spills, and excessive mud, dust or rotting leaves**


Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: Feedback is sufficient to determine the current weather / environmental conditions

       - How this could occur given the true statement above:

           - The sensors present images / points / data with sufficient clarity to deduce the conditions, but the the algorithm is not equipped to look for black ice, leaves, water, unforeseen spillages or environmental debris

               - **REQUIREMENT REQ-36: Apollo must be able to deduce and account for all reasonabely probable sustances that could affect vehicle traction such as black ice, standing water, oil / chemical  spills, and excessive mud, dust or rotting leaves**


#### UCA-6.3: Apollo does not provide brake control when in autonomous mode, the vehicle is stationary, and vehicle path is not clear[H-2] [H-3] [H-4]

**True statement from UCA context: Apollo is parked at a traffic lights at red but does not apply brakes as required by driving code *(human driver would be required to apply the handbrake)***

Belief:

*Apollo incorrectly believes the 'lights' are at green*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to determine that the traffic lights are at red

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - Optical systems are offline, reporting stale data, or transmission is delayed

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**

           - There is more than one traffic light in the field of view, leading to a conflict between one or more sensors

               - **REQUIREMENT REQ-42: Sensors must be capable of distinguishing the traffic lights applicable to the to the selected right of way from many potential candidates**

           - The 'lights' are not lights at all, but a workman holding a 'STOP / GO' sign

               - **REQUIREMENT REQ-43: Apollo and it sensors must be capable of resolving temporary traffic lights, including signs held by workmen, independently of map data**


Belief:

*Apollo incorrectly believes that there is no obstacle in its path*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to determine that there is an obstacle in the vehicles path

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - Optical systems are offline, reporting stale data, or transmission is delayed

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**

           - An 'obstacle' such as a human being enters the field of view, but collapses to the floor, outside of the field of view of the sensors

               - **REQUIREMENT REQ-44: Apollo and its sensors must be capable of detecting fallen pedestrians in order to prevent fatality**


Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Apollo processes data received too slowly, such that the data processed already reflects an earlier physical scenario that is now inappropriate

       - How this could occur given the true statement above:

           - Inadequate hardware specifications

               - **REQUIREMENT REQ-45: Apollo must have hardware capable of processing all data received in real time, with contingency to account for unexpected data bursts, and a real time operating system**

           - A burst of activity causes Apollo to suffer a data overload

               - **REQUIREMENT REQ-45: Apollo must have hardware capable of processing all data received in real time, with contingency to account for unexpected data bursts, and a real time operating system**


       - Incorrect reconciliation of optical and other range-finding techniques causes incorrect obstacle tracking

       - How this could occur given the true statement above:

           - Incorrect time stamping of data leads to a framing conflict

               - **REQUIREMENT REQ-46: All data received must correctly assembled into the relevant frame**

           - Obstacles are incorrectly identified and so cannot be tracked effectively

               - **REQUIREMENT REQ-47: Apollo must be capable of tracking all reasonablely likely obstacles, from lamp posts and trash cans to people, pets, and cattle**


#### UCA-6.4: Apollo does not provide brake control when in autonomous mode and the vehicle has reached the final destination[H-7]

**True statement from UCA context: The vehicle has reached the route destination**

Belief:

*Apollo mistakenly believes that it is in a different location than in reality*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to determine the vehicle location

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - GPS / GNSS / IMU sensors are offline, reporting stale data, or data transmission is delayed

               - **REQUIREMENT REQ-38: The overall geolocation system must be robust enough to cope with momentary communication losses, and have some form of backup**


Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Apollo does not apply the brake

       - How this could occur given the true statement above:

           - The controller algorithm identifies the end of the journey, but is not programmed to provide the brake at the end of the the journey

               - **REQUIREMENT REQ-48: Apollo must be programmed to stop in a safe location and apply the parking brake at the end of the journey**

           - The controller receives adequate feedback but does not correctly identify the end of the journey

               - **REQUIREMENT REQ-49: Apollo must be capable of identifying the journey's end, and able to identify a safe stopping location**


#### UCA-6.6: Apollo does not provide brake control when in autonomous mode and collision occurs[H-1] [H-2] [H-3] [H-4] [H-5]

**True statement from UCA context: The vehicle has suffered a collision and must stop (if only to comply with highway regulation)**

Belief:

*Apollo incorrectly believes that no collision has taken place*

Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: The vehicle sensors report a collision or critical vehicle damage state

       - How this could occur given the true statement above:

           - No collision contingency exists i.e. the vehicle is not programmed to brake, then engage neutral followed by the parking brake (standard emergency stop procedure in the UK)

               - **REQUIREMENT REQ-52: Apollo must bring the vehicle to rest and apply the parking brake after a collision**

           - Failure to stop after a collision is an offence in most countries; this is not accounted for and the vehicle attempts to move off

               - **REQUIREMENT REQ-53: Apollo must not move off after a collision, unless instructed to do so by the human occupants**


Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to determine that a crash has taken place

       - How this could occur given the true statement above:

           - The collision itself has compromised the sensors that were designed to detect the collision

               - **REQUIREMENT REQ-50: Apollo's collision sensors must still be capable of reporting a collision even when extensive damage to the vehicle has taken place**

           - The collision has managed to happen in a manner which is not detected by the sensors, but still represents a critical failure, could include: a broken windscreen, an item impaling the engine or passenger compartment, bumper or exhaust hanging off (in the case of a rear collision)

               - **REQUIREMENT REQ-51: Apollo must be capable of detecting less severe collisions that do not immediately threaten life but require immediate attention, such as a broken windscreen, loose exhaust, etc**


Type 2 scenario:

   -  Necessary controller / feedback information does not exist

       - Specific collision sensors have not been built into the vehicle design


       - Collision sensors exist, but have not been routed through the appropriate data interfaces


#### UCA-6.7: Apollo provides brake command with insufficient amount of braking below the minimum amount needed to avert a forward collision[H-2] [H-3] [H-4]

**True statement from UCA context: The vehicle is approaching an obstacle with a velocity and acceleration vector such that the vehicle will not be brought to rest in time to avert a collision**

Belief:

*Apollo incorrectly believes that the relative velocity is lower than in reality*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the relative distance

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: The feedback received has a conflict

       - How this could occur given the true statement above:

           - Apollo was presented with accurate data from at least one sensor, but it was discarded, distorted or overwritten due to an incorrect priority scheme or process model conflict

               - **REQUIREMENT REQ-33: Priority schemes must be designed with voting systems, consistency checks  and redundancy, rather than crude averages or simple hierarchies**


Belief:

*Apollo incorrectly believes that the relative distance is higher than in reality*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the relative distance

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


       - Information received: the current data reflects a time when the distance to the obstacle was greater

       - How this could occur given the true statement above:

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - The data from the sensors is delayed at source due to poor sensor performance

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**

           - The data is delayed entering into the Apollo software due to a data bottleneck in the hardware platform

               - **REQUIREMENT REQ-54: Apollo hardware must be capable of receiving and processing the maximum data throughput of all its data buses**


Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: The feedback received has a conflict

       - How this could occur given the true statement above:

           - Apollo was presented with accurate data from at least one sensor, but it was discarded, distorted or overwritten due to an incorrect priority scheme or process model conflict

               - **REQUIREMENT REQ-33: Priority schemes must be designed with voting systems, consistency checks  and redundancy, rather than crude averages or simple hierarchies**


Belief:

*Apollo incorrectly believes that the deceleration needed is lower than in reality*

Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: All the necessary feedback to calculate the relevant trajectories was received

       - How this could occur given the true statement above:

           - The control algorithm does not adapt sufficiently quickly to calculate the obstacle dynamics, where an obstacle decelerates rapidly, so that the braking amount is underestimated

               - **REQUIREMENT REQ-45: Apollo must have hardware capable of processing all data received in real time, with contingency to account for unexpected data bursts, and a real time operating system**


Belief:

*Apollo incorrectly believes that it is applying an amount of deceleration different to reality*

Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Apollo algorithm brake percentage is not correctly calibrated for the vehicle, and does not adapt heuristically as a human would


       - Vehicle mass is much higher than normal due to heavy loading, which is not accounted for in the algorithm


       - A mechanical failure causes incorrect braking but the algorithm does not account for this by increasing the braking amount


Belief:

*Apollo incorrectly believes that the obstacle will clear the vehicle’s path*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: Feedback indicates that the obstacle and vehicle will not cross paths

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: All the necessary feedback to calculate the relevant trajectories was received

       - How this could occur given the true statement above:

           - Some lag in processing coupled with a sudden change in direction of the obstacle lead to insufficient braking being calculated

               - **REQUIREMENT REQ-45: Apollo must have hardware capable of processing all data received in real time, with contingency to account for unexpected data bursts, and a real time operating system**


               - **REQUIREMENT REQ-47: Apollo must be capable of tracking all reasonablely likely obstacles, from lamp posts and trash cans to people, pets, and cattle**


**True statement from UCA context: The vehicle is approaching an obstacle with a velocity and acceleration vector such that the vehicle will not be brought to rest in time to avert a collision *in adverse weather conditions***

Belief:

*Apollo incorrectly identifies adverse weather / road conditions, and therefore incorrectly believes that it is applying an amount of deceleration different to reality*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the current weather / environmental conditions

       - How this could occur given the true statement above:

           - Sensors are not calibrated to distinguish snow, ice, 'black' ice, standing water, chemical spills, oils spills, slippery mud left by farm vehicles, soggy leaves or other commonly occuring substances

               - **REQUIREMENT REQ-37: Sensors must be calibrated to detect all reasonabely probable sustances that could affect vehicle traction such as black ice, standing water, oil / chemical  spills, and excessive mud, dust or rotting leaves**


Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Control model does not account for adverse weather conditions when determining the amount of braking to apply, and does not heuristically account for the deficit


               - **REQUIREMENT REQ-36: Apollo must be able to deduce and account for all reasonabely probable sustances that could affect vehicle traction such as black ice, standing water, oil / chemical  spills, and excessive mud, dust or rotting leaves**


#### UCA-6.8: Apollo provides brake command when autonomous driving is not active (off, standby, overridden, or e-stop)[H-3] [H-4] [H-5] [H-6]

**True statement from UCA context: The vehicle is moving and the human driver takes control, but Apollo continues to brake**

Belief:

*Apollo incorrectly believes that autonomous mode is (should be) active*

Type 2 scenario:

   -  Necessary controller / feedback information does not exist

       - Information received: vehicle overrides were external to Apollo – Apollo is unaware of override conditions

       - How this could occur given the true statement above:

           - The human driver has overridden control on one or more control paths, but this does not include the brakes and so braking commands are still sent

               - **REQUIREMENT REQ-55: Apollo must be made aware of channel overrides and be able to account for them**

           - After an emergency override of all controls, no feedback is presented to Apollo, such that when the mode is disengaged Apollo will issue controls without autonomous mode being reactivated

               - **REQUIREMENT REQ-56: A total DataSpeed e-stop should be fed back to Apollo and Apollo should disengage automatic mode**


#### UCA-6.9: Apollo provides brake control when vehicle speed does not exceed limits (speed limit, traffic flow limit, manoeuvre limit, planned test limit, etc.), there is no obstacle, no faults, destination is reachable, and vehicle has not reached destination[H-4]

**True statement from UCA context: there is no need to apply the brakes – no obstacles, the speed limit has not changed, and the vehicle is not going down hill**

Belief:

*Apollo incorrectly believes that an obstacle is present in the roadway*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback is a sensor ghost, corresponding to a forward obstacle

       - How this could occur given the true statement above:

           - A sensor error is causing a ‘ghost’ object to appear, where delayed or cached feedback is sent to Apollo describing an object that is no longer there

               - **REQUIREMENT REQ-57: Sensors should purge buffered data after TBD ms in order to prevent sensor ghosting**


Belief:

*Apollo incorrectly believes that it has entered a new speed limit zone*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to determine the vehicle location

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - GPS / GNSS / IMU sensors are offline, reporting stale data, or data transmission is delayed

               - **REQUIREMENT REQ-38: The overall geolocation system must be robust enough to cope with momentary communication losses, and have some form of backup**

           - The position data is correct but the map (containing speed zone information) itself is incorrect

               - **REQUIREMENT REQ-58: Apollo must have regular access to map updates so that detailed information is up-to-date**


       - Information received: The feedback is insufficient to accurately identify and read a speed limit display or sign

       - How this could occur given the true statement above:

           - Sensors lack the finesse to correct identify signage, resulting in a misread speed limit sign, or some other signage as a speed limit

               - **REQUIREMENT REQ-59: Apollo and its sensor must be capable of identifying and reading speed limit signs, variable speed limit signs and advisories**


Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Apollo systems misread some object as a speed limit sign


       - Apollo systems misread a valid speed limit


Belief:

*Apollo incorrectly believes that the vehicle is going down hill*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received corresponds to some rate of change of altitude

       - How this could occur given the true statement above:

           - Barometric / IMU / pitch sensors present information corresponding to descent which is incorrect

               - **REQUIREMENT REQ-60: Apollo sensors must be capable of detecting a rate of change of altitude**


**True statement from UCA context: there is no need to apply the brakes – the speed limit zone has changed, but the speed restriction does not apply at the current time (for example, a school zone on a Saturday)**

Belief:

*Apollo incorrectly believes that it has entered a new speed limit zone, but the time restrictions do not apply*

Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: The speed limit sign or limit boundary is resolvable in the feedback

       - How this could occur given the true statement above:

           - The system time is incorrect

               - **REQUIREMENT REQ-61: The vehicle on-board time master clock must be routinely and accurately synchronised to UTC**

           - Apollo slows down for e.g. a school zone outside of the school’s operating hours, because the algorithm does not account for the time dependency of speed limit zones

               - **REQUIREMENT REQ-62: Apollo algorithm must take account of time-dependent access and speed limits, for example school zones and bus lanes**


#### UCA-6.10: UCA-6.10: Apollo provides brake control when driver is providing throttle[H-4] [H-5] [H-6]

**True statement from UCA context: The human driver feels it best to accelerate e.g. for safety reasons**

Belief:

*Apollo incorrectly believes that it is safe to apply the brakes while the driver is accelerating*

Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: Apollo receives feedback of the human intervention

       - How this could occur given the true statement above:

           - Apollo disregards human actions and applies the brakes anyway

               - **REQUIREMENT REQ-63: Apollo must detect a human application of throttle and not apply the brakes**


Type 2 scenario:

   -  Necessary controller / feedback information does not exist

       - The feedback that a manual acceleration is taking place is not passed to Apollo

       - How this could occur given the true statement above:

           - Apollo continues to drive in automatic mode - throttle commands from the human are not affected by brake commands from Apollo

               - **REQUIREMENT REQ-63: Apollo must detect a human application of throttle and not apply the brakes**


#### UCA-6.11: Apollo provides excessive brake command when wheel lock has occurred and lateral control is needed  (rationale: ABS may not work below 5mph or other situations)[H-1] [H-2] [H-4] [H-6]

**True statement from UCA context: Apollo is applying brakes to slow down, in the context of an ABS failure to activate while the wheels are slipping**

Belief:

*Apollo incorrectly believes applying maximum brake will lead to the quickest deceleration*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: Apollo receives feedback that ABS is healthy

       - How this could occur given the true statement above:

           - The ABS actuator unit is supplying incorrect feedback

               - **REQUIREMENT REQ-64: The ABS unit should be monitored via robust means such as an externally wetted life contact, and the feedback supplied to Apollo**

           - The ABS actuator has failed but its state is not monitored in the feedback chain

               - **REQUIREMENT REQ-64: The ABS unit should be monitored via robust means such as an externally wetted life contact, and the feedback supplied to Apollo**


Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: The feedback is received that ABS has failed, but does not take this into account

       - How this could occur given the true statement above:

           - The algorithm does not account for ABS failure in its brake calculations

               - **REQUIREMENT REQ-65: Apollo must account for ABS availability when deciding braking level**


#### UCA-6.12: Apollo provides brake command with insufficient amount of braking to reduce vehicle speed within limits (limits for controllability, stability, upcoming manoeuvre, speed limit, traffic flow limit, planned test limit, etc.)[H-1] [H-2] [H-3] [H-4] [H-6]

**True statement from UCA context: Vehicle is rapidly approaching / traversing a corner or bend in the road at excessive speed**

Belief:

*Apollo incorrectly believes that the vehicle is in a different location*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received indicates a greater distance to the path manoeuvre than in reality

       - How this could occur given the true statement above:

           - GPS / GNSS / IMU sensors are offline, reporting stale data, or data transmission is delayed

               - **REQUIREMENT REQ-38: The overall geolocation system must be robust enough to cope with momentary communication losses, and have some form of backup**

           - Optical systems are offline, reporting stale data, or transmission is delayed

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


Belief:

*Apollo incorrectly believes that the road path curvature radius is higher than in reality*

Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: The feedback received is sufficient to determine the road curvature radius

       - How this could occur given the true statement above:

           - Apollo was presented with accurate data from at least one sensor, but it was discarded, distorted or overwritten due to an incorrect priority scheme or process model conflict

               - **REQUIREMENT REQ-33: Priority schemes must be designed with voting systems, consistency checks  and redundancy, rather than crude averages or simple hierarchies**

           - The mathematical calculations inside Apollo fail to process the data correctly

               - **REQUIREMENT REQ-39: Apollo must be able to resolve complex 3D structures from the sensor data with which it is provided**

           - The Apollo algorithm does not attempt to calculate road curvature within its process model, relying on other data, such as map position, deducing an incorrect curvature due to inaccurate positioning or an out-of-date map

               - **REQUIREMENT REQ-40: Apollo and its sensors must be capable of determining the correct right of way, including route curvature, from sensors alone**


Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Infromation received: The feedback received is insufficient to determine the road curvature radius

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**

           - The physical route has been revised, but the HD map was not updated due to a communications failure

               - **REQUIREMENT REQ-58: Apollo must have regular access to map updates so that detailed information is up-to-date**

           - The physical route has been revised, but the HD map was not updated due to a technician error

               - **REQUIREMENT REQ-66: Apollo's map source must be updates as soon as practicable when map data changes**


Belief:

*Apollo incorrectly believes that the vehicle speed is lower than in reality*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the determine the vehicle velocity

       - How this could occur given the true statement above:

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - Vehicle speed sensors suffer an internal failure

               - **REQUIREMENT REQ-41: The vehicle speed sensors are critical and must be redundant and designed and test for operational reliability**

           - GPS / GNSS / IMU sensors are offline, reporting stale data, or data transmission is delayed

               - **REQUIREMENT REQ-38: The overall geolocation system must be robust enough to cope with momentary communication losses, and have some form of backup**


Belief:

*Apollo incorrectly believes that the path manoeuvre itself is required in a different location than in reality*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: Apollo receives feedback or information corresponding to an incorrect manoeuvre location

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**

           - The position data received is correct, but out-of-date map data indicates the manoeuvre in an incorrect location because the road layout or right-of-way has changed

               - **REQUIREMENT REQ-40: Apollo and its sensors must be capable of determining the correct right of way, including route curvature, from sensors alone**

           - Temporary roadworks / path diversions are not marked on the HD map such that Apollo will not slow down for, or avoid, a static obstacle until it is physically detected

               - **REQUIREMENT REQ-67: Apollo and its sensor must be capable of identying roadworks, police cordons, traffic accident scenes and following route markers such as cordons and lines of cones**


Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Algorithm flaw: Apollo has not been programmed or calibrated to respond to changes in the right-of-way, or temporary road layouts


**Vehicle is approaching or traversing a corner or bend in the road at standard speed when adverse weather or environmental conditions render this speed excessive**

Belief:

*Apollo incorrectly identifies or ignores adverse weather / environmental conditions - and believes that it is applying an amout of deceleration lower than in reality*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the current weather / environmental conditions

       - How this could occur given the true statement above:

           - Sensors are not calibrated to distinguish snow, ice, 'black' ice, standing water, chemical spills, oils spills, slippery mud left by farm vehicles, soggy leaves or other commonly occuring substances

               - **REQUIREMENT REQ-37: Sensors must be calibrated to detect all reasonabely probable sustances that could affect vehicle traction such as black ice, standing water, oil / chemical  spills, and excessive mud, dust or rotting leaves**


Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: Feedback is sufficient to determine the current weather / environmental conditions

       - How this could occur given the true statement above:

           - Control model does not account for adverse weather conditions when determining the amount of braking to apply, and does not heuristically account for the deficit

               - **REQUIREMENT REQ-36: Apollo must be able to deduce and account for all reasonabely probable sustances that could affect vehicle traction such as black ice, standing water, oil / chemical  spills, and excessive mud, dust or rotting leaves**


Belief:

*Apollo incorrectly believes that the safe manoeuvre speed is higher than in reality because it has failed to identify adverse weather / road conditions*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the current weather / environmental conditions

       - How this could occur given the true statement above:

           - Sensors are not calibrated to distinguish snow, ice, 'black' ice, standing water, chemical spills, oils spills, slippery mud left by farm vehicles, soggy leaves or other commonly occuring substances

               - **REQUIREMENT REQ-37: Sensors must be calibrated to detect all reasonabely probable sustances that could affect vehicle traction such as black ice, standing water, oil / chemical  spills, and excessive mud, dust or rotting leaves**


Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: Feedback is sufficient to determine the current weather / environmental conditions

       - How this could occur given the true statement above:

           - Control model does not account for adverse weather conditions of the prevailing type when determining the safe speed limit for the upcoming manoeuvre

               - **REQUIREMENT REQ-68: Apollo must account for environmental conditions of the prevailing type when calculation the safe speed for manoeuvres**


**True statement from UCA context: The vehicle suffers a momentary instability which requires the reduction in the braking amount that is then rectified**

Belief:

*Apollo incorrectly believes that the vehicle is in a unstable state when it is not*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback is insufficient to determine that the vehicle is / has become stable

       - How this could occur given the true statement above:

           - Feedback from stability sensors lead to the brakes being released, but these were ‘locked’ in state leading to Apollo continuing to refrain from braking when it would now be safer to do so

               - **REQUIREMENT REQ-69: Vehicle stability must not be processed as a 'latched' condition**

           - The stability sensors have failed leading to stale or inaccurate feedback

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information recevied: The feedback is sufficient to determine that the vehicle is stable

       - How this could occur given the true statement above:

           - Apollo incorrectly amalgamates sensor data leading it to believe that the vehicle has become unstable

               - **REQUIREMENT REQ-70: Apollo must correctly derive the vehicle stability condition from the available sensors**


#### UCA-6.13: UCA-6.13: Apollo provides a brake command that is excessive beyond the physical limit of the passengers

**True statement from UCA context: Apollo causes the vehicle to decelerate rapidly enough to cause physical injury to the occupants, when it is unnecessary in the context of averting a worse collision**

Belief:

*Apollo believes it is applying normal braking*

Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: after applying brakes, unexpected high brake level is applied - feedback is received that is sufficient to determine that the level of braking is excessive

       - How this could occur given the true statement above:

           - Apollo fails to take into account feedback from inertial / velocity sensors, and to reduce the level of braking

               - **REQUIREMENT REQ-71: When braking Apollo must heuristically adapt the level of braking if the deceleration is too slow, or too rapid**


Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Algorithm flaw: Apollo is incorrectly calibrated such that applying brakes normally results in excessive braking


               - **REQUIREMENT REQ-73: Apollo must be accurately calibrated for the braking system**


Belief:

*Apollo incorrectly believes that a collision far worse is about to take place, full brakes are applied*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: Feedback corresponding to a collision is received

       - How this could occur given the true statement above:

           - Near miss collision data is interpreted as a collision due to slight time stamp errors, meaning that a moving vehicle in front is interpreted as static

               - **REQUIREMENT REQ-46: All data received must correctly assembled into the relevant frame**


Type 2 scenario:

   -  Apollo does not receive feedback / information when needed

       - Information received: Information corresponding to an obstacle is received late, requiring that the vehicle brake much more severely than would have been required had the information been received promptly

       - How this could occur given the true statement above:

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


**True statement from UCA context: The vehicle is in a location where stopping is never appropriate when the path is open, such as a motorway / highway, when another vehicle has unavoidably stopped due to a brake down**

Belief:

*Apollo incorrectly believes that the vehicle in front has stopped due to traffic congestion*

Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Bulk traffic tracking fails: The vehicle pulls up behind a broken down vehicle rather than evading it, exacerbating the dangerous traffic build up


               - **REQUIREMENT REQ-72: Apollo must be capable of distinguishing broken down vehicles from queuing traffic**


**True statement from UCA context: The vehicle is in a location where stopping is never appropriate when the path is open, such as a motorway / highway**

Belief:

*Apollo incorrectly believes that there is an obstacle configuration that constitutes slow or stationary traffic ahead*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Feedback received: Apollo receives feedback corresponding to a stationary / rapidly decelerating traffic ahead, in the bulk of the road

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**


#### UCA-6.14: Apollo provides brake control too late (TBD sec) after relative velocity and distance to an obstacle mean that a collision is imminent[H-2] [H-3] [H-4]

**True statement from UCA context: An opportunity to brake in order to avoid a collision with an obstacle is being missed**

Belief:

*Apollo incorrectly believes that there is no present need to brake*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: is insufficient to accurately determine the correct time to brake

       - How this could occur given the true statement above:

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Algorithm flaw: Apollo processes data received too slowly, such that the data processed already reflects an earlier physical scenario that is now inappropriate

       - How this could occur given the true statement above:

           - Apollo has insufficient processor resources to process the data

               - **REQUIREMENT REQ-45: Apollo must have hardware capable of processing all data received in real time, with contingency to account for unexpected data bursts, and a real time operating system**

           - Apollo processor resources are unavailable

               - **REQUIREMENT REQ-45: Apollo must have hardware capable of processing all data received in real time, with contingency to account for unexpected data bursts, and a real time operating system**

           - Apollo software performance degrades over time due to a programming fault

               - **REQUIREMENT REQ-74: Where Apollo is required to access historic data, it must be ensured that e.g. the data is compatmentalized to avoid linearly growing seek times**


       - Algorithm flaw: Apollo fails to track a vehicle travelling at a relatively slow speed

       - How this could occur given the true statement above:

           - The vehicle is temporarily obscured by a faster moving vehicle pulling in front of it, since visual contact is lost Apollo fails to slow down

               - **REQUIREMENT REQ-75: Apollo must be able to temporarily track objects that are momentarily out of view**


Type 2 scenario:

   -  Apollo does not receive feedback / information when needed

       - Information received: Apollo receives feedback of an upcoming obstacle too late

       - How this could occur given the true statement above:

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


#### UCA-6.15: Apollo provides braking control too late (> tbd seconds) prior to manoeuvre[H-1] [H-2] [H-3] [H-4] [H-6]

**True statement from UCA context: An opportunity to brake in order to avoid a collision with an obstacle is being missed**

Belief:

*Apollo incorrectly believes that there is no present need to brake*

Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Algorithm flaw: Apollo processes data received too slowly, such that the data processed already reflects an earlier physical scenario that is now inappropriate

       - How this could occur given the true statement above:

           - Apollo has insufficient processor resources to process the data

               - **REQUIREMENT REQ-45: Apollo must have hardware capable of processing all data received in real time, with contingency to account for unexpected data bursts, and a real time operating system**

           - Apollo processor resources are unavailable

               - **REQUIREMENT REQ-45: Apollo must have hardware capable of processing all data received in real time, with contingency to account for unexpected data bursts, and a real time operating system**

           - Apollo software performance degrades over time due to a programming fault

               - **REQUIREMENT REQ-74: Where Apollo is required to access historic data, it must be ensured that e.g. the data is compatmentalized to avoid linearly growing seek times**


Type 2 scenario:

   -  Apollo does not receive feedback / information when needed

       - Information received: Apollo receives feedback about an obstacle too late

       - How this could occur given the true statement above:

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


#### UCA-6.16: Apollo provides brake control too late before (< TBD sec before) limits are exceeded (limits for upcoming manoeuvre, controllability, stability, speed limit, traffic flow limit, planned test limit, etc.)[H-2] [H-3] [H-4] [H-6]

**True statement from UCA context: The vehicle is passing through the point where gentle braking will suffice, such that the vehicle has not begun to brake and more severe braking or stability compromise will ensue**

Belief:

*Apollo incorrectly believes that there is no present need to brake*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: is insufficient to accurately determine the correct time to brake

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Algorithm flaw: Apollo processes data received too slowly, such that the data processed already reflects an earlier physical scenario that is now inappropriate

       - How this could occur given the true statement above:

           - Apollo has insufficient processor resources to process the data

               - **REQUIREMENT REQ-45: Apollo must have hardware capable of processing all data received in real time, with contingency to account for unexpected data bursts, and a real time operating system**

           - Apollo processor resources are unavailable

               - **REQUIREMENT REQ-45: Apollo must have hardware capable of processing all data received in real time, with contingency to account for unexpected data bursts, and a real time operating system**

           - Apollo software performance degrades over time due to a programming fault

               - **REQUIREMENT REQ-74: Where Apollo is required to access historic data, it must be ensured that e.g. the data is compatmentalized to avoid linearly growing seek times**


Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Algorithm flaw: The control algorithm does not account for vehicle stability prior to arriving at the apex, treating the curve as a discrete point rather than a contiguous path


Type 2 scenario:

   -  Apollo does not receive feedback / information when needed

       - Information received: Apollo receives feedback about an obstacle too late

       - How this could occur given the true statement above:

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


**True statement from UCA context: The vehicle is approaching the point where the vehicle would normally brake, but adverse weather conditions (road traction) require that the braking should begin earlier than normal**

Belief:

*Apollo incorrectly believes that the point at which braking is required is as normal*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the current weather / environmental conditions

       - How this could occur given the true statement above:

           - Sensors are not calibrated to distinguish snow, ice, 'black' ice, standing water, chemical spills, oils spills, slippery mud left by farm vehicles, soggy leaves or other commonly occuring substances

               - **REQUIREMENT REQ-37: Sensors must be calibrated to detect all reasonabely probable sustances that could affect vehicle traction such as black ice, standing water, oil / chemical  spills, and excessive mud, dust or rotting leaves**


Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Algorithm flaw: Control model does not account for adverse weather conditions of the prevailing type when determining the deceleration limit when braking for the upcoming manoeuvre


               - **REQUIREMENT REQ-36: Apollo must be able to deduce and account for all reasonabely probable sustances that could affect vehicle traction such as black ice, standing water, oil / chemical  spills, and excessive mud, dust or rotting leaves**


#### UCA-6.17: Apollo removes brake control too early when relative velocity and distance to an obstacle mean that a collision will occur[H-2] [H-3] [H-4]

**True statement from UCA context: The vehicle is approaching an obstacle, and slows down to some extent but then removes the braking control**

Belief:

*Apollo incorrectly believes that the relative distance is higher than in reality*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the relative distance

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


Belief:

*Apollo incorrectly believes that it has achieved the planned vehicle velocity*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the determine the vehicle velocity

       - How this could occur given the true statement above:

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - Vehicle speed sensors suffer an internal failure

               - **REQUIREMENT REQ-41: The vehicle speed sensors are critical and must be redundant and designed and test for operational reliability**

           - GPS / GNSS / IMU sensors are offline, reporting stale data, or data transmission is delayed

               - **REQUIREMENT REQ-38: The overall geolocation system must be robust enough to cope with momentary communication losses, and have some form of backup**


Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: Apollo receives feedback that it is not decelerating as expected

       - How this could occur given the true statement above:

           - Apollo was presented with accurate data from at least one sensor, but it was discarded, distorted or overwritten due to an incorrect priority scheme or process model conflict

               - **REQUIREMENT REQ-33: Priority schemes must be designed with voting systems, consistency checks  and redundancy, rather than crude averages or simple hierarchies**

           - Assumed deceleration is used to calculate braking duration rather than monitoring the actual vehicle velocity

               - **REQUIREMENT REQ-71: When braking Apollo must heuristically adapt the level of braking if the deceleration is too slow, or too rapid**


Belief:

*Apollo believes that the target velocity is different to that required in reality*

Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Apollo miscalculates due to a programming fault


**True statement from UCA context: The original target velocity was achieved but a changing obstacle path now requires further action**

Belief:

*Apollo incorrectly believes that original reduction in velocity was sufficient*

Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Hardware flaw: Insufficient resources delay the cycle between receipt of the new sensor data and a command being sent


               - **REQUIREMENT REQ-45: Apollo must have hardware capable of processing all data received in real time, with contingency to account for unexpected data bursts, and a real time operating system**


       - Algorithm flaw: Excessive weight is placed on previous calculations leading to a trajectory that does not decelerate rapidly enough


               - **REQUIREMENT REQ-79: Apollo must discard previous trajectory calculations when the situation suddenly changes - this impacts 'stitching' algorithms**


Type 2 scenario:

   -  Apollo does not receive feedback / information when needed

       - Information received: The feedback is insufficiently prompt to allow the process model to be updated in time to take action

       - How this could occur given the true statement above:

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


Belief:

*Apollo incorrectly believes that the obstacle will clear the vehicle's path*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately predict obstacle’s path

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**

           - The vehicle was originally on trajectory to leave the lane but e.g. has swerved back suddenly

               - **REQUIREMENT REQ-45: Apollo must have hardware capable of processing all data received in real time, with contingency to account for unexpected data bursts, and a real time operating system**


               - **REQUIREMENT REQ-47: Apollo must be capable of tracking all reasonablely likely obstacles, from lamp posts and trash cans to people, pets, and cattle**


#### UCA-6.19: Apollo stops applying brake control when in autonomous mode before (> TBD seconds before) vehicle slows to acceptable speed (speed limit, traffic flow limit, manoeuvre limit, planned test limit, limits for controllability, stability, etc.)[H-1] [H-2] [H-3] [H-4] [H-6]

**True statement from UCA context: The vehicle was decelerating at an appropriate rate in order to enter the manoeuvre, but decleration has ceased**

Belief:

*Apollo incorrectly believes that it has achieved a vehicle target velocity consistent with the planned manoeuvre*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the determine the vehicle velocity

       - How this could occur given the true statement above:

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - Vehicle speed sensors suffer an internal failure

               - **REQUIREMENT REQ-41: The vehicle speed sensors are critical and must be redundant and designed and test for operational reliability**

           - GPS / GNSS / IMU sensors are offline, reporting stale data, or data transmission is delayed

               - **REQUIREMENT REQ-38: The overall geolocation system must be robust enough to cope with momentary communication losses, and have some form of backup**


Belief:

*Apollo incorrectly believes that it has entered the corner, apex, or exited the corner*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - The feedback received is insufficient to accurately determine the current position relative to the manoeuvre being executed

       - How this could occur given the true statement above:

           - Externally mounted sensors have their alignment, focus, or position compromised, or are blocked by environmental or load-shed debris

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - One or more sensors suffer an internal failure

               - **REQUIREMENT REQ-38: The overall geolocation system must be robust enough to cope with momentary communication losses, and have some form of backup**


**True statement from UCA context: The vehicle was decelerating at an appropriate rate in order to enter the manoeuvre, but decleration has ceased**

Belief:

*Apollo incorrectly believes that the safe speed for the manoeuvre is higher than in reality*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - The feedback is insufficient to determine the required manoeuvre velocity

       - How this could occur given the true statement above:

           - The change in perspective as the vehicle begins to enter the bend leads to an underestimation of the remaining curvature, due to limited field-of-view

               - **REQUIREMENT REQ-76: Apollo must adopt a worst-case  view when deducing road curvature**


**True statement from UCA context: The vehicle has completed ‘standard’ deceleration for the manoeuvre, but further deceleration is required because of adverse weather / road conditions**

Belief:

*Apollo incorrectly believes that the safe manoeuvre speed is higher than in reality because it has failed to identify adverse weather / road conditions*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the current weather / environmental conditions

       - How this could occur given the true statement above:

           - Sensors are not calibrated to distinguish snow, ice, 'black' ice, standing water, chemical spills, oils spills, slippery mud left by farm vehicles, soggy leaves or other commonly occuring substances

               - **REQUIREMENT REQ-37: Sensors must be calibrated to detect all reasonabely probable sustances that could affect vehicle traction such as black ice, standing water, oil / chemical  spills, and excessive mud, dust or rotting leaves**


Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Weather conditions that lead to a slight slipping of the vehicle, and therefore reduced g-force, are interpreted as lower radius of curvature or a higher maximum speed


Belief:

*Apollo incorrectly believes that the vehicle is in a unstable state when it is not*

Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Undulations in the road, coupled with fluctuations in the road surface texture and deviations in the road relative to a circular arc are misinterpreted as vehicle slippage


#### UCA-6.20: Apollo continues applying brake control too long (> TBD seconds) after vehicle slows to acceptable speed (speed limit, traffic flow limit, manoeuvre limit, planned test limit, limits for controllability, stability, etc.)[H-3] [H-4]

**True statement from UCA context: The vehicle has approached a e.g. a corner, slowed down, but is now slowing down to a speed that is below the expectations of other driver and (for example) the UK highway code for 'progress'**

Belief:

*Apollo incorrectly believes that the vehicle is travelling faster than in reality*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information received: The feedback received is insufficient to accurately determine the determine the vehicle velocity

       - How this could occur given the true statement above:

           - A data error on the sensor(s) data bus prevents up-to-date data from being received

               - **REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**

           - The controller receives stale data because the feedback transmission medium is overloaded by this or other sensors

               - **REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**

           - Vehicle speed sensors suffer an internal failure

               - **REQUIREMENT REQ-41: The vehicle speed sensors are critical and must be redundant and designed and test for operational reliability**

           - GPS / GNSS / IMU sensors are offline, reporting stale data, or data transmission is delayed

               - **REQUIREMENT REQ-38: The overall geolocation system must be robust enough to cope with momentary communication losses, and have some form of backup**


Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Algorithm flaw: The algorithm is excessively cautious, making a lack of progress; the risk of rear end collision / overtaking collisions is increased


#### UCA-6.21: Apollo stops applying brake control too soon at end of test before driver has resumed control (e.g. manual braking)[H-1] [H-2] [H-3] [H-4]

**True statement from UCA context: The vehicle comes to a halt at some predesignated position, but the brakes have not been engaged prior to the human driver resuming control**

Belief:

*Apollo mistakenly believes that the human driver has taken control*

Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Algorithm flaw: Apollo automatically drops to human control (automatic off) without the human's knowledge or instruction


               - **REQUIREMENT REQ-48: Apollo must be programmed to stop in a safe location and apply the parking brake at the end of the journey**


Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Apollo does not account for the end of the test period and apply brakes (either a standard continuous brake command, or a transition to ‘Park’ mode)


               - **REQUIREMENT REQ-48: Apollo must be programmed to stop in a safe location and apply the parking brake at the end of the journey**


Belief:

*Apollo mistakenly believes it is supplying sufficient brake*

Type 2 Scenario:

   -  Apollo receives incorrect feedback / information:

       - Information such as the local angle of the road (relative to the vertical action of gravity) is either not fed back to the process model, or it is not taken into account


Type 1 Scenario:

   -  Controller receives correct feedback but interprets it incorrectly or ignores it:

       - Information received: Feedback is sufficient to determine that the vehicle is on a hill

       - How this could occur given the true statement above:

           - Apollo does not account for the enhanced braking requirement

               - **REQUIREMENT REQ-77: Apollo must account for gradient when applying the brakes**

           - The specific local gradient is rejected in favour of the map gradient

               - **REQUIREMENT REQ-78: Apollo must use the local gradient, rather than the map gradient, when applying the brakes when stationary**


#### UCA-6.22: CA-6.22: Apollo stops applying brake control when collision occurs and driver has not resumed control (e.g. manual braking)[H-1] [H-2] [H-3] [H-4] [H-5]

**True statement from UCA context: The vehicle has been brought to rest, but the vehicle drops out of automatic mode following a collision - leaving the vehicle free to move on e.g. a hill, or if further collisions take place**

Belief:

*Apollo mistakenly believes that the human driver has taken control*

Type 1 scenario:

   -  Inadequate control algorithm / hardware

       - Algorithm flaw: The control state transitions to human control mode

       - How this could occur given the true statement above:

           - Following a collision and being brought to rest, automatic mode is simply ended without 'Park' being engaged

               - **REQUIREMENT REQ-48: Apollo must be programmed to stop in a safe location and apply the parking brake at the end of the journey**

           - The collision and associated trajectory change are misinterpreted as a human override, leading to drop out of automatic mode

               - **REQUIREMENT REQ-52: Apollo must bring the vehicle to rest and apply the parking brake after a collision**

           - The algorithm attempts to slow down to avoid a collision, but the algorithm does not recognise a post collision scenario, and therefore simply carries on going

               - **REQUIREMENT REQ-50: Apollo's collision sensors must still be capable of reporting a collision even when extensive damage to the vehicle has taken place**


               - **REQUIREMENT REQ-51: Apollo must be capable of detecting less severe collisions that do not immediately threaten life but require immediate attention, such as a broken windscreen, loose exhaust, etc**


               - **REQUIREMENT REQ-52: Apollo must bring the vehicle to rest and apply the parking brake after a collision**
