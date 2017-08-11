'''
Prime Numbers spelt with prime number of letters
'''

WORDS = {
    1: 'ONE',
    2: 'TWO',
    3: 'THREE',
    4: 'FOUR',
    5: 'FIVE',
    6: 'SIX',
    7: 'SEVEN',
    8: 'EIGHT',
    9: 'NINE',
    0: '',
    10: 'TEN',
    11: 'ELEVEN',
    12: 'TWELVE',
    13: 'THIRTEEN',
    14: 'FOURTEEN',
    15: 'FIFTEEN',
    16: 'SIXTEEN',
    17: 'SEVENTEEN',
    18: 'EIGHTEEN',
    19: 'NINETEEN'
}
TENS = {
    1: 'TEN',
    2: 'TWENTY',
    3: 'THIRTY',
    4: 'FORTY',
    5: 'FIFTY',
    6: 'SIXTY',
    7: 'SEVENTY',
    8: 'EIGHTY',
    9: 'NINETY'
}


def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes


def isPrimeWords(n):
    '''
    Generate words for the given input number
    '''
    ans = ''
    l = 0

    def twoDigitNums(n):
        if n != '':
            # print('n', n)
            if int(n) > 19:
                return TENS[int(n[0])] + WORDS[int(n[1])]
            else:
                return WORDS[int(n)]
        return ''

    if len(n) < 5:
        n = '0' * (5 - len(n)) + n

    tens, h, th = n[-2:], n[-3], n[:-3]

    thousands = twoDigitNums(th)
    if thousands != '':
        ans += thousands + 'THOUSAND'

    hundreds = WORDS[int(h)]
    if hundreds != '':
        ans += hundreds + 'HUNDRED'

    units = twoDigitNums(tens)
    if units != '':
        if ans != '':
            ans += 'AND' + units
        else:
            ans += units

    # print(ans, len(ans))
    if len(ans) in PRIMES:
        return True
    return False


if __name__ == '__main__':
    N1, N2 = [int(x.strip()) for x in input().strip().split()]

    PRIMES = get_primes(N2)

    count = 0
    for num in range(N1, N2 + 1):
        if num in PRIMES:
            if isPrimeWords(str(num)):
                count += 1

    print(count)
