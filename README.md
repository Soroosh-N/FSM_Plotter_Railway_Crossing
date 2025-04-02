# FSM Plotter for Railway Crossing Problem
In this code we provide an FSM (Finite State Machine) plotter for "Railway Crossing" problem using Python language.
## Introduction:
Railway crossings are a significant safety hazard for pedestrians and motor traffic. We implemented an FSM for a safety warning system to prevent crossings while a train is approaching and until it has passed.

## Problem Description:
There are two tracks, one going north and the other south. At the crossing, a roadway (for cars, pedestrians, baby strollers, etc.) intersects both tracks. There is an arm which lowers to block crossing and an audible alarm which warns against crossing. Trains on each track only run in one direction. The system has an audible alarm, and a barrier that is lowered to block the crossing. The crossing alarm and barrier are controlled with signals `alarm_enable`, `alarm_disable`, `barrier_lower`, and `barrier_raise`. You have a timer available which emits a clock event once per second if needed.

When a train is approaching, the alarm begins clanging.  After 10 seconds, the barrier lowers. The alarm continues to sound and the barrier remains lowered while a train is present. When no train is present the barrier raises, and after 10 seconds the alarm stops. Approach and depart events will always come in pairs (a train cannot depart without first approaching).

* Proximity sensors are placed on the tracks before and after the crossing.
* The sensors `northbound_approach` and `southbound_approach` emit a short pulse when the first car of the train crosses the sensor (leading edge).
* The sensors `northbound_depart` and `southbound_depart` emit a short pulse when the last car of the train crosses the sensor (trailing edge).
