import math
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.
def is_prime(n, list_of_primes):
	for p in list_of_primes:
		if n % p == 0:
			return False
	return True

def is_prime_2(p):
	for i in range(2, p):
		if p % i == 0:
			return False
	return True

def main():
	all_numbers_list = []
	for n in range(2000000):
		all_numbers_list.append(True)
	for i in range(0, int(math.sqrt(len(all_numbers_list)))+2):
		if all_numbers_list[i+2]:
			if i+2 == 509:
				print_stuff = True
			for j in range(0, len(all_numbers_list)):
				index = (i+2)**2 + (i+2)*j
				if index >= len(all_numbers_list):
					break
				all_numbers_list[index] = False

	primes = []
	prime_total = 0
	total_primes = 0
	for i in range(2, len(all_numbers_list)):
		if all_numbers_list[i]:
			total_primes +=1
			primes.append(i)
			prime_total += i
	print 'prime total', prime_total

if __name__ == '__main__':
	main()
