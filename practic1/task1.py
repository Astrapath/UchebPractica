def count(j, s):
    jewel = set(j)
    count = sum(1 for stone in s if stone in jewel)
    return count
j = 'ab'
s = 'aabbccd'
print(count(j, s))