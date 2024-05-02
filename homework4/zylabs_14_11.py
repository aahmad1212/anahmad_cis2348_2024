# Adil Ahmad
# 2278219
def selection_sort_descend_trace(x):
    for j, i in enumerate(x[:-1]):
        index_min = j
        for y in range(j + 1, len(x)):
            if x[y] > x[index_min]:
                index_min = y

        temp = x[j]
        x[j] = x[index_min]
        x[index_min] = temp
        for y in x:
            print(y, end=" ")
        print()


if __name__ == "__main__":
    inputs = input().split()
    input_list = [int(x) for x in inputs]
    selection_sort_descend_trace(input_list)
