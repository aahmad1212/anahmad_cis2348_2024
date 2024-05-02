# Adil Ahmad
# 2278219
# Global variable
num_calls = 0


# TODO: Write the partitioning algorithm - pick the middle element as the
#       pivot, compare the values using two index variables l and h (low and high),
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary
def partition(inplist, i, k):
    midp = i + (k - i) // 2
    piv = inplist[midp]

    done = False
    lo = i
    hi = k
    while not done:
        while inplist[lo] < piv:
            lo += 1
        while piv < inplist[hi]:
            hi -= 1
        if lo >= hi:
            done = True
        else:
            temp = inplist[lo]
            inplist[lo] = inplist[hi]
            inplist[hi] = temp
            lo += 1
            hi -= 1
    return hi


# TODO: Write the quicksort algorithm that recursively sorts the low and
#       high partitions. Add 1 to num_calls each time quicksort() is called
def quicksort(nums, i, k):
    global num_calls
    num_calls += 1
    j = 0
    if j:
        pass
    if i >= k:
        return
    j = partition(nums, i, k)
    quicksort(nums, i, j)
    quicksort(nums, j + 1, k)

    return


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
