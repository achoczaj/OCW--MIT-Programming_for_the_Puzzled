# MIT 6.S095 - Programming for the Puzzled - Srini Devadas
# Puzzle 2 - The Best Time to Party

# Given a list of intervals when celebrities will be at the party
# Output is the time that you want to go the party when the maximum number of
# celebrities are still there.
# Brute force algorithm implemented here

# Schedule - list of intervals when celebrities will be at the party (list of tuples)
sched1 = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
            (9, 10), (10, 11), (10, 12), (11, 12)]

def bestTimeToParty(schedule):
    # Inicialize start time and end time
    start = schedule[0][0] # the first entry of first tuple (start of 1st interval) 
    end = schedule[0][1]   # the secound entry of first tuple (end of 1st interval)
    
    # Find start time and end time
    for c in schedule:   # c = celebrity
        start = min(c[0], start)
        end = max(c[1], end)

    # Compute count of celebrities at each time between start and end
    count = celebrityDensity(schedule, start, end)
    
    print ('Start: ', start)
    print ('End: ', end)
    print ('Count of celebrities at each time', count)
    
    maxcount = 0
    # Range over times to find the time when the maximum celebrities are around.
    for i in range(start, end + 1):  # from start to end, inclusive
        if count[i] > maxcount:
            maxcount = count[i]
            time = i
    
    print ('Maxcount: ', maxcount)
    print ('Time: ', time)


##    maxcount = max(count[start:end + 1])  # from start to end, inclusive
##    time = count.index(maxcount)  # determine the index at which maximum element (maxcount) is found 

    #Output the best time to party.
    #Note that the \ means the statement continues on the next line.
    print ('Best time to attend the party is at', time,\
           'o\'clock', ':', maxcount, 'celebrities will be attending!')


def celebrityDensity(sched, start, end):

    # Initialize a list of length end + 1 to all 0's
    count = [0] * (end + 1) # use indexies of count as time
    # i ranges over different times
    for i in range(start, end + 1):
        count[i] = 0  # this line is not nessesary as all values are inicialized as 0 
        # c ranges over the celebrities
        for c in sched:
            # Check if celebrity c is around at time i
            if c[0] <= i and c[1] > i: # the time i must be >= c's start time and less than c's end time
                count[i] += 1
                
    return count
                

bestTimeToParty(sched1)       
 
                
            
        