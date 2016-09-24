def  movePlane(command):
    shift = 1
    (x, y) =(0, 0)
    ns = -1
    for i, c in enumerate(command):
        if c.isdigit():
            shift = int(c)
        elif c is 'D':
            y = y - shift
            shift = 1

        elif c is 'L':
            x = x - shift
            shift = 1

        elif c is 'U':
            y = y + shift
            shift = 1

        elif c is 'R':
            x = x + shift
            shift = 1

        elif c is 'X' :
            if i != 0:
                pc = command[i-1]
                if command[i-2] and command[i-2].isdigit():
                    ns = -int(command[i-2])

                (x, y) =move(pc, ns, x, y)
                ns = -1

        else:
            x, y = (999, 999)
    return str((x, y))

def move(c, shift, x, y):
    if c is 'D':
        y = y - shift

    elif c is 'L':
        x = x - shift

    elif c is 'U':
        y = y + shift

    elif c is 'R':
        x = x + shift
    else:
        x = 999
        y = 999
    return x, y

print(movePlane('7D3DX2D'))

print(movePlane('X'))

print(movePlane('7UXDX2D'))

print(movePlane('7UDX2D'))

print (movePlane('UDLL'))

print (movePlane('8D2L'))

print (movePlane('X4D2R'))
