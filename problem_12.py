import math

def main():
	current = 0
	to_add = 1
	while True:
		current = current + to_add
		divisors = get_divisors(current)
		if len(divisors) > 500:
			print 'divisors', len(divisors), len(set(divisors))
			print 'number:', current
			break
		to_add += 1

def get_divisors(n):
	divisors = []
	for d in range(1, int(math.sqrt(n)+1)):
		if n % d == 0:
			divisors.append(d)
			if n/d != d:
				divisors.append(n/d)
	return divisors


if __name__ == '__main__':
	main()
