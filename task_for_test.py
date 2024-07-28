# Task is create free_time list[dicts] and split by 30 min

busy = [
    {
        'start': '10:30',
        'finish': '10:50'
    },
    {
        'start': '18:40',
        'finish': '18:50'
    },
    {
        'start': '14:40',
        'finish': '15:50'
    },
    {
        'start': '16:40',
        'finish': '17:20'
    },
    {
        'start': '20:05',
        'finish': '20:20'
    }
]


def from_hm_to_m(hm: str) -> int:
    h, m = [int(x) for x in hm.split(':')]
    return h * 60 + m


def from_m_to_hm(m: int) -> str:
    h = str(m // 60)
    m = str(m % 60)
    h = h if len(h) == 2 else '0' + h
    m = m if len(m) == 2 else '0' + m
    return f'{h}:{m}'


busy_intervals = []
for elem in busy:
    busy_intervals.append([
        from_hm_to_m(elem['start']),
        from_hm_to_m(elem['finish'])])
busy_intervals.sort()
# print(busy_intervals)

free_intervals = [[0, 1440]]
for busy_interval in busy_intervals:
    for index, free_interval in enumerate(free_intervals.copy()):
        if (busy_interval[0] > free_interval[0] and
                busy_interval[1] < free_interval[1]):
            free_intervals.insert(index + 1, [busy_interval[1], free_interval[1]])
            free_intervals[index][1] = busy_interval[0]

# print(free_intervals)


def create_30_m_interval(interval: list, minutes = 30):
    if interval[0] + minutes < interval[1]:
        return (
            [interval[0], interval[0] + minutes],
            *create_30_m_interval([interval[0] + minutes, interval[1]])
        )
    else:
        return [interval]


free_interval_by_m = []
for free_interval in free_intervals:
    free_interval_by_m = [*free_interval_by_m, *create_30_m_interval(free_interval)]


result = []
for free_interval in free_interval_by_m:
    result.append({
        'start': from_m_to_hm(free_interval[0]),
        'finish': from_m_to_hm(free_interval[1])
    })

print(result)
