# Apollo Inter-Process Communication

This document details the messages sent between modules in the Apollo 2.0 project.

Currently it is just a list of the adapter.conf receive and publish messages for each module.

## planning

* Receive
  - LOCALIZATION
  - CHASSIS
  - ROUTING_RESPONSE
  - PREDICTION
  - TRAFFIC_LIGHT_DETECTION
* Publish
  - ROUTING_REQUEST
  - PLANNING_TRAJECTORY

## planning/testdata

* Receive
  - LOCALIZATION
  - CHASSIS
  - ROUTING_RESPONSE
  - PREDICTION
  - TRAFFIC_LIGHT_DETECTION
* Publish
  - ROUTING_REQUEST
  - PLANNING_TRAJECTORY

## third_party_perception

* Receive
  - MOBILEYE
  - DELPHISER
  - LOCALIZATION
* Publish
  - PERCEPTION_OBSTACLES

## calibration/lidar_ex_checker

* Receive
  - POINT_CLOUD
  - GPS
  - INS_STAT

## calibration/republish_msg

* Receive
  - GPS
  - INS_STAT
* Publish
  - RELATIVE_ODOMETRY

## prediction

* Receive
  - PERCEPTION_OBSTACLES
  - LOCALIZATION
  - PLANNING_TRAJECTORY
* Publish
  - PREDICTION

## drivers/contri_radar

* Publish
  - CONTI_RADAR
  - MONITOR

## control

* Receive
  - LOCALIZATION
  - PAD
  - PLANNING_TRAJECTORY
  - CHASSIS
* Publish
  - CONTROL_COMMAND
* Duplex
  - MONITOR

## control/testdata

  * Receive
    - LOCALIZATION
    - PAD
    - PLANNING_TRAJECTORY
    - CHASSIS
  * Publish
    - CONTROL_COMMAND
  * Duplex
    - MONITOR

## control/testdata/control_tester

  * Receive
    - LOCALIZATION
    - PAD
    - PLANNING_TRAJECTORY
    - CHASSIS

## perception

* Receive
  - POINT_CLOUD
  - LOCALIZATION
  - CONTI_RADAR
  - IMAGE_SHORT
  - IMAGE_LONG
* Publish
  - PERCEPTION_OBSTACLES
  - TRAFFIC_LIGHT_DETECTION

## dreamview

* Receive
  - COMPRESSED_IMAGE
  - IMAGE_SHORT
  - PLANNING_TRAJECTORY
  - PERCEPTION_OBSTACLES
  - PREDICTION
  - SYSTEM_STATUS
  - TRAFFIC_LIGHT_DETECTION
* Publush
  - PAD
  - ROUTING_REQUEST
* Duplex
  - LOCALIZATION
  - CHASSIS
  - MONITOR
  - ROUTING_RESPONSE

## canbus

* Receive
  - CONTROL_COMMAND
* Publish
  - CHASSIS
  - CHASSIS_DETAIL
  - MONITOR

## routing

* Receive
  - ROUTING_REQUEST
* Publush
  - ROUTING_RESPONSE
* Duplex
  - MONITOR

## monitor

* Receive
  - GNSS_STATUS
  - INS_STATUS
  - POINT_CLOUD
  - IMAGE_LONG
  - IMAGE_SHORT
  - LOCALIZATION
  - PERCEPTION_OBSTACLES
  - PREDICTION
  - PLANNING_TRAJECTORY
  - CONTROL_COMMAND
  - CONTI_RADAR
* Publish
  - SYSTEM_STATUS
  - STATIC_INFO
  - MONITOR
