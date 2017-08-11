'''
Digital Time 12
'''

if __name__ == '__main__':
    try:
        digits = [ int(x.strip()) for x in input().strip().split(',')]
        ans = ''
        # print(digits)
        if 1 in digits:
            digits.remove(1)
            # print(digits)
            ans += '1'
            for i in [2, 1, 0]:
                if i in digits and digits.count(0) >= 4:
                    ans += str(i)
                    digits.remove(i)
                    break
            else:
                # print('if 1 block')
                raise TypeError
        elif 0 in digits:
            digits.remove(0)
            m = max(digits)
            digits.remove(m)
            ans += '0' + str(m)
        else:
            # print('If 0 block')
            raise TypeError

        digits.sort()
        digits.reverse()
        for i in range(2):
            ans += ':'
            for num in digits:
                if num < 6:
                    ans += str(num)
                    digits.remove(num)
                    break
            else:
                # print('for %s block' % str(i))
                raise TypeError

            m = max(digits)
            ans += str(m)
            digits.remove(m)

        # 12:01:01
        if ans[:2] == '12' and ans[-5:] == '00:00':
            # TODO: Need to reform a new time
            raise TypeError
        elif ans == '00:00:00':
            raise TypeError
        print(ans)
    except TypeError:
        print('Impossible')