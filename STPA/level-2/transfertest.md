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
