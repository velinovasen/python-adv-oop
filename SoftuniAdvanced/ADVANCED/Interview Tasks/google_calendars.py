import time
calendar_one = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
boundary_one = ['9:00', '20:00']
calendar_two = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
boundary_two = ['10:00', '18:30']
'''
['10:30', '12:00'], ['13:00', '16:00'], ['18:00', '20:00']
['11:30', '12:30'], ['15:00', '16:00'], ['17:00', '18:30']
'''
free_times_first = []
free_times_second = []
final_times = []
for x in range(len(calendar_one)):
    if x == 0:
        if calendar_one[x][0] != boundary_one[0]:
            free_times_first.append([boundary_one[0], calendar_one[x][0]])
    if len(calendar_one) - x > 1:
        if calendar_one[x][1] != calendar_one[x + 1][0]:
            free_times_first.append([calendar_one[x][1], calendar_one[x + 1][0]])
    if len(calendar_one) - x == 1:
        if calendar_one[x][1] != boundary_one[1]:
            free_times_first.append([calendar_one[x][1], boundary_one[1]])

for x in range(len(calendar_two)):
    if x == 0:
        if calendar_two[x][0] != boundary_two[0]:
            free_times_second.append([boundary_two[0], calendar_two[x][0]])
    if len(calendar_two) - x > 1:
        if calendar_two[x][1] != calendar_two[x + 1][0]:
            free_times_second.append([calendar_two[x][1], calendar_two[x + 1][0]])
    if len(calendar_two) - x == 1:
        if calendar_two[x][1] != boundary_one[1]:
            free_times_second.append([calendar_two[x][1], boundary_two[1]])

if len(free_times_first) > len(free_times_second):
    time_check = len(free_times_first)
else:
    time_check = len(free_times_second)

for x in range(time_check):
    start_time = ''
    end_time = ''
    if time.strptime(free_times_first[x][0], '%H:%M') >= time.strptime(free_times_second[x][0], '%H:%M'):
        start_time = free_times_first[x][0]
    else:
        start_time = free_times_second[x][0]
    if time.strptime(free_times_first[x][1], '%H:%M') <= time.strptime(free_times_second[x][1], '%H:%M'):
        end_time = free_times_first[x][1]
    else:
        end_time = free_times_second[x][1]

    final_times.append([start_time, end_time])

print(final_times)