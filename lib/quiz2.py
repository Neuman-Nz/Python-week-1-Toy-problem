def digit_sum(Number):
#Function to calculate the sum of digits of a number
    total = 0
    while Number:
        total += Number % 10
        Number //= 10
    return total

def solution(A):
    max_sum = -1

#Iterate through all pairs of numbers in the array
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            sum1 = digit_sum(A[i])
            sum2 = digit_sum(A[j])

#If the sums of digits are equal, update max_sum if needed
            if sum1 == sum2:
                max_sum = max(max_sum, A[i] + A[j])

    return max_sum

print(solution([42, 33, 60]))