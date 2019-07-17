# Level 2 Scenario Analysis

## Apollo Brake Command

### UCA: Apollo does not provide a brake command when relative velocity and distance to an obstacle mean that a collision is imminent.

Basic Scenario #1: 
	- A does not provide brake command
	- Feedback indicates that relative velocity/distance is such that a collision is imminent

		- A does not provide a brake command due to a physical failure of the A controller (loss of power, damaged components, etc.)

		- A does not provide a brake command because it does not know it has to provide a brake command when a collision is imminent.
 			a) ... the requirements are correct but the software implementation is flawed in that it is not implemented that a brake command has to be provided when a collision is imminent (e.g. programmers over-worked, de-motivated, etc.) 
 			b) ... the software requirements are flawed in that they do not specify that a brake command has to be provided whenever relative velocity and distance to an obstacle mean that a collision is imminent (e.g. due to missing requirements, data loss in requirements management, etc.)
 			c) ... the software or the responsibiliities of the software have changed 
   				... it was initially correctly implemented in the software that a brake command has to be provided when a collision is imminent but over time the software was changed and part of the implementation was lost (e.g. by means of an update).
   				... an older design version required that no brake command is provided when a collision is imminent (e.g. driver was notified of a hazard and had to intervene by procedure) but the vehicle matured and A was now supposed to provide brake commands when a collision is imminent, too. A software update addressing the change, however, has not been performed. 

		- A does not provide a brake command when a collision is imminent because it receives a control input to send brake commands only to the monitoring display (e.g. for testing purposes, maintenance unfinished, hackers, pilot input due to mistrust, etc.)

		- A does not provide a brake command when a collision is imminent because it receives a control input to go to 'sleep mode' and therefore does not react on commands.

		- A receives a control input to disable autonomy modules or switch off completely.

		- A receives an input that indicates a fault and as a result A inhibits giving a brake command (e.g. propulsion, steering, braking, watchdog fault flag, etc.) 

Basic Scenario #2:
	- A collision is imminent
	- feedback to A indicates that no collision is imminent

		- A erroneously believes that there is no collision imminent due to feedback issues with feedback on:    
 		#1 relative position to an obstacle 
 		#2 closing speed 
 		#3 direction of the vehicle and/or the obstacles 
 		#4 acceleration of the vehicle and/or the obstacles 
 		#5 Brakes applied
 			a) ... A receives feedback #1 - #4 that indicates there is no collision imminent (e.g. sensors mounted incorrectly, sensor focus or position compromised, sensor blocked, etc.)
 			a) ... A receives incorrect feedback that indicates that the obstacle type does not pose a collision danger.
 			a) ... A receives feedback that there is no obstacle to collide with (e.g. due to obscured sensor, sensor mounted in wrong position/orientation, sensors offline, obstacle outside of sensor view, adverse weather conditions identified incorrectly (missing algorithm functionality), not calibrated, etc.)
 			a) ... A receives incorrect feedback that the collision is already averted e.g. the brakes or steering are applied already (e.g. sensors mounted incorrectly, sensor focus or position compromised, sensor blocked, etc.)
 			b) ... A receives feedback that there is a collision imminent but interprets the feedback as obsolete (ignores feedback) because it reasons that the vehicle is at a stop (e.g. because feedback containts information that the wheel turning rate is zero)
			c) ... A receives feedback #1 - #4 delayed or not at all
 				c1) ... feedback is sent by brake/LIDAR/etc. sensors but not received at A in time because communication is blocked (BUS busy, BUS broken, EMI, etc.)
 				c2) ... feedback is not sent by brake/LIDAR/etc. and a default "most likely feedback" is used (e.g. because of sensor failure(s), flawed requirements, sensor loss of power, etc.)
 			d) ... feedback #1 - #5 do not exist or are not available to A by design (e.g. requirements incomplete, cuts on project scope, etc.)

Basic Scenario #3:
	- A sends brake command
	- brakes are not actuated

		- A provides a brake command but brake actuators do not provide braking force.
 			a) ... because the communication channel to the actuator is blocked (e.g. cables are damaged, EMI, communication lines incorrectly installed, etc.) 
 			a) ... because DataSpeed does not pass on the brake command because it is in some driver override mode (e.g. throttle more than 30%, etc.) 
 			a) ... because DataSpeed does not pass on the command because SDs provided Estop
 			a) ... because system is in some overload state (e.g. DataSpeed busy, energy prioritized between DataSpeed and other consumers, etc.)
 			b) ... because brake command is sent but actuator does not respond due to an actuator failure (piston jammed, loss of hydraulic power, actuator in 'sleep', buffer overload, actuator busy with other command, etc.)
 			c) ... because actuator receives brake command and provides braking actuation but no braking force is generated by hydraulic cylinder (e.g. actuator loss of power, actuator assembled incorrectly, etc.)
		- [None]

Basic Scenario #4:
	- A sends brake command
	- brakes are actuated but vehicle won't slow down

		- A provides a brake command and brakes are applied but vehicle won't slow down.
 			a) … applying brakes has no effect (e.g. due to brake disc disconnect, wheels hydroplane, etc.)
		- [None]











