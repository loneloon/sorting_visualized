from visualizer import Visualizer
import random
import copy


display_visuals = True if input("Enable visuals? [Y/n]").lower() in "yes" else False

min_length = 200
max_length = 500
max_val = 600

input_array = list(random.randint(1, max_val) for i in range(random.randint(min_length, max_length)))


def insertion_sort(input_arr):

    array = copy.deepcopy(input_arr)

    for i in range(len(array)):
        j = i - 1
        while j >= 0 and array[j] > array[j+1]:
            array[j+1], array[j] = array[j], array[j+1]
            j -= 1

            if display_visuals:
                motion.update_image(array, j)

    return array


if display_visuals:
    motion = Visualizer(2560, 1080, max_val, 0)
    motion.animation_loop(insertion_sort, input_array)

output_array = insertion_sort(input_array)
print("Unsorted input: %s" % input_array)
print("Sorted output: %s" % output_array)
