# PHASE-3 WEEK 1 TOY PROBLEM

# PROBLEM STATEMENT (Number 1):
<p>You are given N boxes (numbered from 0 to N−1) arranged in a row. Each box contains a certain number of bricks. In one move, you can take one brick from some box and move it to a neighboring box (either to the left or to the right). The goal is to end up with exactly 10 bricks in every box.</p>

<p>Write a function solution(A) where A is an array of integers representing the number of bricks in each box. The function should return the minimum number of moves needed to achieve the goal. If it's not possible to end up with exactly 10 bricks in every box, the function should return -1.</p>

# Example
<ul>print(solution([7, 15, 10, 8]))  
print(solution([11, 10, 8, 12, 8, 10, 11]))  
print(solution([7, 14, 10])) </ul>

# APPROACH SOLUTION
<ol>Calculate the total number of bricks.
Check if it's possible to evenly distribute the bricks to each box to get 10 bricks in every box. If not, return -1.
Calculate the target number of bricks per box.
Iterate through each box:
If there are more bricks than the target, add the difference to the total moves.
If there are fewer bricks than the target, subtract the difference from the total moves.
Return the total moves.</ol>

# PROBLEM STATEMENT (Number 2):
<p>Given an array A consisting of N integers, find the maximum sum of two numbers whose digits add up to an equal sum. If there are no two numbers whose digits have an equal sum, return -1.</p>

## Example Usage:
<ul>print(solution([51, 71, 17, 42])) 
print(solution([42, 33, 60]))       
print(solution([51, 32, 43]))</ul>     


# APPROACH SOLUTION:
<ol>Define a helper function to calculate the sum of digits of a number.
Iterate through each pair of numbers in the array.
Check if the sums of the digits of the two numbers are equal.
Keep track of the maximum sum encountered.
Return the maximum sum found, or -1 if no such pair exists.</ol>

# Time Complexity:
The time complexity of this solution is O(N^2), where N is the number of elements in the array.

# PROBLEM STATEMENT (Number 3):
<p>Given an integer N, generate a string of length N containing as many different lowercase letters ('a' to 'z') as possible, where each letter occurs an equal number of times.</p>

# Example:
<ol>print(generate_string(3))  
print(generate_string(5))   
print(generate_string(30)) 
</ol>

# APPROACH SOLUTION:
<ol>Iterate through the alphabet ('a' to 'z').
Calculate the number of times each letter should be repeated based on the integer division of N by 26 (the number of lowercase letters in the alphabet) and the remainder.
Generate the string with repeated letters accordingly.
Return the generated string.</ol>

# Time Complexity:
The time complexity of this solution is O(N), where N is the length of the output string.

# AURTHOR: NEUMAN WALALA


