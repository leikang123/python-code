maze = [
    [1,1,1,1,1,0,0,0,01,0,1,0,1],
    [0,0,0,0,0,0,01,1,1,0,1,1],
    [1,1,1,1,1,1,1,1,0,0,0,0,0,1]
    [0,0,0,0,0,0,0,0,01,1,1,1,0,1]
]  
for a in maze:
    for i in a:
        print('%4d' % i, end='')
    print()