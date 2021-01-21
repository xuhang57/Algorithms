def count_1_bits(value):
	n = 0
	while value:
		value &= value - 1
		n += 1
	return n

def main():
	print(count_1_bits(1))
	print(count_1_bits(10))
	print(count_1_bits(131))

if __name__ == "__main__":
	 main()
