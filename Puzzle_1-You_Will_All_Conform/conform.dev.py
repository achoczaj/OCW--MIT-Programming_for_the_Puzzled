# MIT 6.S095 - Programming for the Puzzled - Srini Devadas
# Puzzle 1 - You Will All Conform

# Input is a vector of F's and B's, in terms of forwards and backwards caps.
# Output is a set of commands (printed out) to get either all F's or all B's.
# Fewest commands are the goal.

caps1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B',
        'B', 'B', 'F', 'F', 'B', 'F' ]
caps2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B',
        'B', 'B', 'F', 'F', 'F', 'F' ]

def pleaseConform(caps):
    # Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []

    # Determine intervals where caps are on in the same direction
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, orientation = F/B)
            intervals.append((start, i - 1, caps[start]))

            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i

    # Add the last interval after for loop completes execution
    intervals.append((start, len(caps) - 1, caps[start]))
    if caps[start] == 'F':
        forward += 1
    else:
        backward += 1

    print ('---------------')
    print ('Caps case vector = ', caps)
    print ('Intervals tuple = ', intervals)
    print ('Intervals number = ', len(intervals))
    print ()
    print ('Forward intervals = ', forward)
    print ('Backward intervals = ', backward)
    print ('---------------')
    
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for interval in intervals:
        if interval[2] == flip:
            #Exercise: if interval[0] == interval[1] change the printing!
            print ('People in positions', interval[0],
                   'through', interval[1], 'flip your caps!')


pleaseConform(caps1)
pleaseConform(caps2)
