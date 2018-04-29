import sys
import os
import re

def parse_command(line):
    pieces = line.split(' ')
    parsed = {}
    for p in pieces:
        if not p:
            continue

        kind,data = p[0],p[1:]
        data = re.compile(r"\(.*").sub('', data)
        if not data:
            continue

        if kind == 'G':
            parsed[kind] = int(data)
        else:
            parsed[kind] = float(data)

    return parsed

known_parameters = ['G', 'M', 'P', 'S', 'X', 'Y', 'Z', 'I', 'J', 'F']
def serialize_command(command):
    pieces = []
    for parameter in known_parameters:
        val = command.get(parameter)
        if val is not None:
            pieces.append("{}{}".format(parameter, val))

    unknown_parameters = set(command.keys()) - set(known_parameters)
    for parameter in unknown_parameters:
        val = command.get(parameter)
        if val is not None:
            pieces.append("{}{}".format(parameter, val))        

    return ' '.join(pieces)


def postprocess(gcode):
    last_z = None
    epsilon = 0.0001

    out = []
    for line in gcode.split('\n'):
        c = parse_command(line)

        Z = c.get('Z')
        if Z is not None:
            change_z = last_z is None or abs(c['Z']-last_z) > epsilon
            if change_z:
                servo = 'M3 S0' if Z > 0.0 else 'M3 S40'
                out.append(servo)
                last_z = c['Z']

            del c['Z']

        if set(c.keys()) != set(['G']):
            out.append(serialize_command(c))

    return '\n'.join(out)    

inp = """
G00 Z0.300000
G00 X154.889190 Y56.379210

G01 Z-0.125000 F100.0(Penetrate)
G03 X152.742534 Y56.025041 Z-0.125000 I0.000000 J-6.682640 F400.000000
G03 X154.889190 Y56.379210 Z-0.125000 I-2.160392 J-6.368966
G01 X154.889190 Y56.379210 Z-0.125000
G00 Z0.300000
"""

out = """
G00 X154.889190 Y56.379210

G01 F100.0
G03 X152.742534 Y56.025041 I0.000000 J-6.682640 F400.000000
G03 X154.889190 Y56.379210 I-2.160392 J-6.368966
G01 X154.889190 Y56.379210
G00 Z0.300000
"""

def test_first():
    o = postprocess(inp)
    print('o', o)
    assert o == out

def main():
    path = sys.argv[1]
    with open(path, 'r') as f:
        gcode = f.read()
        out = postprocess(gcode)
        sys.stdout.write(out)

if __name__ == '__main__':
    main()
   
