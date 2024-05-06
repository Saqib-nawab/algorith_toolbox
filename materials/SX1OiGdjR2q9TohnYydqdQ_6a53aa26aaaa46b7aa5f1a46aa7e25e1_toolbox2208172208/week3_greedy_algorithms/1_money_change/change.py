# Python3 program to implement 
# the above approach 


def find_sequence(n): 

	# Base Case 
	if n == 1: 
		return 1, -1

	# Recursive Call for n-1 
	ans = (find_sequence(n - 1)[0] + 1, n - 1) 

	# Check if n is divisible by 2 
	if n % 2 == 0: 
		div_by_2 = find_sequence(n // 2) 

		if div_by_2[0] < ans[0]: 
			ans = (div_by_2[0] + 1, n // 2) 

	# Check if n is divisible by 3 
	if n % 3 == 0: 
		div_by_3 = find_sequence(n // 3) 

		if div_by_3[0] < ans[0]: 
			ans = (div_by_3[0] + 1, n // 3) 

	# Returns a tuple (a, b), where 
	# a: Minimum steps to obtain x from 1 
	# b: Previous number 
	return ans 

# Function that find the optimal 
# solution 
def find_solution(n): 
	a, b = find_sequence(n) 

	# Print the length 
	print(a) 

	sequence = [] 
	sequence.append(n) 

	# Exit condition for loop = -1 
	# when n has reached 1 
	while b != -1: 
		sequence.append(b) 
		_, b = find_sequence(b) 

	# Return the sequence 
	# in reverse order 
	return sequence[::-1] 

# Driver Code 

# Given N 
n = 99

# Function Call 
print(*find_solution(n)) 
