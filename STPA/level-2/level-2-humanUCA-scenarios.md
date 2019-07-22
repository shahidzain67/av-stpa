# Level 2 Human Unsafe Control Actions - Scenarios

<table class="table table-bordered">
  <tr>
    <th>UCA</th>
    <th>Basic Scenario #1 (Inadequate Controller Behavior) </th>
    <th>Basic Scenario #2 (Inadequate Feedback/Information) </th>
    <th>Basic Scenario #3 (Inadequate Control Execution) </th>
    <th>Basic Scenario #4 (Inadequate Process Behavior) </th>
  </tr>

  <tr>
    <td>SD does not provide E-Stop when a manual override is not effective.</td>
    <td class="Basic Scenario #1 (Inadequate Controller Behavior)">
	<b># SD does not provide Estop </b>
	<b># Feedback indicates that manual override is not effective </b>
	-----
      SD is distracted/blacked out/in a state of shock/surprise/etc. <br><br>
      The SD does not know Estop has to be provided when manual override is not effective <br><br>
		a) … Inaccurate information was spread during driver training, e.g.: <br><br>
			# that the Safety Driver 2 does never have to provide an E-Stop command and only Safety Driver 1 does) <br><br>
			# that Estop should only be provided in emergency situations when a collision is imminent <br><br>
			# that an Estop triggers a hold on the vehicle that can only be removed by a maintenance station and therefore the SD is hesitant to use the Estop <br><br>
		b) ... Safety Driver was taught to press a different button to trigger E-Stop during training (e.g. button relocated, etc.) <br><br>
		b) ... Estop button (with respective layout) was used to replace a button for a different function during assembly and was never replaced so SD presses the Estop button but gets a different function <br><br>
		b) ... SD was taught to only press the E-Stop button after being instructed by Safety Driver 1 and SD1 does not give that instruction (e.g. does not remember, was never taught to do so, etc.) <br><br>
		c) ... the SD's (internal) model of how to operate the vehicle or the SD's responsibiliities have changed <br><br>
			# SD was taught to press the E-Stop button only for a short period of time which was correct at the time of training. However, later SW changes require the button to be pressed for more than x seconds to trigger E-Stop<br><br>
			# from the experiences the SD had when driving the autonomous vehicle it has often proved to be more useful to not provide an Estop and just to prevent a stronger (more percentage) override <br><br>
	-----
		In order to test the limits of the autonomous software (and maybe the necessity of Estop) the SD were told not to make use of Estop at all <br><br>
		SD were told not to make use of E-Stop during testing when there is attention by the press <br><br>
	-----
		The SD do not know the manual override is not effective <br><br>
			a) ... SD receives feedback that manual override was effective when in fact it was not (e.g. rpm indicator shows increasing/decreasing rpm) <br><br>
			b) ... SD receives correct feedback that manual override was not effective (e.g. throttle stays constant) but mistakes other cockpit indicator (e.g. speed) as throttle feedback (e.g. because driver is overwhelmed, "uniform" cockpit design that makes it hard to distinguish gauges, etc.) <br><br>
			c1) ... SD does not receive feedback on effectiveness of manual override because communication line is blocked (e.g. EMI, bus busy, etc.) <br><br>
			c2) ... SD receives outdated feedback that manual override was effective (e.g. feedback delayed in transmission, etc.) <br><br>
			d) ... there is no feedback on the effectiveness of manual overrides foreseen in the system design (e.g. SD believes autonomy was disabled due to manual braking cmds…) <br><br>
    </td>
    <td class="Basic Scenario #2 (Inadequate Feedback/Information)">
	<b># Manual override is not effective </br>
	<b># Feedback to SD indicates manual override is effective </br>
	-----
		The SD do not know the manual override is not effective.
			a) ... SD receives feedback that manual override was effective when in fact it was not (e.g. rpm indicator shows increasing/decreasing rpm)
			b) ... SD receives correct feedback that manual override was not effective (e.g. throttle stays constant) but mistakes other cockpit indicator (e.g. speed) as throttle feedback (e.g. because driver is overwhelmed, "uniform" cockpit design that makes it hard to distinguish gauges, etc.) 
			c1) ... SD does not receive feedback on effectiveness of manual override because communication line is blocked (e.g. EMI, bus busy, etc.)
			c2) ... SD receives outdated feedback that manual override was effective (e.g. feedback delayed in transmission, etc.)
			d) ... there is no feedback on the effectiveness of manual overrides foreseen in the system design (e.g. SD believes autonomy was disabled due to manual braking cmds…)
    </td>
    <td class="Basic Scenario #3 (Inadequate Control Execution)">
	<b># SD provides Estop </b>
	<b># Estop is not executed </b>
	-----
		SD provides Estop but power to autonomy modules is not cut off <br><br>
			a) ... Estop command is sent but never arrives at Estop trigger (e.g. transmission unstable due to power interrupts, EMI, etc.) <br><br>
			b) ... Estop command is received but Estop is not triggered (e.g. trigger fails closed, trigger linked to wrong precondition, etc.) <br><br>
			c) ... Estop command is sent, received, and power cut off is triggered but autonomous modules are still supplied by power (e.g. backup batteries, alternative power supply, internal energy storage, etc.) <br><br>
    -----
		None
	</td>
    <td class="Basic Scenario #4 (Inadequate Process Behavior)">
	<b># SD provides Estop and Estop is executed </b>
	<b># vehicle still follows commands by autonomous SW </b>
	-----
		SD provides Estop but vehicle nevertheless follows commands by autonomous software
			a) … autonomy software modules are cut off from their main source of power but vehicle still follows autonomy commands, e.g. because:
				# there is an alternative source of power
				# commands by autonomy have been sent already and queued at the actuators 
	-----
		None
    </td>
  </tr>

</table>

* Note : Testnote
