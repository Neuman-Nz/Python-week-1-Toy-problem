def solution(A):
    N = len(A)
    total_moves = 0
    
 # Calculate the total number of bricks in the array
    total_bricks = sum(A)
    
    target_bricks = 10 * N
    
 # Check if it's possible to distribute bricks evenly
    if total_bricks % N != 0:
        return -1
 # Iterate through the boxes and calculate the moves needed to reach the target 
    for i in range(N):
        diff = A[i] - 10
        if diff > 0:
            
            total_moves += diff
            A[i] -= diff
            if i < N - 1:
                A[i + 1] += diff
            else:
                A[i - 1] += diff
        elif diff < 0:
            
            total_moves -= diff
            A[i] -= diff
            if i < N -1:
                A[i + 1] += diff
            else:
                A[i - 1] += diff
                
    if all(brick == 10 for brick in A):
        return total_moves
    else:
        return -1
    
    
print(solution([7, 14, 10]))
                
   