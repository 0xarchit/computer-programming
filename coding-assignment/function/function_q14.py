# function to generate a multiplication table

def generate_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
generate_multiplication_table(10)