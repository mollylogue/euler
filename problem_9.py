def main():
	for c in range(1, 1000):
		for a in range(1, c):
			b = 1000 - c - a
			if b < 0:
				break
			if check_is_pythagorean(a, b, c):
				print 'is pythagorean', a, b, c
				print 'product: ', a * b * c

def check_is_pythagorean(a, b, c):
	if a ** 2 + b ** 2 == c ** 2:
		return True
	return False

if __name__ == '__main__':
	main()
