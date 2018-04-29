
## Tapecore @ LGM2017 - Plotting along openly

https://github.com/jonnor/tapecore

## Goals
- Understand the TapeCore project.
Motivation, construction principles, current state
- Understand basics of digital fabrication.

## Non-goals
- Learn to build machine

## Format

1. Demo
2. Talk, some background
3. Hands-on usage

## About me

Contract

    Twitter: @jononor
    Github: jonnor
    Web: https:/jonnor.com

Background

    BEng. Electronics 
    Software Engineer: Embedded, Open Source
    (ex) Bike mechanic

    Libre Graphics 2009-2014. MyPaint,OpenRaster,
    Maker community. 2014-< . Bitraf & Fellesverkstedet
    
Dayjob

    Independent consultant. Internet of Things. Rapid prototyping. SW/E.eng/M.Eng 
    MSc. Data Science. Machine learning

## TapeCore

- LOW cost
- LOW tech
- OK performance. Sub-millimeter precision

Fabricatable in makerspace/fablab 

- Few speciality tools
Lasercut + 3d-printed.
- Few speciality parts.
Instead: Digital fabricated and generic consumables.
Tape (Kapton/UHWMPE), Wire/fishing line.

### Handy A4

Designed in FreeCAD

[Bill of Materials](
https://docs.google.com/spreadsheets/d/1o2K1h2c_w2d49ZTSx7vD1f-7HGYju6wTmgCQS48S1lg)

Why penplotters

GRBL controller
https://github.com/gnea/grbl



## Review

Good

- Portable
- Open bottom frame

Needs work

- Backlash in Y axis. Replace split rail with individual rails 
- Glue needed for gantry slider.
- Diagonal stiffness too low
- Too many screws


## Fabricatable machines

https://github.com/fellesverkstedet/fabricatable-machines

- Medium to high-end machines
- CNCed Aluminum/POM
- Chamfer rail
- Humprey: Full-size CNC
- FAB2.0 - build a Fablab in a Fablab


## Digital fabrication

### Concept

    Digital 3d-model + digitally controlled fabrication machine
    => automated production of
       software-defined physical objects

In practice:

- Manual labor needed.
Postprocessing, machine tending
- Craft involved.
Design-for-manufacturing, technology choice, choosing machine parameters

### Where is this taking us?

- Less human labor needed
Cheaper products. Fewer jobs
- Less manual skills needed
Beginners can get good results also.
- Mass-production
Automated, easy to scale up
- Mass-customization
Each part can be unique 

### Democratization

Ensure the benefits are widely distributed instead of going to a selected few.

* Shared public access.
Maker/hackerspaces, Fablabs
* Open online manufacturing services.
Ponoko,3d-hubs,Shapeways,iMaterialize
* Open source hardware.
Reprap project, Prusa i3
* Open source software.
 Grbl, Marlin
* Consumer market.
Low prices, OK volume.
Makers as early adopters

### Process

Generally

    CAD -> CAM -> MC

    CAD: Computer-Aided Design
    CAM: Computer-aided Manufacturing
    MC: Machine Control


Example Plotting:

    Inkscape -> Inkscape gcodetools -> OctoPrint 

Example LaserCutting:

    FreeCAD -> AutoLaser -> Control panel on Redsail

Example generative code

    Python script generates

Why these divisions?

- Legacy: In instrustry often separate personell for each role
- CAD: Best software depends on what to design.
- CAM/MC: Depends on technology

### Languages


https://www.shapeoko.com/wiki/index.php/G-Code
http://reprap.org/wiki/G-code

Alternative for penplotters: HPGL

```
PU100,100
PD200,200
```
Often in 1/64th inch etc


## Machine

Open loop. Dead reckoning

