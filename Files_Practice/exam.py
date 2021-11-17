num = int(input("enter a number: "))
numbers = []
while num != 0:
	numbers.append(num)
	num = int(input("enter a number: "))
if len(numbers) != 0:
	for i in numbers:
		if numbers.count(i) > 1:
			print(f"value {i} appear {numbers.count(i)} times")

