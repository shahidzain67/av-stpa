Requirements

R-1: If insufficient feedback is provided to determine relative velocity, Apollo must assume worst case scenario and come to a stop. [UCA-6.1]

R-2: If different sensors provide different values, the worst case scenario should be assumed and vehicle should be brought to a stop. [UCA-6.1]

R-3: If insufficient feedback is provided to determine relative distance, Apollo must assume worst case scenario and come to a stop. [UCA-6.1] 

R-4: Apollo must be able to detect if sensors have been compromised (due to e.g. roof mounted sensors collide with obstacle, something blocks images, etc). [UCA-6.1] [UCA-6.2] [UCA-6.7]

R-5: Sensors must be robust to environmental conditions. [UCA-6.1] [UCA-6.2] [UCA-6.3] [UCA-6.7]

R-6: Multiple sensors should be used with voting system incase of sensor failure. [UCA-6.1] [UCA-6.2] [UCA-6.3] [UCA-6.7]

R-7: Apollo must be able to detect adverse weather conditions. [UCA-6.1] [UCA-6.2]

R-8: Apollo must be able to detect road conditions that could affect vehicle traction. [UCA-6.1] [UCA-6.2]

R-9: Apollo must be equipped to detect and deal with environmental conditions such as black ice, leaves, water, unforeseen spillages or environmental debris. [UCA-6.1] [UCA-6.2]

R-10: Apollo must be able to detect if sensors (GPS/Optical system) are offline and respond accordingly. [UCA-6.2] [UCA-6.4]

R-11: If feedback from sensors is not received within x seconds, Apollo must assume location data is not accurate/up-to-date. [UCA-6.2]

R-12: Apollo must check how location data is changing compared to velocity information, to ensure stale data is not being used. [UCA-6.2]

R-13: Apollo must be able to detect sensor failure. [UCA-6.2]

R-14: If insuffient data is received to calculate road curvature Apollo should be brought to a stop. [UCA-6.2]

R-15: Apollo must calculate road curvature to check with map position. [UCA-6.2]

R-16: If Apollo believes it is in an unstable state, the vehicle should be brought to a stop. [UCA-6.2]

R-17: If insufficient feedback is given to determine the traffic flow limit, Apollo should be brought to a stop. [UCA-6.2]

R-18: Apollo must process surrounding object data and traffic flow speed data with appropriate ratings. [UCA-6.2]

R-19: If insufficient processor power to calculate the traffic flow speed, worst case scenario must be assumed. [UCA-6.2]

R-20: If there is a planned test speed limit, this mode must be activated. [UCA-6.2]

R-21: If insuffient feedback is given to determine the state of a traffic light, red should be assumed. [UCA-6.3]

R-22: If cameras are not available Apollo must be brought to a stop. [UCA-6.3]

R-23: Sensors must have a large enough field of view to detect low-lying obstacles. [UCA-6.3]

R-24: If processed data has not been updated within x seconds, Apollo must be brought to a stop. [UCA-6.3]

R-25: Controller algorithm must be programmed to stop at the end of the journey. [UCA-6.4]

R-26: If sensors have been compromised, Apollo must be brought to a stop. [UCA-6.5]

R-27: Sensors must be able to detect collions that can cause critical failures. [UCA-6.5]

R-28: Collision sensors must be built into the vehicle design and be routed through the appropriate data interfaces. [UCA-6.5]

R-29: If collision is detected, Apollo must be brought to a stop. [UCA-6.5]

