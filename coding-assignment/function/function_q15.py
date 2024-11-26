# function to find the median of a list

def find_median(lst):
    sorted_list = sorted(lst)
    n = len(sorted_list)
    if n % 2 == 1:
        return sorted_list[n // 2]
    else:
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2