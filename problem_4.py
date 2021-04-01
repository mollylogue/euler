#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def main():
	largest_palindrome = 1
	for n in range(100, 999):
		for m in range(100, 999):
			to_check = n * m
			if is_palindrome(to_check):
				if to_check > largest_palindrome:
					largest_palindrome = to_check

	print 'Largest palindrome: ', largest_palindrome

def is_palindrome(number):
	number_as_string = str(number)
	for i in range(len(number_as_string)/2):
		if number_as_string[i] != number_as_string[len(number_as_string) - i -1]:
			return False
	return True

if __name__ == '__main__':
	main()
