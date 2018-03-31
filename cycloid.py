import math

"""
Usage in FreeCAD

import sys
sys.path.insert(0, '/home/jon/projects/tapecore') # where to find cycloid.py script
import cycloid
C = cycloid.cycloid(3, steps=100)
P = list(FreeCAD.Vector(x, y, 0.0) for x, y in zip(C['x'], C['y']))
Draft.makeWire(P,closed=False,face=True,support=None)
"""

### TODO
# Create shape for one tooth only
# Repeat over by period/n_teeth
# Close the shape
# Fillet teeth tip

def cycloid_x(y, a=1.0):
    return a * math.acos(1.0 - (y/a)) - math.sqrt(2.0*a*y - y**2)

def cycloid_period(a, steps):    
    # first half
    yleft = list(i/(steps/2.0) for i in range(0, steps))
    xleft = list(cycloid_x(yleft[i], a) for i in range(0, steps))

    xmax = max(xleft)
    ymax = max(yleft)

    # second half
    yright = list(ymax - i/(steps/2.0) for i in range(0, steps))
    xright = list((xmax*2.0) - cycloid_x(yright[i], a) for i in range(0, steps))

    Y = yleft + yright
    x = xleft + xright

    # reflect across Y
    #Y = list(ymax - y for y in Y)

    return { 'x': x, 'y': Y, 'xmax': xmax, 'ymax': ymax }

def shifted(points, shift):
    return list(p + shift for p in points)
    
def cycloid(periods, a=1.0, steps=1000):
    points = { 'x': [], 'y': [] }
    period = cycloid_period(a, steps)
    for i in range(periods):
        x = shifted(period['x'], period['xmax']*2*i)
        points['x'] += x
        points['y'] += period['y']

    return points
