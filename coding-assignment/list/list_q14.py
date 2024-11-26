# program to find all prime numbers in a list

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
prime_numbers = []
for num in lst:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
print("Prime numbers:", prime_numbers)