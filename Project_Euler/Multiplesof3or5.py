def solution(limit):
    sum_of_multiples = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i
    return sum_of_multiples


limit = 1000
print(solution(limit))