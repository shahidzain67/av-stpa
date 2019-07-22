<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-88nc{font-weight:bold;border-color:inherit;text-align:center}
.tg .tg-1syg{font-weight:bold;font-size:16px;border-color:inherit;text-align:center}
.tg .tg-hysb{font-weight:bold;font-size:12px;text-align:left}
.tg .tg-qv16{font-weight:bold;font-size:16px;text-align:center;vertical-align:top}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-jlrw{font-size:16px;text-align:center}
.tg .tg-qnmb{font-weight:bold;font-size:16px;text-align:center}
.tg .tg-xldj{border-color:inherit;text-align:left}
.tg .tg-s268{text-align:left}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-1syg" rowspan="2">UCA</th>
    <th class="tg-1syg" colspan="3">basic scenario #1<br></th>
    <th class="tg-qnmb">basic scenario #2</th>
    <th class="tg-jlrw" colspan="2"><span style="font-weight:bold">basic scenario #3</span></th>
    <th class="tg-qv16" colspan="2">basic scenario #4</th>
  </tr>
  <tr>
    <td class="tg-hysb">&gt; physical failure</td>
    <td class="tg-hysb">&gt; inadequate control algorithm<br> a) flawed implementation<br> b) control algorithm is flawed<br> c) control algorithm becomes inadequate</td>
    <td class="tg-hysb">&gt; unsafe control or other inputs</td>
    <td class="tg-hysb">&gt; inadequate process model<br> a) incorrect feedback<br> b) interprets the feedback wrong<br> c) not received when needed <br>  c1) sent+not received<br>  c2) not sent+received<br> d) feedback does not exist</td>
    <td class="tg-hysb">&gt; control action not executed adequately<br> a) sent+not received<br> b) received+no response<br> c) response not received by process</td>
    <td class="tg-hysb">&gt; control action improperly executed<br> a) sent+received improperly<br> b) received+respond inadequately<br> c) respond adequately+received improperly by process<br> d) not sent+respond as if sent</td>
    <td class="tg-hysb">&gt; process: control action not executed adequately<br> a) applied but process does not respond</td>
    <td class="tg-hysb">&gt; process: improperly executed<br> a) received but process responds improperly<br> b)  not received but responds as if</td>
  </tr>
  <tr>
    <td class="tg-88nc" rowspan="2">SD does not provide Estop when a manual override is not effective </td>
    <td class="tg-xldj" colspan="3"># SD does not provide Estop <br># feedback indicates that manual override is not effective</td>
    <td class="tg-s268"># Manual override is not effective<br># feedback to SD indicates manual override is effective</td>
    <td class="tg-s268" colspan="2"># SD provides Estop<br># Estop is not executed</td>
    <td class="tg-s268" colspan="2"># SD provides Estop and Estop is executed<br># vehicle still follows commands by autonomous SW</td>
  </tr>
  <tr>
    <td class="tg-0pky">SD is distracted/blacked out/in a state of shock/surprise/etc.</td>
    <td class="tg-0pky">The SD does not know Estop has to be provided when manual override is not effective<br>  a) … Inaccurate information was spread during driver training, e.g.: <br>   # that the Safety Driver 2 does never have to provide an E-Stop command and only Safety Driver 1 does)<br>   # that Estop should only be provided in emergency situations when a collision is imminent<br>   # that an Estop triggers a hold on the vehicle that can only be removed by a maintenance station and therefore the SD is hesitant to use the Estop<br>  b) ... Safety Driver was taught to press a different button to trigger E-Stop during training (e.g. button relocated, etc.)<br> b) ... Estop button (with respective layout) was used to replace a button for a different function during assembly and was never replaced so SD presses the Estop button but gets a different function<br> b) ... SD was taught to only press the E-Stop button after being instructed by Safety Driver 1 and SD1 does not give that instruction (e.g. does not remember, was never taught to do so, etc.)<br> c) ... the SD's (internal) model of how to operate the vehicle or the SD's responsibiliities have changed  <br>     ... SD was taught to press the E-Stop button only for a short period of time which was correct at the time of training. However, later SW changes require the button to be pressed for more than x seconds to trigger E-Stop<br>     ... from the experiences the SD had when driving the autonomous vehicle it has often proved to be more useful to not provide an Estop and just to prevent a stronger (more percentage) override<br></td>
    <td class="tg-0pky">In order to test the limits of the autonomous software (and maybe the necessity of Estop) the SD were told not to make use of Estop at all<br><br>SD were told not to make use of E-Stop during testing when there is attention by the press</td>
    <td class="tg-0lax">The SD do not know the manual override is not effective.<br> a) ... SD receives feedback that manual override was effective when in fact it was not (e.g. rpm indicator shows increasing/decreasing rpm)<br> b) ... SD receives correct feedback that manual override was not effective (e.g. throttle stays constant) but mistakes other cockpit indicator (e.g. speed) as throttle feedback (e.g. because driver is overwhelmed, "uniform" cockpit design that makes it hard to distinguish gauges, etc.) <br> c1) ... SD does not receive feedback on effectiveness of manual override because communication line is blocked (e.g. EMI, bus busy, etc.)<br> c2) ... SD receives outdated feedback that manual override was effective (e.g. feedback delayed in transmission, etc.)<br> d) ... there is no feedback on the effectiveness of manual overrides foreseen in the system design (e.g. SD believes autonomy was disabled due to manual braking cmds…)</td>
    <td class="tg-0lax">SD provides Estop but power to autonomy modules is not cut off<br> a) … Estop command is sent but never arrives at Estop trigger (e.g. transmission unstable due to power interrupts, EMI, etc.)<br> b) … Estop command is received but Estop is not triggered (e.g. trigger fails closed, trigger linked to wrong precondition, etc.)<br> c) ... Estop command is sent, received, and power cut off is triggered but autonomous modules are still supplied by power (e.g. backup batteries, alternative power supply, internal energy storage, etc.)</td>
    <td class="tg-0lax">None<br></td>
    <td class="tg-0lax">SD provides Estop but vehicle nevertheless follows commands by autonomous software<br> a) … autonomy software modules are cut off from their main source of power but vehicle still follows autonomy commands, e.g. because:<br>  # there is an alternative source of power<br>  # commands by autonomy have been sent already and queued at the actuators</td>
    <td class="tg-0lax">None</td>
  </tr>
  <tr>
    <td class="tg-c3ow"></td>
    <td class="tg-0pky"></td>
    <td class="tg-c3ow"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
</table>