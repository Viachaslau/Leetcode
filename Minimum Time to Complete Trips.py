
time = [5,10,10]
totalTrips = 9
time.sort()
countTrip = 0
min_time = time[0]-1
while countTrip < totalTrips:
    min_time += 1
    for i in time:
        if min_time // i >= 1 and min_time % i == 0:
            countTrip += 1
            if countTrip >= totalTrips:
                break
            else:
                continue
        else:
            continue 
print(countTrip)
print(min_time)

