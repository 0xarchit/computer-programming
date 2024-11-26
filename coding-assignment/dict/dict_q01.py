# Find the frequency of each distinct element in the list using a Python dictionary.

def CountFrequency(my_list):
	freq = {}
	for item in my_list:
		if (item in freq):
			freq[item] += 1
		else:
			freq[item] = 1

	for key, value in freq.items():
		print(f"{key} : {value}")
my_list = [int(x) for x in input("Enter the list elements separated by space: ").split()]
CountFrequency(my_list)
