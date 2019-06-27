# STPA for Autonomous Vehicles

The aim of this project is to develop a base set of safety requirements which will be widely applicable to autonomous vehicles.

The requirements are being derived using STPA (System-Theoretic Process Analysis), a systems approach to safety developed at MIT. The analysis is being done on an autonomous car which uses Apollo 2.0, an Open Source Autonomous Vehicle project, however the results are easily transferable to other autonomous vehicles.

All of the analysis is fully open, provided under the [MIT License](https://en.wikipedia.org/wiki/MIT_License). We are also open for contributors to the project. We fully believe that the best way to achieve safety is by open collaboration between as many parties as possible. To contribute, please see our contributing page.

This project is part of [Trustable](https://trustable.gitlab.io/).

**All work here is Work In Progress, and is published on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.**

<img src="./images/level-2-control-diagram.png" alt="Level 2 Control Diagram" width="80%"/>

## A Systems Approach to Safety

Software systems are becoming increasingly complicated, they are often in the order of millions of lines of code running on complex hardware platforms, and current safety standard techniques which focus on failure rates of individual components are ineffective. It is unachievable to test large software for every set of possible states. As well as this, regardless of failure rates, accidents can be caused by poor system design, where each component is acting exactly as designed. This project has found circumstances where even if nothing fails, and everything is acting entirely reasonably and as intended (hardware, software and humans), severe accidents are still possible due to the way these things interact with each other. It is clear that safety techniques are needed to improve the design process, so that complex systems can be analysed properly. System-Theoretic Process Analysis (STPA) is a systems approach to safety, developed at MIT. It allows us to look at the system as a whole, and abstract complexity by starting at a very high level using black boxes. We can then zoom into these black boxes and iterate the process through more and more detailed levels. Through STPA it is possible to develop a set of safety requirements which will determine the software architecture requirements.

## STPA

> STPA (System-Theoretic Process Analysis) is a relatively new hazard analysis technique based on an extended model of accident causation. In addition to component failures, STPA assumes that accidents can also be caused by unsafe interactions of system components, none of which may have failed.

The above is from the STPA handbook, which can be found [here](http://psas.scripts.mit.edu/home/materials/).

This repo contains a Work In Progress (WIP) STPA for an autonomous vehicle containing Apollo 2.0. Even though this is looking at a specific implementation of an autonomous vehicle, it is believed that the work done will be widely transferable.

## Apollo

[Apollo](http://apollo.auto/) is an Open Source Autonomous Vehicle project ([source code repository](https://github.com/ApolloAuto/apollo)), which provides a software platform for its partners to develop their own autonomous driving systems. It is made available by Baidu under the Apache 2.0 License.
