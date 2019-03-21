# STPA Requirements

**REQUIREMENT REQ-1: Physical brake actuators must be designed must be designed and tested to be operationally reliable**


**REQUIREMENT REQ-2: The battery / alternator power system must be designed and tested to be operationally**


**REQUIREMENT REQ-3: The power supply route to the brake actuators must be redundant if practicable**


**REQUIREMENT REQ-4: The power supply system must not issue brake actuator 'sleep' commands during normal operation**


**REQUIREMENT REQ-5: The brake command transmission rate should not exceed the rate at which the brake actuators can process commands**


**REQUIREMENT REQ-6: Any brake actuator buffers should routinely purge data on a FIFO basis**


**REQUIREMENT REQ-7: The brake commands should not be implemented on a select-exectute model**


**REQUIREMENT REQ-8: All system commands must be mainted in a master I/O schedule that, where practicable, uses unique addressing for each component and command**


**REQUIREMENT REQ-9: All vehicle systems must be time synchronised via an on-board clock master, rather than 'dialing out' to an off-vehicle source**


**REQUIREMENT REQ-10: Transmission media should be polled regularly where practicable to ensure that false positives are not reported**


**REQUIREMENT REQ-11: All command and data pathways must be redundant and self-healing where practicable**


**REQUIREMENT REQ-12: All transmission media should be polled or tested automatically, including secondary routes**


**REQUIREMENT REQ-13: All systems using the transmission media must determine the currently active route prior to commencing normal operation**


**REQUIREMENT REQ-14: Buffered transmission must be accomplanied by a buffer purge when the route fails for longer > than TBD seconds**


**REQUIREMENT REQ-15: All controllers and sensors must use send rates such that the total usage of the bus or network, for all clients, does not exceed the media bandwidth**


**REQUIREMENT REQ-16: Analogue values should be transmitted cyclically, or a change threshold should be applied**


**REQUIREMENT REQ-17: Critical systems should take priority over non-critical systems when using the transmission media**


**REQUIREMENT REQ-18: The autonomous system must be equipped with sensors and algorithms capable of detecting standing water, in order to slow down before entering**


**REQUIREMENT REQ-19: The autonomous system must be capable of detecting when there is or has been heavy rain, in order to accound for reduced traction**


**REQUIREMENT REQ-20: Critical auxiliary systems must be designed and tested for operational reliability**


**REQUIREMENT REQ-21: The human driver should be warned (acoustically or visually) when they are about to exceed the override threshold**


**REQUIREMENT REQ-22: The human driver / monitor should be informed (acoustically or visually) when a channel override is activated or deactivated**


**REQUIREMENT REQ-23: Both the driver and safety driver e-stop buttons should activate a klaxon or other warning device to signal all channels are overridden**


**REQUIREMENT REQ-24: E-stop controls should be non-latching since DataSpeed requires the override to be manually disabled already**


**REQUIREMENT REQ-25: Data types and formats should be kept consistent from command source through to actuator; unnecessary protocol conversion should be eliminated**


**REQUIREMENT REQ-26: Transmission media should be rigorously isolated and designed and tested for operational reliability**


**REQUIREMENT REQ-27: The brake actuators must not default to braking upon an unknown command state**


**REQUIREMENT REQ-28: The human driver should be constantly alert but should not cover the pedals unless braking may be likely**


**REQUIREMENT REQ-29: Factory configuration should be used in the brake actuators with scaling changes applied in the controller, where practicable**


**REQUIREMENT REQ-30: All FOTA methods should have a cyclic check and automatic roll-back method in the event of a failed download**


**REQUIREMENT REQ-31: A primary command pathway should not automatically activate on restoration if the secondary has not failed and the routes are otherwise identical**


**REQUIREMENT REQ-32: A transmission media that has degraded to the point where it impacts safety must be considered failed**


**REQUIREMENT REQ-33: Priority schemes must be designed with voting systems, consistency checks  and redundancy, rather than crude averages or simple hierarchies**


**REQUIREMENT REQ-34: Sensors must be mounted and shaped so that they cannot collide with the environment or snag debris, and be self cleaning where applicable**


**REQUIREMENT REQ-35: All sensors must be designed and tested for operational reliability**


**REQUIREMENT REQ-36: Apollo must be able to deduce and account for all reasonabely probable sustances that could affect vehicle traction such as black ice, standing water, oil / chemical  spills, and excessive mud, dust or rotting leaves**


**REQUIREMENT REQ-37: Sensors must be calibrated to detect all reasonabely probable sustances that could affect vehicle traction such as black ice, standing water, oil / chemical  spills, and excessive mud, dust or rotting leaves**


**REQUIREMENT REQ-38: The overall geolocation system must be robust enough to cope with momentary communication losses, and have some form of backup**


**REQUIREMENT REQ-39: Apollo must be able to resolve complex 3D structures from the sensor data with which it is provided**


