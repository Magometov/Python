duration = int(input('duration= '))
if duration < 60:
    print(duration, 'сек')

if 60 <= duration < 3600:
    minute = int(duration / 60)
    duration = duration - (minute * 60)
    print(minute, 'мин', duration, 'сек')

elif 3600 <= duration < (3600 * 24):
    hour = int(duration / 3600)
    minute = int((duration - (hour * 3600))) // 60
    duration = duration - ((hour * 3600) + minute * 60)
    print(hour, 'час', minute, 'мин', duration, 'сек')

elif duration >= (3600 * 24):
    day = int(duration / (3600 * 24))
    duration -= day * (3600 * 24)
    hour = int(duration / 3600)
    minute = int((duration - (hour * 3600))) // 60
    duration = duration - ((hour * 3600) + minute * 60)
    print(day, 'день', hour, 'час', minute, 'мин', duration, 'сек')
