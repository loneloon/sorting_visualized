import random


def merge_sort(input_arr):

    if len(input_arr) > 0 and len(input_arr) // 2 >= 1:
        left_slice = merge_sort(input_arr[:len(input_arr)//2])
        right_slice = merge_sort(input_arr[len(input_arr)//2:])

        input_arr = []

        while left_slice and right_slice:
            if left_slice[0] < right_slice[0]:
                input_arr.append(left_slice.pop(0))
            else:
                input_arr.append(right_slice.pop(0))

        if left_slice:
            input_arr.extend(left_slice)
        else:
            input_arr.extend(right_slice)

    return input_arr


min_length = 100
max_length = 100

input_array = list(random.randint(1, 9) for i in range(random.randint(min_length, max_length)))
output_array = merge_sort(input_array)

print("Unsorted input: %s" % input_array)
print("Sorted output: %s" % output_array)