**REQUIREMENT REQ-40: Apollo and its sensors must be capable of determining the correct right of way, including route curvature, from sensors alone**


**REQUIREMENT REQ-41: The vehicle speed sensors are critical and must be redundant and designed and test for operational reliability**


**REQUIREMENT REQ-42: Sensors must be capable of distinguishing the traffic lights applicable to the to the selected right of way from many potential candidates**


**REQUIREMENT REQ-43: Apollo and it sensors must be capable of resolving temporary traffic lights, including signs held by workmen, independently of map data**


**REQUIREMENT REQ-44: Apollo and its sensors must be capable of detecting fallen pedestrians in order to prevent fatality**


**REQUIREMENT REQ-45: Apollo must have hardware capable of processing all data received in real time, with contingency to account for unexpected data bursts, and a real time operating system**


**REQUIREMENT REQ-46: All data received must correctly assembled into the relevant frame**


**REQUIREMENT REQ-47: Apollo must be capable of tracking all reasonablely likely obstacles, from lamp posts and trash cans to people, pets, and cattle**


**REQUIREMENT REQ-48: Apollo must be programmed to stop in a safe location and apply the parking brake at the end of the journey**


**REQUIREMENT REQ-49: Apollo must be capable of identifying the journey's end, and able to identify a safe stopping location**


**REQUIREMENT REQ-50: Apollo's collision sensors must still be capable of reporting a collision even when extensive damage to the vehicle has taken place**


**REQUIREMENT REQ-51: Apollo must be capable of detecting less severe collisions that do not immediately threaten life but require immediate attention, such as a broken windscreen, loose exhaust, etc**


**REQUIREMENT REQ-52: Apollo must bring the vehicle to rest and apply the parking brake after a collision**


**REQUIREMENT REQ-53: Apollo must not move off after a collision, unless instructed to do so by the human occupants**


**REQUIREMENT REQ-54: Apollo hardware must be capable of receiving and processing the maximum data throughput of all its data buses**


**REQUIREMENT REQ-55: Apollo must be made aware of channel overrides and be able to account for them**


**REQUIREMENT REQ-56: A total DataSpeed e-stop should be fed back to Apollo and Apollo should disengage automatic mode**


**REQUIREMENT REQ-57: Sensors should purge buffered data after TBD ms in order to prevent sensor ghosting**


**REQUIREMENT REQ-58: Apollo must have regular access to map updates so that detailed information is up-to-date**


**REQUIREMENT REQ-59: Apollo and its sensor must be capable of identifying and reading speed limit signs, variable speed limit signs and advisories**


**REQUIREMENT REQ-60: Apollo sensors must be capable of detecting a rate of change of altitude**


**REQUIREMENT REQ-61: The vehicle on-board time master clock must be routinely and accurately synchronised to UTC**


**REQUIREMENT REQ-62: Apollo algorithm must take account of time-dependent access and speed limits, for example school zones and bus lanes**


**REQUIREMENT REQ-63: Apollo must detect a human application of throttle and not apply the brakes**


**REQUIREMENT REQ-64: The ABS unit should be monitored via robust means such as an externally wetted life contact, and the feedback supplied to Apollo**


**REQUIREMENT REQ-65: Apollo must account for ABS availability when deciding braking level**


**REQUIREMENT REQ-66: Apollo's map source must be updates as soon as practicable when map data changes**


**REQUIREMENT REQ-67: Apollo and its sensor must be capable of identying roadworks, police cordons, traffic accident scenes and following route markers such as cordons and lines of cones**


**REQUIREMENT REQ-68: Apollo must account for environmental conditions of the prevailing type when calculation the safe speed for manoeuvres**


**REQUIREMENT REQ-69: Vehicle stability must not be processed as a 'latched' condition**


**REQUIREMENT REQ-70: Apollo must correctly derive the vehicle stability condition from the available sensors**


**REQUIREMENT REQ-71: When braking Apollo must heuristically adapt the level of braking if the deceleration is too slow, or too rapid**


**REQUIREMENT REQ-72: Apollo must be capable of distinguishing broken down vehicles from queuing traffic**


**REQUIREMENT REQ-73: Apollo must be accurately calibrated for the braking system**


**REQUIREMENT REQ-74: Where Apollo is required to access historic data, it must be ensured that e.g. the data is compatmentalized to avoid linearly growing seek times**


**REQUIREMENT REQ-75: Apollo must be able to temporarily track objects that are momentarily out of view**


**REQUIREMENT REQ-76: Apollo must adopt a worst-case  view when deducing road curvature**


**REQUIREMENT REQ-77: Apollo must account for gradient when applying the brakes**


**REQUIREMENT REQ-78: Apollo must use the local gradient, rather than the map gradient, when applying the brakes when stationary**


**REQUIREMENT REQ-79: Apollo must discard previous trajectory calculations when the situation suddenly changes - this impacts 'stitching' algorithms**

