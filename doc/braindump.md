
# Endstops and autoleveling probe

Endstops are cheap, but a specialized part. It would be great if we could reproduce them.
Using a conductive filament (like ProtoPasta Conductive), one could create traces which
can be connected together. In PLA one could design a spring which would separate the traces.

TODO: 

* Do research of existing work on reprappable endstops/switches
* Do reserch on suitable spring designs
* Design and print a prototype
* Test repeatability


On a 3d-printer could use mechanical switches/endstops as an autoleveling probe.
The problem however is that the switch cannot be lower than the nozzle when running
- it will interfere with printing.

* Have an endstop on two sides of the nozzle, some millimeters higher than nozzle
* Each corner of the build plate, has an elevated area (a bit).
* When running autoleveling, head moves such that the switch is above each of the areas before moving down.
* The hit-targets in the corners can also be the clamps for the glass-plate
* Note: requires careful calibration of build size area
* If repping endstops is cheap enough, can be achieved easily using min+max stops.
* Another advantage is that one can use a printed piece with correct offset
to autolevel also ontop of objects (like a CNC mill)

# Coating 

Using coats of an epoxy-like binder as an alternative to tape.
Can both provide structural stength, binding individual parts and getting a slick/hard sliding surface

* [How to measure friction](http://www.tribology-abc.com/abc/friction.htm)
* [Understanding Polyurethane Friction](https://www.slideshare.net/SunrayInc/understanding-polyurethane-coefficient-of-friction).
Harder -> lower friction.
Wet Polyurethane COF `<0.3` against stainless steel, and `<0.7` when dry.
Wood against dry Polyurethane `<0.2` for 75D hardness.
* [Testing coating hardness using pencil method](http://www.woodweb.com/knowledge_base/Testing_Your_Coatings_Hardness.html)
* Durometer. [1](https://www.amazon.com/MegaBrand-Durometer-Digital-Hardness-Tester/dp/B011JCG1KK)


# Reprappable laser

Using Rishalaser/TapeXY as a base.
Focusing first on ultra-low cost for use with textiles & paper,
with long-term goal of having high enough power to cut itself and similar structures.

## Milestone 1: Simplified mechanics (DONE)

* CoreXY architecture.
* Using string (Nylon) instead of belts
* Tape (Kapton/Scotch) slide-bearings
* See [TapeXY](../README.md#TapeXY)

## Milestone 2: Raster firmware (in progress)

* Couple open source alternatives available

## Milestone 3: 

* CNC-millable PCB with discrete H-bridges & microcontroller
* Firmware runs directly on this microcontroller

## Milestone 4: Fabbable motors

* Either brusless with gearing and closed-loop, or a direct-drive stepper
* 3d-printed or lasercut bobbins and structure
* Etched

## Milestone 5: Custom CO2 laser tubes

* See [Kreatures work](http://hackaday.com/2015/09/13/building-a-3d-printed-laser-tube/)
* If one can get them up to 20+ watt, should be able to reproduce
