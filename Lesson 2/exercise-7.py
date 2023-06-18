hour = int(input('Starting time (hours): '))
mins = int(input('Starting time (minutes): '))
dura = int(input('Event duration (minutes): '))

if not (0 <= hour <= 23):
    print('You entered not true hours!')
elif not (0 <= mins <= 59):
    print('You entered not true minutes!')
elif dura < 0:
    print('You entered not true duration!')
else:
    delta_hours = dura // 60
    hours = hour + delta_hours
    delta_mins = dura % 60
    minutes = mins + delta_mins
    if minutes > 60:
        hours = hours + 1
        minutes = minutes - 60
    if hours >= 24:
        hours = hours - 24

    print(f'Start at {hour}:{mins}, duration {dura} minutes, end at {hours}:{minutes}.')
