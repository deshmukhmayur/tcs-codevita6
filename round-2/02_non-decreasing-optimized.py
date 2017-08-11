"""
Numbers with non-decreasing digits
"""


def rearrange(n=0):
    """
    Rearranging the digits in largest increasing order
    greater than n
    """
    global i
    i += 1
    # print('iter', i, n)
    if n < len(digits) - 1:
        # print(i)

        if digits[n] <= digits[n + 1]:
            rearrange(n + 1)
        else:
            digits[n] = str(int(digits[n]) - 1)
            # print(n, digits)
            j = n - 1
            while j >= 0 and digits[j] > digits[n]:
                # print(j, digits, n)
                digits[j] = str(int(digits[j]) - 1)
                # print(j, digits, n)
                j -= 1

            digits[j + 2:] = ['9'] * len(digits[j + 2:])
            # print(digits)
            rearrange(n + 1)


if __name__ == '__main__':
    N = int(input().strip())
    digits = list(str(N))
    i = -1

    if digits == sorted(digits):
        print(int(''.join(digits)))
    else:
        rearrange()
        print(int(''.join(digits)))
