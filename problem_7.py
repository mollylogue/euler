def main():
	number_of_primes = 10001
	current = 1
	n = 1
	while current <= number_of_primes:
		n += 1
		if is_prime(n):
			current += 1
	print 'n', n	

def is_prime(p):
	for i in range(2, p):
		if p % i == 0:
			return False
	return True

if __name__ == '__main__':
	main()
