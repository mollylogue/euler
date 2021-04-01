#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def get_prime_factorization(n):
	prime_factors = dict()
	current = n
	if is_prime(n):
		prime_factors[n] = 1
		return prime_factors
	for i in range(2, n):
		if current % i == 0 and is_prime(i):
			prime_factors[i] = 0
			while True:
				if current % i == 0:
					current = current / i
					prime_factors[i] += 1
				else:
					break
	return prime_factors

def is_prime(p):
	for i in range(2, p):
		if p % i == 0:
			return False
	return True
				
def merge_prime_factor_maps(main_map, map_to_merge):
	for k, v in map_to_merge.iteritems():
		if k not in main_map:
			main_map[k] = v
		elif main_map[k] < v:
			main_map[k] = v
	return main_map

def multiply_prime_factors(prime_factors_map):
	product = 1
	for k, v in prime_factors_map.iteritems():
		product *= k ** v
	return product

def main():
	prime_factors = dict()
	for n in range(1, 20):
		prime_factors_for_n = get_prime_factorization(n)
		prime_factors = merge_prime_factor_maps(prime_factors, prime_factors_for_n)

	product = multiply_prime_factors(prime_factors)
	print 'product', product

	# Previous solution: (worked for 10, slow and inefficient for 20)
	#my_number = 20
	#current = 20
	#while True:
	#	if current % 1000000 == 0:
	#		print "current", current
	#	does_work = True
	#	for i in range(1, my_number):
	#		if current % i != 0:
	#			does_work = False
	#			break
	#	if does_work:
	#		print "Smallest number divisible by every number 1 to 20:", current
	#		break
	#	current += 1

if __name__ == '__main__':
	main()
