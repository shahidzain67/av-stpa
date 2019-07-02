Title: Checks on HMI actions

# Checks on HMI actions

Presented here are preliminary results of the investigation to determine if HMI actions can lead to unsafe conditions. The actions headers below have so far been investigated.

The point of this is to determine if an unsafe condition (invalid map, etc) can come about through the e.g. the user changing a destination or a map file whilst the car is driving in auto mode.

## Driving Mode

- Whilst numerous driving modes are available, currently only full auto and manual are selectable from the HMI. (refer to line 231 of modules/dreamview/backend/hmi/hmi.cc)
- The driving mode can be altered while in automatic mode.

## Routing request

- In terms of the HMI, a routing request can be sent without reference to the the current state of the vehicle automation operation.
- There are no checks on the source of a routing request in OnRoutingRequest. No check is made on the state of the vehicle.
  - In principle, this may not matter, because the start point of a new route will always be the vehicle's current position.

## Change Map

- The map directory may be changed in the HMI without reference to the driving mode.
- the map is specified in terms of a directory, the base map always has a standard file name or it will not be found - as in **hdmap_util.cc** the function BaseMapFile() is used to supply the file name
- the CreateMap() function pulls in all kinds of map data (positions of lanes, traffic lights, speed bumps, etc) into a structure, and returns a pointer to that structure
- the BaseMapPtr() function locks a mutex and then calls CreateMap(), thus returning a pointer to the map structure. It is not clear that the mutex is ever used.
- New map data is **does not** autmatically picked up by the planning module just because the base directory has changed.
- It seems that the map is loaded to routing, planning and perception upon initialisation
  - this takes the form: hdmap_ = apollo::hdmap::HDMapUtil::BaseMapPtr();
- therefore, a new map will not be available to the Apollo modules until they are cycled on and off
- _however, there may still exist the possibility that the map visible in the HMI will be inconsistent with the one loaded in the other modules, which could lead to incorrect, but not necessarilly unsafe, waypoints being set TBD_

## HMI control of Apollo Software Modules

- The ModuleController of dreamview/frontend/src/components is responsible for taking action when the module checkboxes are ticked
  - onClick={() => { this.props.store.hmi.toggleModule(key)}}
- toggleModule(id) of hmi.js then (amonst other things) calls
  - WS.executeModuleCommand(id, command) ... with command = 'start' or 'stop'
- executeModuleCommand in turn sends the command to the websocket
  - which lands in websocket.cc of the back end...
- is handled via

    websocket_->RegisterMessageHandler(
      "ExecuteModuleCommand",
      [this](const Json &json, WebSocketHandler::Connection *conn) {

- which calls RunComponentCommand(config_.modules(), module, command);
  - this is in hmc.cc (int HMI::RunComponentCommand(_args_)
- which, finally, calls: const int ret = std::system(cmd->c_str());
- because the commands that are sent here are sent by the HMI backend, they are listed out in:
  - dreamview/conf/HMI.conf

## Level of HMI control

We conclude that the HMI can run any command that

- a) the HMI frontend has some mechanism to pass to the websocket so it can by handled by the relevant socket handler by the backend
- b) a handler exists to handle it in the backend
- c) can be returned by config_.modules(), which will depend on the the relevant .conf file, in this case HMI.conf

**The HMI is capable of starting or stopping any Apollo module, because the conditions above are fulfilled. This could lead to unsafe driving conditions, and / or the software monitor invoking an emergency stop due to a FATAL error.**
