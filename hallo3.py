def difference(total):
    element_sum = sum(total)
    digit_sum = 0

    for num in total:
        while num > 0:
            digit = num % 10
            digit_sum = digit_sum + digit
            num = num // 10

    return abs(element_sum - digit_sum)


print(difference([1, 15, 6, 3]))
print(difference([1, 2, 3, 4]))

# print(difference([11, 12, 13, 14]))