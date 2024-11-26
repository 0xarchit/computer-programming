# function to check if a number is an Armstrong number

def is_armstrong(num):
    n = len(str(num))
    return num == sum(int(digit) ** n for digit in str(num))