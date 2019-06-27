Title: Emergency Mode

# 'Emergency Mode', Emergency Stop ('estop_'), Emergency Overide

These three functions allow a different kind of emergency functionality to take place

- Emergency mode: A problem with the hardware on the canbus leads to a return to manual control
- Emergency Stop: Software conditions have determined that the vehicle should be stopped
- Emergency Override: The vehicle occupant intercedes to override the controls - Dataspeed overrides the control output from Apollo.

## Emergency Mode

There exists within Apollo the ability to raise a flag called EMERGENCY_MODE. This flags a time measurement; if emergency mode stays active, **or becomes active again**, 10s after this initial time mark, then the vehicle will be returned to manual control.

### When Emergency Mode triggers are checked

The EMERGENCY_MODE flag is raised when CheckResponse() is repeatedly negative, which is checked when one of the following is called from **canbus/vehicle/lincoln/lincoln_controller.cc** :

_Upon mode change, (CheckResponse() checked 20 times in a row)_

- EnableAutoMode()
- EnableSteeringOnlyMode()
- EnableSpeedOnlyMode()

_Called on a watchdog thread-cyclic basis, fails more than kMaxFailAttempt times_

- SecurityDogThreadFunc()

### Conditions activating Emergency Mode

- If, for either of the following, no data is received or the function is reported off-line:
  - Electronic Power Steering (_when checking a steering-active mode_)
  - VCU (velocity control unit?) (_when checking a throttle-active mode_)
- Any of the following functions report a {watchdog, channel, calibration, connector} error via canbus
  - EPS
  - Brake
  - Throttle

### Results of activating Emergency mode

A program contained in **control/tools/terminal.cc** allows the HMI or 'PAD' to send the AUTO_DRIVE_COMMND and RESET_COMMAND. However, it has another function:

**When emergency mode is activated, the time is noted. 10s later the driving mode will be automatically reset to Manual. Provided the chassis data reports emergency mode, there is no way to manually override this feature.**

The human occupant must clearly be ready to take control after this period ends.

## Emergency Stop

The apparent primary purpose of **estop_** is to allow the planning module to signal that the vehicle should be brought to a stop rapidly.

### When Emergency Stop triggers are checked

The trigger flag from planning and the flag raising conditions are checked each time Controll::ProduceControlCommand is executed, which is essentially cyclically under automatic operation.

### Conditions activating Emergency Stop

Under non-fault operating conditions for the vehicle, emergency stop is activated by the planning module *(trajectory_.estop().is_estop() )*

The condition can be **also activated** by

- A 'FATAL' category message from the software Monitor module
- A status 'OK' response from CheckInput() was **not** received, which requires
  - localization has been observed *at some time*,
  - chassis data has been observed *at some time*,
  - trajectory data is available
- trajectory data is **not** within time-stamp tolerance
- A Control Command, based on the supplied inputs and trajectory, could not be computed

### Results of activating Emergency Stop

The code used, contained in **control/control.cc**, is

  control_command->set_speed(0);
  control_command->set_throttle(0);
  control_command->set_brake(control_conf_.soft_estop_brake());
  control_command->set_gear_location(Chassis::GEAR_DRIVE);

The conditional encapsulation of normal control functions in Control::ProduceControlCommand on line 151 means that no further control commands from the planning module will be obeyed until this condition is cleared.

The vehicle will be brought to a rapid halt. _It is significant that both Apollo fault and non-fault conditions can trigger this event_

### Deactivation of 'Emergency Stop'

PAD message DrivingAction::RESET will result in estop_ being cleared; it will also result in _fully manual_ control being assumed immediately.

## Emergency Override

In the context of Apollo, the emergency override is operated outside the Apollo software system. The nature of the Dataspeed override and its effects are documented elsewhere [_link to follow_].

So, in terms of the Apollo software:

- The Override is activated outside of the Apollo software
- The Override is deactivated outside of the Apollo software
- Although Apollo _parses_ the driver override bit that can be set by Dataspeed, we have not found, to date, a _use_ of this override bit in software.

## Summary

Whilst it is too early to conclude the consequences of the existance of these three operational functions, we can at least observe (using the abbreviation E=Emergency):

- The E-Stop, E-Mode, E-Override are activated by different conditions
- The E-Stop, E-Mode, and E-Override have different effects on the system
- The E-Stop, E-Mode, and E-Override operate _independently in software_ and interract through their control consequences for the vehicle.
