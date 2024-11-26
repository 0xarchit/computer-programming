# program to generate number and its cube in dictionary

n = int(input())
cubes = {x: x**3 for x in range(1, n + 1)}
print(cubes)