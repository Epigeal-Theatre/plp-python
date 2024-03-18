def add_nums(*nums):
    sum = 0
    for x in nums:
        sum = sum + x
    return sum

total = add_nums(10,20,70)
print(total)
