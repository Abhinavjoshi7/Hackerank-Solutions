import statistics
def average(array):
    # your code goes here
    set_arr = set(array)
    avg = 0
    avg = statistics.mean(set_arr)
    return avg

