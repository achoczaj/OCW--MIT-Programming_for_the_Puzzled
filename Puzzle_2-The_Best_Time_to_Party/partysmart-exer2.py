# MIT 6.S095 - Programming for the Puzzled - Srini Devadas
# Puzzle 2 - The Best Time to Party

# Given a list of intervals when celebrities will be at the party
# Output is the time that you want to go the party when the maximum number of
# celebrities are still there.

# Clever algorithm that will work with fractional times

# Exercise 3: There is an alternative way of computing the best time 
# to party that does not depend on the granularity of time. 
# We choose each celebrity interval in turn, 
# and determine how many other celebrity intervals 
# contain the chosen celebrity’s start time. 
# We pick the time to attend the party to be the start time of the celebrity 
# whose start time is contained in the maximum number of other celebrity intervals. 
# Code this algorithm and verify that it produces the same answer 
# as the algorithm based on sorting.
 
sched1 = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
            (9, 10), (10, 11), (10, 12), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
          (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]

def bestTimeToPartySmart(schedule):
    #Convert schedule to list of start times and end times marked as such
    intervals = []
    for c in schedule:
        intervals.append(('interval', c[0], c[1]))
    
    print (intervals)
    
    # Sort the list of times.
    #Each time is a start or end time of a celebrity sighting.
    #sortlist(times)
    #print ('Sorted', times)


    #maxweight, maxcount, time = chooseTime(times)


    #Output best time to party
#    print ('Best time to attend the party is at', time,\
#          'o\'clock', ':', maxcount, 'celebrities will be attending!')
    

#Sort the elements of tlist in ascending order
#Sorting is based on the value of the first item of the element tuple
def sortlist(tlist):
    
    for index in range(len(tlist)-1):
        ismall = index
        for i in range(index, len(tlist)):
            #Sort based on first item of tuple
            if tlist[ismall][0] > tlist[i][0]:
                ismall = i
        #Swap the positions of the elements at index and ismall indices
        tlist[index], tlist[ismall] = tlist[ismall], tlist[index]
    
    return


def chooseTime(times):
    
    rcount = 0  # running count of celebrities
    rweight = 0 # running weight
    maxcount = 0  # max count of celebrities
    maxweight = 0
    besttime = 0
    
    # Range through the times computing a running count of celebrities
    
    for t in times:
                       
          if t[1] == 'start':
            rcount = rcount + 1
            rweight = rweight + int(t[2])
          elif t[1] == 'end':
            rcount = rcount - 1
            rweight = rweight - int(t[2])
               
        # Find max count of celebrities and best time
             
          if rweight > maxweight :
            maxweight = rweight
            maxcount = rcount
            besttime = t[0]
            
    return maxweight, maxcount, besttime

##bestTimeToPartySmart(sched)
bestTimeToPartySmart(sched2)