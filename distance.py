def konvert_distance(a, b, c):
    distances = {
        'm': 1,
        'km': 1000,
        'au': 149597870700,
        'ly': 9460730472580800,
        'distancesc': 30856776000000000,
    }
    return a * distances[b] / distances[c]


print 'Please enter value'
amount = float(raw_input())
print 'First unit of measurement (m, km, au, ly, pc )'
measure1 = raw_input()
print 'Second unit of measurement (m, km, au, ly, pc )'
measure2 = raw_input()
print str(amount) + measure1 + ' = ' \
    + str(konvert_distance(amount, measure1, measure2)) + measure2
