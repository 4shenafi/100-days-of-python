def add(*args):
    sum_of_nums = 0
    for num in args:
        sum_of_nums += num
    return sum_of_nums
print(add(1,2,3,4,5,6,7,8,9))