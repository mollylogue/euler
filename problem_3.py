#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def main():
	my_number = 600851475143
	current = 1
	print 'find largest prime factor for', my_number
	n = 0
	while True:
		n+=1
		if my_number % n == 0:
			if is_prime(n):
				current = current * n
				if current == my_number:
					print 'largest prime factor:', n
					break


def is_prime(n):
	for i in range(2, n/2):
		if n % i == 0:
			return False
	return True


if __name__ == '__main__':
	main()
