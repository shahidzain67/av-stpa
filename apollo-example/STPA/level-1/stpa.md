# Control Diagram

![Level 1 Control Diagram](./level1DotDiagram/level1-control-diagram.png)

# Unsafe Control Actions (UCAs)

## Apollo

<table>
  <tr>
    <th>Control Action</th>
    <th>Not Providing</th>
    <th>Providing</th>
    <th>Too Early / Too Late / Out of Order</th>
    <th>Stopped Too Soon / Applied Too Long</th>
  </tr>

  <tr>
    <td>Brake</td>
    <td class="Not Providing">
      UCA-6.1: Apollo does not provide the brake control action when relative velocity and distance to an obstacle mean that a collision is imminent. [H-2]<br><br>
      UCA-6.2: Apollo does not provide the brake control action when vehicle speed exceeds limits for controllability and stability of upcoming manoeuvrer. [H-1, H-2, H-3, H-6]<br><br>
      UCA-6.3: Apollo does not provide the brake control action when the vehicle is stationary and vehicle path is not clear. [H-1, H-2, H-3]<br><br>
      UCA-6.4: Apollo does not provide the brake control action when the vehicle has reached the final destination. <br><br>
      UCA-6.5: Apollo does not provide the brake control action when velocity exceeds speed limit, traffic flow limit, or planned test limit.
    </td>
    <td class="Providing">    
      UCA-6.6: Apollo provides brake control action with insufficient amount of braking below the minimum amount needed to avert a forward collision.<br><br>
      UCA-6.7: Apollo provides brake control action when vehicle speed does not exceed limits (speed limit, traffic flow limit, manoeuvrer limit, planned test limit, etc.) and there is no obstacle. <br><br>
      UCA-6.8: Apollo provides brake control action when driver is providing throttle.<br><br>
      UCA-6.9: Apollo provides excessive brake control action when wheel lock has occurred [H-1, H-2] (rationale: ABS may not work below 5mph)<br><br>
      UCA-6.10: Apollo provides brake control action with insufficient amount of braking to reduce vehicle speed within the limits for controllability and stability of upcoming manoeuvrer. <br><br>
      UCA-6.11: Apollo provides brake control action that is excessive beyond the physical limit of the passengers. <br><br>
      UCA-6.12: Apollo provides brake control action when autonomous driving is not active (off, standby, overriden, or e-stop). <br><br>
      UCA-6.13: Apollo provides emergency stop when a moving vehicle is in close proximity to the rear and forward collision is not imminent. [H-2]<br><br>
      UCA-6.14: Apollo provides emergency stop when in a location where stopping is never appropriate, and forward collision is not imminent. [H-1, H-2]
    </td>
    <td class="Too Early / Too Late / Out of Order">
      UCA-6.15: Apollo provides brake control action too late (> TBD sec) after relative velocity and distance to an obstacle mean that a collision is imminent [H-2]<br><br>
      UCA-6.16: Apollo provides brake control action too late (> TBD seconds) prior to manoeuvre. [H-1, H-2]<br><br>
      UCA-6.17: Apollo provides brake control action too late (> TBD sec) before upcoming manoeuvre's speed limit for controllability and stability is exceeded. <br><br>
      UCA-6.18: Apollo provides brake control action with too early timing that is outside of the time range when the signal is expected at the recipient (msg rate too high)<br><br>
      UCA-6.19: Apollo provides brake control action with too late timing that is outside of the time range specified for when the signal is supposed to arrive at the recipient (msg rate too low)
    </td>
    <td class="Stopped Too Soon / Applied Too Long">
      UCA-6.20: Apollo removes brake control action too early when relative velocity and distance to an obstacle mean that a collision will occur. [H-2]<br><br>
      UCA-6.21: Apollo removes brake control action too early (> TBD seconds) prior to/during  manoeuvre. [H-1, H-2]<br><br>
      UCA-6.22: Apollo stops brake control action before (< TBD seconds) vehicle slows to target speed (speed limit, traffic flow limit, maneuver limit, planned test limit, etc.). [H-1, H-2, H-3]<br><br>
      UCA-6.23: Apollo stops brake control action too soon at end of test before driver has resumed control (e.g. manual braking)
    </td>
  </tr>

</table>
