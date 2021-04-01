def main():
	sum_of_squares = 0
	square_of_sums = 0
	for n in range(101):
		sum_of_squares += n ** 2
		square_of_sums += n
	square_of_sums = square_of_sums ** 2
	print 'square of sums', square_of_sums
	print 'sum of squares', sum_of_squares
	print 'difference: ', square_of_sums - sum_of_squares

if __name__ == '__main__':
	main()
