# Level 2 Unsafe Control Actions (UCAs)

<table class="table table-bordered">
  <tr>
    <th>Control Action</th>
    <th>Not Providing</th>
    <th>Providing</th>
    <th>Too Early / Too Late / Out of Order</th>
    <th>Stopped Too Soon / Applied Too Long</th>
  </tr>

  <tr>
    <td>brake command<br><br> </td>
    <td class="Not Providing">
	   SD does not proide manual brake cmd when Autonomous SW engaged at start of test (will prevent shift to D) <br><br>
	   SD does not provide manual brake cmd when forward or side collision is imminent <br><br>
	   SD does not provide manual brake cmd when vehicle speed exceeds planned test limits  (2) <br><br>
	   SD does not provide manual brake cmds when Autonomous SW is not controlling brakes (overriden, disengaged, Estop) <br><br>
	   SD does not provide manual brake cmd when vehicle does not detect traffic control device that requires slowing down (e.g. red light, stop sign, etc.) <br><br>
	   SD does not provide manual brake cmd when emergency vehicle is present <br><br>
	   SD does not provide manual brake cmd when automated steering is inconsistent with vehicle speed (e.g. about to destabilize vehicle) <br><br>
	   SD does not provide manual brake cmd when Autonomous SW engaged at start of test (will prevent shift to D) <br><br>
	   SD does not provide manual brake command when Autonomous SW is not controlling brakes (overridden, disengaged, Estop) <br><br>
	   SD does not provide manual brake cmd when Autonomous SW engaged at start of test (will prevent shift to D) <br><br>
	   SD does not provide manual brake cmd when forward or side collision is imminent <br><br>
	   SD does not provide manual brake cmd when vehicle does not detect traffic control device that requires slowing (e.g. red light, stop sign, etc.) <br><br>
	   SD does not provide manual brake cmd when emergency vehicle is present <br><br>
	   SD does not provide manual brake cmd when vehicle speed exceeds planned test limits <br><br>
	   SD does not provide required manual brake cmds when Autonomous SW is not controlling brakes. (overridden, disengaged, Estop) <br><br>
	   SD does not provide manual brake cmd when automated steering is inconsistent with vehicle speed (e.g. about to destabilize vehicle) 
    </td>
	<td class="Providing">
		SD provides insufficient manual braking to prevent collision when forward or side collision is imminent <br><br>
		SD provides insufficient manual braking to override Autonomous SW when Autonomous SW is accelerating and deceleration is needed (vehicle speed exceeds limits, collision is imminent, or emergency vehicle is present) <br><br>
		SD provides manual braking cmd but brake lights are not functional <br><br>
		SD provides sudden manual brake cmd when there is following traffic that cannot decelerate in time <br><br>
		SD provides manual braking cmd but brake lights are not functional <br><br>
		SD provides manual brake cmd too late at start of test causing override after Autonomous SW engages <br><br>
		SD provides insufficient manual braking to prevent collision when forward or side collision is imminent <br><br>
		SD provides insufficient manual braking to override Autonomous SW when Autonomous SW is accelerating and deceleration is needed (vehicle speed exceeds limits, collision is imminent, or emergency vehicle is present)
    </td>
    <td class="Too Early / Too Late / Out of Order">
		SD provides manual brake cmd too late at start of test causing override after Autonomous SW engages <br><br>
		SD applies manual braking too late to avoid imminent collision <br><br>
		SD applies manual braking too early before vehicle is in safe area to decelerate <br><br>
		SD applies manual braking too late to avoid imminent collision <br><br>
		SD applies manual braking too early before vehicle is in safe area to decelerate
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
		SD applies manual braking too long after collision is averted (potentially causing another collision) <br><br>
		SD applies manual braking too long after overspeed is corrected (potentially causing another collision) <br><br>
		SD stops manual braking early before collision is averted or before overspeed is corrected (L-1,L-2] <br><br>
		SD stops providing manual braking cmds too early before Autonomous SW is re-engaged <br><br>
		SD applies manual braking too long after collision is averted (potentially causing another collision) <br><br>
		SD applies manual braking too long after over speed is corrected (potentially causing another collision) <br><br>
		SD stops manual braking early before collision is averted or before over speed is corrected <br><br>
		SD stops providing manual braking cmds too early before Autonomous SW is re-engaged
    </td>
  </tr>
  <tr>
    <td>throttle command<br><br></td>
    <td class="Not Providing">
		SD does not provide manual throttle cmds when Autonomous SW is not controlling throttle (overriden, disengaged, Estop) <br><br>
		SD does not provide manual throttle cmd when vehicle speed is too slow for the area <br><br>
		SD does not provide manual throttle cmd when rear or side collision is imminent <br><br>
		SD does not provide manual throttle cmds when Autonomous SW is not controlling throttle (overriden, disengaged, Estop) <br><br>
		SD does not provide manual throttle cmd when vehicle speed is too slow for the area <br><br>
		SD does not provide manual throttle commands when Autonomous SW is not controlling throttle (overridden, disengaged, Estop)
    </td>
    <td class="Providing">
		SD provides manual throttle cmd when the vehicle's path is not clear <br><br>
		SD provides manual throttle cmd when an object is about to enter vehicle's path <br><br>
		SD provides manual throttle cmd when forward or side collision is imminent <br><br>
		SD provides manual throttle cmd when deceleration is required <br><br>
		SD provides insufficient manual throttle to override when Autonomous SW is braking erroneously <br><br>
		SD provides insufficient manual throttle to avert rear or side collision <br><br>
		SD provides excessive manual throttle cmds when vehicle speed is at or near planned test limits
	</td>
    <td class="Too Early / Too Late / Out of Order">
		SD provides manual throttle cmd too late to avoid rear or side collision <br><br>
		SD provides manual thorttle cmd too early before vehicle path is clear
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
		SD continues to provide manual throttle cmd too long until forward collision becomes imminent <br><br>
		SD continues to provide manual throttle cmd too long until planned test limits are exceeded <br><br>
		SD stops providing manual throttle cmds too early before Autonomous SW is re-engaged
    </td>
  </tr>
  
  <tr>
    <td>shift command<br><br></td>
    <td class="Not Providing">
		SD does not provide shift to D when Autonomous SW engaged at start of test (will prevent shift to D) <br><br>
		SD does not provide shift to P at end of test when vehicle at rest with brakes applied
    </td>
    <td class="Providing">
		SD provides shift to P (ignored) at end of test while previous shift is still in progress <br><br>
		SD provides shift to D (ignored) while previous shift is still in progress <br><br>
		SD provides shift to R,N,L at any time when Autonomous SW engaged  (3) <br><br>
		SD provides shift to P without disengaging Autonomous SW <br><br>
		SD provides shift to D (ignored) while previous shift is still in progress
    </td>
    <td class="Too Early / Too Late / Out of Order">
		SD provides shift to D too early when Autonomous SW is not yet engaged and Safety Driver is not applying brakes <br><br>
		SD provides shift to D too late after Autonomous SW already engaged <br><br>
		SD provides shift to P too late after Autonomous SW already disengaged, brakes released while in D or R <br><br>
		SD provides shift to D too early before Autonomous SW is engaged
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>estop command<br><br></td>
    <td class="Not Providing">
		SD does not provide Estop when a manual override is not effective <br><br>
		SD does not provide Estop when a fault is detected (fault in vehicle (e.g. AEB), Autonomous SW , dataspeed, Lidar, cameras (obstructed view), etc) <br><br>
		SD does not provide Estop when ending test operations <br><br>
		SD does not provide Estop when starting vehicle <br><br>
		SD does not provide Estop when raining (6) <br><br>
		SD does not provide Estop when automation does not detect obstacle in or near the vehicle's path (within TBD ft) <br><br>
		SD does not provide Estop when automation inadequately predicts movement of object in or near vehicle's path (including incorrectly classifying mobile object as static object) <br><br>
		SD does not provide Estop when automated steering commands do not correspond to calculated trajectory <br><br>
		SD does not provide Estop when automated brake/throttle commands do not correspond to calculated speed trend <br><br>
		SD does not provide Estop when calculated speed trend will violate planned speed limit for current location <br><br>
		SD does not provide Estop when calculated speed trend is inconsistent with calculated trajectory (e.g. will destabilize the vehicle) <br><br>
		SD does not provide Estop when automation calculates a trajectory outside the planned test path <br><br>
		SD does not provide Estop  when automation calculates a trajectory that presents an imminent collision
		SD does not provide Estop when automation calculates target speed trend with insufficient deceleration for an object on collision path <br><br>
		SD does not provide Estop when automated systems experience a fault (fault in vehicle (e.g. AEB), Autonomous SW , dataspeed, Lidar, cameras, etc.) <br><br>
		SD does not provide Estop when cameras on roof become visually obscured <br><br>
		SD does not provide Estop when Lidar becomes visually obscured <br><br>
		SD does not provide Estop when any HMI control is deactivated (e.g. Lidar inadvertently turned off) <br><br>
		SD does not provide Estop when any HMI sensor status turns red <br><br>
		SD does not provide Estop when radar is obscured (e.g. moth) <br><br>
		SD does not provide Estop when any HMI control is unexpectedly activated (e.g. Lidar inadvertently turned on
    </td>
	<td class="Providing">
		SD provides Estop before manual steering commands when straight travel presents a hazard (e.g. would place vehicle in opposing traffic lane, outside road markings, etc.) (11) <br><br>
		SD provides Estop before manual steering commands when steering action is required to avoid imminent collision <br><br>
		SD provides Estop before manual braking commands when braking action is required to avoid imminent collision <br><br>
		SD provides Estop before manual throttle commands when acceleration is required to avoid imminent collision <br><br>
		SD provides Estop when SD is not prepared to assume manual control when any HMI control is actuated (e.g. Lidar inadvertently turned off) <br><br>
		SD provides Estop when SD is not prepared to assume manual control when any HMI sensor status turns red
    </td>
    <td class="Too Early / Too Late / Out of Order">
		SD provides Estop too early before SD provides manual steering cmds during a turn (11) <br><br>
		SD provides Estop too late (> TBD s) after automation does not detect obstacle in or near the vehicle's path <br><br>
		SD provides Estop too late (> TBD s) after automation inadequately predicts movement of object in or near vehicle's path (including incorrectly classifying mobile object as static object) <br><br>
		SD provides Estop too late after automated steering commands diverge from calculated trajectory <br><br>
		SD provides Estop too late after automated brake/throttle commands diverge from calculated speed trend <br><br>
		SD provides Estop too late after calculated speed trend violates planned speed limit for location <br><br>
		SD provides Estop too late after calculated speed trend is inconsistent with calculated trajectory (e.g. will destabilize the vehicle) <br><br>
		SD provides Estop too late after automation calculates a trajecotry outside the planned test path <br><br>
		SD provides Estop too late after automation calculates a trajectory that presents an imminent collision <br><br>
		SD provides Estop too late after automation calculates target speed trend with insufficient deceleration for an object on collision path <br><br>
		SD provides Estop too late after automated systems experience a fault (fault in vehicle (e.g. AEB), Autonomous SW , dataspeed, Lidar, cameras, etc.)
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
		SD cancels Estop too soon before fault condition (fault in vehicle (e.g. AEB), Autonomous SW , dataspeed, Lidar, cameras, any "non-green" status, etc) has been diagnosed and resolved by technician <br><br>
		SD cancels Estop too soon before Autonomous SW has been disengaged, reset, and verified to be in known safe state/position <br><br>
		SD cancels Estop too soon before dataspeed has been reset and verified to be in known safe state/position <br><br>
		SD cancels Estop too soon before vehicle systems have been reset to known safe state (e.g. traction control) and vehicle maneuvered to known safe starting position <br><br>
		SD cancels Estop at any time (12)
    </td>
  </tr>
  
  <tr>
    <td>disengage estop<br><br></td>
    <td class="Not Providing">
		SD does not disengage Estop prior to start of test <br><br>
		SD or SD do not disengage Estop prior to enabling autonomy mode
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>reset Apollo<br><br></td>
    <td class="Not Providing">
		SD or SD do not reset (cold boot) Autonomous SW prior to resetting/releasing Estop
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>verify horn<br><br></td>
	<td class="Not Providing">
		SD does not verify functionality of horn prior to enabling autonomy mode
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>verify turn lights<br><br></td>
    <td class="Not Providing">
		SD does not verify functionality of turn signals prior to enabling autonomy mode
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>verify parking lights<br><br></td>
	<td class="Not Providing">
		SD does not verify functionality of parking lights prior to enabling autonomy mode
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>verify head lights<br><br></td>
	<td class="Not Providing">
		SD does not verify functionality of head lights (high beam & low beam) prior to enabling autonomy mode
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>verify wipers<br><br></td>
    <td class="Not Providing">
		SD does not verify functionality of windshield wipers prior to enabling autonomy mode
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>verify hazard lights<br><br></td>
    <td class="Not Providing">
		SD does not verify functionality of hazard lights when vehicle is about to set off <br><br>
		SD does not verify functionality of hazard lights prior to enabling autonomy mode
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>verify mirrors<br><br></td>
    <td class="Not Providing">
		SD does not verify functionality of mirrors when vehicle is about to set off <br><br>
		SD does not verify functionality of mirrors prior to enabling autonomy mode
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>stop test<br><br></td>
    <td class="Not Providing">
		SD does not stop test when camera performance has been impaired <br><br>
		SD does not stop test when actuation fault occurs <br><br>
		SD does not stop test when planned trajectory is outside acceptance bounds <br><br>
		SD does not stop test when camera or LIDAR performance has been impaired <br><br>
		SD does not stop test when GPS performance has been lost for an extended amount of time <br><br>
		SD does not stop test when OEM AEB capability is not functional (as indicated on vehicle instrumentation)
    </td>
    <td class="Providing">
		SD stops test when SD is not informed <br><br>
		SD stops tests when vehicle is in a maneuver difficult for the SD to manage (intersection, pedestrian crossing, bus merge lane) <br><br>
		SD stops test when SD is not ready to control the vehicle yet
    </td>
    <td class="Too Early / Too Late / Out of Order">
		SD stops test too late when vehicle is already about to go off-course
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>clean camera<br><br></td>
    <td class="Not Providing">
		SD does not clean cameras on roof when they are dirty, wet, or otherwise obscured <br><br>
		SD does not clean cameras on roof when performance has been impaired
    </td>
    <td class="Providing">
		SD cleans cameras on roof too late after they become dirty, wet, or otherwise obscured <br><br>
		SD damages cameras while cleaning
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>horn command<br><br></td>
    <td class="Not Providing">
		SD does not sound horn when vehicles/pedestrians must react to help avert collision (e.g. in blind spot of other vehicle, bus merging into traffic, etc.) <br><br>
		SD does not sound horn at start of testing to verify functionality
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>turn signals<br><br></td>
    <td class="Not Providing">
		SD does not engage turn signal TBD ft before automation (or SD) executes turning maneuver <br><br>
		SD does not engage turn signals in safe location (not on active road) at start of testing to verify functionality
    </td>
    <td class="Providing">
	SD engages turn signal without automation (or SD) executing a turning maneuver
    </td>
    <td class="Too Early / Too Late / Out of Order">
	SD engages turn signal too late (< TBD ft) before automation (or SD) executes turning maneuver
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
	SD cancels turn signal too soon before automation (or SD) executes turning maneuver <br><br>
	SD cancels turn signal too late after automation (or SD) executes turning maneuver
    </td>
  </tr>
  
  <tr>
    <td>verify parking lights<br><br></td>
    <td class="Not Providing">
		SD does not verify functionality of parking lights prior to enabling autonomy mode
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>engage parking lights<br><br></td>
    <td class="Not Providing">
    </td>
    <td class="Providing">
	SD engages parking lights at any time while driving
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td> disengage headlights<br><br></td>
    <td class="Not Providing">
		SD does not disengage head lights (high beam) when 500 ft from oncoming vehicle
    </td>
    <td class="Providing">
	SD disengages headlights when raining, when wipers are on, or when driving after sunset
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>engage headlights<br><br></td>
    <td class="Not Providing">
		SD does not turn headlights on when raining or when wipers are on <br><br>
		SD does not turn on head lights (low beam) during low-light conditions resulting in vehicle not seen by other road users <br><br>
		SD does not turn headlights on at start of testing to verify functionality of exterior lighting (head, marker, tail lights) <br><br>
		SD does not turn headlights on when raining <br><br>
		SD does not turn headlights on when driving after sunset <br><br>
		SD does not engage (high beam) headlights when environmental conditions require using lights (7) <br><br>
		SD does not reengage head lights (high beam) after turning them off for oncoming traffic when conditions require head lights <br><br>
		SD does not engage head lights during low-light conditions resulting in impaired SD vision
    </td>
	
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
		SD turns headlights on too late after rain starts <br><br>
		SD turns headlights on too late when vehice has started setting off in dark low visibility environment
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>engage high beam<br><br></td>
    <td class="Not Providing">
		SD does not engage high beam during low light conditions when there is no oncoming traffic (7) <br><br>
		SD does not reengage high beam during low light conditions when oncoming traffic has cleared <br><br>
		SD does not engage high beam at start of testing to verify functionality
    </td>
    <td class="Providing">
		SD turns on high beam when environment ahead is foggy <br><br>
		SD turns on high beam when closer than 500ft from oncoming vehicle
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>disengage high beam<br><br></td>
    <td class="Not Providing">
		SD does not disengage high beam when 500 ft from oncoming vehicle
    </td>
    <td class="Providing">
		SD disengages high beam during low light when there is no oncoming traffic
    </td>
    <td class="Too Early / Too Late / Out of Order">
		SD disengages high beam too late after oncoming vehicle is closer than 500 ft
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>engage windshield wipers<br><br></td>
    <td class="Not Providing">
		SD does not turn on wind shield wipers during rain conditions <br><br>
		SD does not engage wipers at start of testing to verify functionality <br><br>
		SD does not engage wipers when raining <br><br>
		SD does not engage wipers (wash mode) when windshield becomes dirty or obscured (8)
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
		SD engages wipers too late after windshield is obscured by rain, dirt, etc.
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>engage hazard lights<br><br></td>
    <td class="Not Providing">
		SD does not use hazard lights when pulling car over in presence of emergency vehicle <br><br>
		SD does not engage hazard lights when nearby traffic must be warned of an external hazard. E.g. roadway ahead is unexpectedly obstructed (animal crossing, delivery truck, etc), emergency vehicle present, etc. <br><br>
		SD does not engage hazard lights when vehicle functionality is impaired (E.g. vehicle unable to match speed of flow of traffic (too high or too low), unable to command full range of steering (e.g. partial loss of power steering, inability to override steering, etc.), or any other time vehicle behavior may present unexpected hazard to nearby traffic
    </td>
    <td class="Providing">
		SD engages hazard lights when vehicle functionality is not impaired and there is no external hazard
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>adjust mirrors<br><br></td>
    <td class="Not Providing">
		SD does not adjust mirrors to allow proper viewing
    </td>
    <td class="Providing">
		SD changes mirror position preventing proper viewing
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>adjust seating<br><br></td>
    <td class="Not Providing">
		SD does not adjust seating position to allow proper access to all controls and necessary views
    </td>
    <td class="Providing">
		SD changes seating position preventing proper viewing
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>engage parking brake<br><br></td>
    <td class="Not Providing">
		SD does not engage parking brake with vehicle in D to verify functionality before test <br><br>
		SD does not engage parking brake when parking the vehicle on an incline
    </td>
    <td class="Providing">
		SD engages parking brake when there is no emergency requiring additional braking
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>disengage parking brake<br><br></td>
    <td class="Not Providing">
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
		SD does not disengage parking brake (stop applying park brake) before testing begins
    </td>
  </tr>
  
  <tr>
    <td>configure mirrors<br><br></td>
    <td class="Not Providing">
		SD does not configure mirrors to allow proper viewing <br><br>
    </td>
    <td class="Providing">
		SD changes configuration of mirrors when new configuration makes view worse
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>configure seating<br><br></td>
    <td class="Not Providing">
		SD does not configure proper seating position prior to enabling autonomy mode
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>start autonomy<br><br></td>
    <td class="Not Providing">
		SD provides start autonomy command with wrong setup/configuration <br><br>
		SD starts autonomy when not all sensors are green
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>disable module<br><br></td>
    <td class="Not Providing">
		SD disables a required module when autonomy is enabled
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>call out<br><br></td>
    <td class="Not Providing">
		SD does not provide call out when an undetected object appears in the vehicle's path <br><br>
		SD does not provide call out when traffic light is detected incorrectly <br><br>
		SD does not call out module controller failure when vehicle is about to drive in autonomy mode
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>stop test<br><br></td>
    <td class="Not Providing">
		SD does not stop test when camera performance has been impaired <br><br>
		SD does not stop test when actuation fault occurs <br><br>
		SD does not stop test when planned trajectory is outside acceptance bounds <br><br>
		SD does not stop test when camera or LIDAR performance has been impaired <br><br>
		SD does not stop test when GPS performance has been lost for an extended amount of time <br><br>
		SD does not stop test when OEM AEB capability is not functional (as indicated on vehicle instrumentation)
    </td>
    <td class="Providing">
		SD stops test when SD is not informed <br><br>
		SD stops tests when vehicle is in a maneuver difficult for the SD to manage (intersection, pedestrian crossing, bus merge lane) <br><br>
		SD stops test when SD is not ready to control the vehicle yet
    </td>
    <td class="Too Early / Too Late / Out of Order">
		SD stops test too late when vehicle is already about to go off-course
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>engage Autonomous SW<br><br></td>
    <td class="Not Providing">
		SD engages Autonomous SW when vehicle transmission is in D
    </td>
    <td class="Providing">
		SD engages Autonomous SW when Autonomous SW has not been reset to a known safe start state, setup, and configuration (e.g. with a module disabled or configured improperly, after Backend Data reset, etc.) <br><br>
		SD engages Autonomous SW when dataspeed has not been reset to a known safe start state <br><br>
		SD engages Autonomous SW when vehicle is not "reset" (stopped, in D, vehicle on, centered in lane, on planned test path) <br><br>
		SD engages Autonomous SW when Estop is engaged <br><br>
		SD engages Autonomous SW when vehicle automation has not been reset to known safe starting state (e.g. traction control state, ABS inactive, stability control inactive, etc.) <br><br>
		SD engages Autonomous SW when autonomy system is not fully functional <br><br>
		SD engages Autonomous SW when vehicle steering has not been calibrated (see dataspeed FAQ)
    </td>
    <td class="Too Early / Too Late / Out of Order">
		... <br><br>
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>disengage Autonomous SW<br><br></td>
    <td class="Not Providing">
    </td>
    <td class="Providing">
		SD disables an Autonomous SW module at any time during testing or when Autonomous SW is engaged (15) <br><br>
		SD disables an Autonomous SW module at any time before testing or before Autonomous SW is engaged (15)
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>setup command<br><br></td>
    <td class="Not Providing">
    </td>
    <td class="Providing">
		SD provides Setup cmd at any time (15) <br><br>
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>reset command<br><br></td>
	<td class="Not Providing">
    </td>
    <td class="Providing">
		SD provides Reset All at any time (15) <br><br>
		SD provides Reset Backend Data at any time (15)
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>dump message<br><br></td>
    <td class="Not Providing">
    </td>
    <td class="Providing">
		SD provides Dump Message at any time (15)
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>
  
  <tr>
    <td>hazard warning signal<br><br></td>
    <td class="Not Providing">
		SD does not provide warning signal to vehicle or VRU entering forward path
    </td>
    <td class="Providing">
    </td>
    <td class="Too Early / Too Late / Out of Order">
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
    </td>
  </tr>

</table>

* (1) Assume all shifting is manual; Apollo can not control shifting
* (2) Planned test limits not fixed. E.g. speed should decrease before planned turns
* (3) Manual shifting may be required to maneuver vehicle before or after testing is performed
* (4) "Collision" includes collision with fixed objects, mobile objects, curb, etc.
* (5) None of the HMI controls should be relied on for real-time or time-critical controls. Risk of touching wrong control, bumps, no tactile feedback, etc. Monitor should use E-Stop when disengagement is needed for safety reasons, not HMI touchscreen button to disengage
* (6) Rain will obscure/interfere with cameras on roof--no wipers for cameras
* (7) Cameras will be less reliable in low light. Proper illumination needed to reliably detect obstacles, path, etc. May want test operation at night with strong oncoming high beams
* (8) Need to verify if windshield washers can spray on camera box/lidar and obscure their vision
* (11) Can be hazardous because steering will abruptly return to center position. Can also be hazardous because EPAS torque assist setting may abruptly change from dataspeed setting of 0 speed (parking lot assist level) to a different assist level for current speed
* (12) Potential hazard from allowing both copilot and montior to cancel E-Stop: automation could be enabled without the other person being aware or ready. Copilot should E-stop button to confirm readiness for automated control. Need to minimize time vehicle is in state (E-stop=normal, Apollo disabled) to minimize mode confusion. These criteria would be satisfied by: (1) verbal agreement by CP and Mon to engage autonomous mode (2) CP puts vehicle in known safe state and maneuvers vehicle to known safe starting location (3) Mon resets Apollo (4) CP cancels E-Stop (power dataspeed) (5) Mon activates Apollo. 
* (13) It is not known whether Apollo automatically shifts from P to D when autonomy mode is engaged, it is not known what Apollo's response will be to this action.
* (15) No documentation provided about this command or it's effect on system. Assume worst case: providing this command at any time has potential to interfere with autonomous operations
