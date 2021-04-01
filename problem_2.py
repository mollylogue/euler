#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def main():
	maximum = 4000000
	previous1 = 0
	previous2 = 1
	even_total = 0
	while True:
		current = previous1 + previous2
		previous1 = previous2
		previous2 = current
		if current > maximum:
			break
		if current % 2 == 0:
			even_total += current
	print 'total: ', even_total	

if __name__ == '__main__':
	main()
