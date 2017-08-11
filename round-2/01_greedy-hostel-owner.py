'''
Greedy Hostel Owner
'''

N = int(input().strip())
readings = [i for i in input().strip().split()]
central_reading = int(input())

HASH = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


def decode_reading(reading):
    '''
    Decodes the input string and returns the units consumed.
    '''
    unit = ''
    for i in range(len(reading)):
        # print(reading[i], HASH.index(reading[i]))
        digit = HASH.index(reading[i])

        if 4 < digit <= 9 and i < len(reading) - 1:
            if HASH.index(reading[i + 1]) == 9 - digit:
                unit += str(9 - digit)
            else:
                unit += str(digit)
        else:
            unit += str(digit)

    # print(unit)
    return unit


reading_sum = 0
for reading in readings:
    reading_sum += int(decode_reading(reading))

# if the sum of the individual readings is <= central reading
# the Owner is innocent
if reading_sum <= central_reading:
    print('INNOCENT')
else:
    print('GREEDY')
    print(abs(reading_sum - central_reading))
