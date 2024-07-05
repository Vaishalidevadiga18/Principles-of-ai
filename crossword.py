# Python program for the above approach

# Ways to calculate the number of
# Possible ways to fill the grid
ways = 0

# This function is used to print
# The resultant matrix
def printMatrix(matrix, n):
	for i in range(n):
		print(matrix[i])

# This function checks for the current word
# If it can be placed horizontally or not
# x -> it represent index of row
# y -> it represent index of column
# currentWord -> it represent the
# Current word in word array
def checkHorizontal(x, y, matrix, currentWord):
	n = len(currentWord)

	for i in range(n):
		if matrix[x][y + i] == '#' or matrix[x][y + i] == currentWord[i]:
			matrix[x] = matrix[x][:y + i] + currentWord[i] + matrix[x][y + i + 1:]
		else:
			
			# This shows that word cannot
			# Be placed horizontally
			matrix[0] = "@"
			return matrix
	return matrix

# This function checks for the current word
# If it can be placed vertically or not
# x -> it represent index of row
# y -> it represent index of column
# currentWord -> it represent the
# Current word in word array
def checkVertical(x, y, matrix, currentWord):
	n = len(currentWord)

	for i in range(n):
		if matrix[x + i][y] == '#' or matrix[x + i][y] == currentWord[i]:
			matrix[x + i] = matrix[x + i][:y] + currentWord[i] + matrix[x + i][y + 1:]
		else:
			
			# This shows that word
			# Cannot be placed vertically
			matrix[0] = "@"
			return matrix
	return matrix

# This function recursively checks for every
# Word that can align vertically in one loop
# And in another loop it checks for those words
# That can align horizontally words -> it
# Contains all the words to fill in a crossword
# Puzzle matrix -> it contain the current
# State of crossword index -> it represent
# The index of current word n -> it represent
# The length of row or column of the square matrix
def solvePuzzle(words, matrix, index, n):
	global ways
	if index < len(words):
		currentWord = words[index]
		maxLen = n - len(currentWord)
		
		# Loop to check the words that can align vertically.
		for i in range(n):
			for j in range(maxLen + 1):
				temp = checkVertical(j, i, matrix.copy(), currentWord)
				if temp[0] != "@":
					solvePuzzle(words, temp, index + 1, n)
		
		# Loop to check the words that can align horizontally.
		for i in range(n):
			for j in range(maxLen + 1):
				temp = checkHorizontal(i, j, matrix.copy(), currentWord)
				if temp[0] != "@":
					solvePuzzle(words, temp, index + 1, n)
	else:
		
		# Calling of print function to
		# Print the crossword puzzle
		print(str(ways + 1) + " way to solve the puzzle ")
		printMatrix(matrix, n)
		print()
		
		# Increase the ways
		ways += 1
		return

# Driver Code
if __name__ == '__main__':
	# Length of grid
	n1 = 10
	
	# Matrix to hold the grid of puzzle
	matrix = []
	
	# Take input of puzzle in matrix
	# Input of grid of size n1 x n1
	matrix.append("*#********")
	matrix.append("*#********")
	matrix.append("*#****#***")
	matrix.append("*##***##**")
	matrix.append("*#****#***")
	matrix.append("*#****#***")
	matrix.append("*#****#***")
	matrix.append("*#*######*")
	matrix.append("*#********")
	matrix.append("***#######")

	words = []
	
	# The words matrix will hold all
	# The words need to be filled in the grid
	words.append("PUNJAB")
	words.append("JHARKHAND")
	words.append("MIZORAM")
	words.append("MUMBAI")
	
	
	# Initialize the number of ways
	# To solve the puzzle to zero
	ways = 0
	
	
	# Recursive function to solve the puzzle
	# Here 0 is the initial index of words array
	# n1 is length of grid
	solvePuzzle(words, matrix, 0, n1)
	print("Number of ways to fill the grid is " + str(ways))
