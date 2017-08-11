'''
Numbers with non-decreasing digits
'''

N = int(input().strip())
i = N
while i > 0:
    digits = list(str(i))
    if digits == sorted(digits):
        print(i)
        break
    i -= 1
else:
    print(i)
