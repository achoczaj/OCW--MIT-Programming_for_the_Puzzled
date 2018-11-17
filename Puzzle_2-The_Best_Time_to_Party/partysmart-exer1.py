# MIT 6.S095 - Programming for the Puzzled - Srini Devadas
# Puzzle 2 - The Best Time to Party

# Given a list of intervals when celebrities will be at the party
# Output is the time that you want to go the party when the maximum number of
# celebrities are still there.

# Clever algorithm that will work with fractional times

# Exercise 1: 
# Suppose you are yourself a busy celebrity 
# and don’t have complete freedom in choosing when you can go to the party.
# Add arguments to the procedure bestTimeToPartySmart 
# and modify it so it determines the maximum number of celebrities 
# you can see within a given time range between ystart and yend. 
# As with celebrities the interval is [ystart, yend]so you are available 
# at all times t such thatystart <= t < yend.


sched1 = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
            (9, 10), (10, 11), (10, 12), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
          (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]

ystart = (6.0, 'start')
yend = (10.0, 'end')

def bestTimeToPartySmart(schedule):
    #Convert schedule to list of start times and end times marked as such
    times = []
    for c in schedule:
        times.append((c[0], 'start'))
        times.append((c[1], 'end'))

    #times.append(ystart)
    #times.append(yend)

    print (times)
    #Sort the list of times.
    #Each time is a start or end time of a celebrity sighting.
    sortlist(times)
    print ('Sorted', times)
##    print times

    maxcount, time = chooseTime(times)


    #Output best time to party
    print ('Best time to attend the party is at', time,\
           'o\'clock', ':', maxcount, 'celebrities will be attending!')
    

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
    maxcount = 0  # max count of celebrities
    besttime = 0
    
    # Range through the times computing a running count of celebrities
    for t in times:
        
        # Limit the range to between ystart and yend.
        
        if t[0] >= ystart[0] and  t[0] < yend[0] :
        
          if t[1] == 'start':
            rcount = rcount + 1
          elif t[1] == 'end':
            rcount = rcount - 1
         
               
        # Find max count of celebrities and best time
             
          if rcount > maxcount:
            maxcount = rcount
            besttime = t[0]
            
    return maxcount, besttime

##bestTimeToPartySmart(sched)
bestTimeToPartySmart(sched2)