from collections import deque

nums_of_gas_stations = int(input())

gas_amount = deque([])
kilometres = deque([])
gas_tank = 0
distance_to_go = 0
for _ in range(nums_of_gas_stations):
    gas, distance = [int(x) for x in input().split()]
    gas_amount.append(gas)
    kilometres.append(distance)

for y in range(nums_of_gas_stations):
    valid = True
    gas_tank = gas_amount.popleft()
    distance_to_go = kilometres.popleft()
    if gas_tank >= distance_to_go:
        for x in range(y, len(kilometres)):
            gas_tank += gas_amount[y]
            distance_to_go += kilometres[y]
            if gas_tank < distance_to_go:
                valid = False
        if valid:
            print(y)
            break

    else:
        kilometres.append(distance_to_go)
        gas_amount.append(gas_tank)

if len(kilometres) == 0:
    print('0')


'''6. Truck Tour
Suppose there is a circle. There are N petrol pumps on that circle. Petrol pumps are numbered 0 to (N−1) (both inclusive). You have two pieces of information corresponding to each of the petrol pump: (1) the amount of petrol that petrol pump will give, and (2) the distance from that petrol pump to the next petrol pump (kilometers).
Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol pumps. Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop at each of the petrol pumps. The truck will move one kilometer for each liter of the petrol.
Input
The first line will contain the value of N
The next N lines will contain a pair of integers each, i.e. the amount of petrol that petrol pump will give and the distance between that petrol pump and the next petrol pump
Output
An integer which will be the smallest index of the petrol pump from which we can start the tour
Constraints
1 ≤ N ≤ 1000001
1 ≤ Amount of petrol, Distance ≤ 1000000000
Examples
Input	Output	Comments
3
1 5
10 3
3 4	1	
'''