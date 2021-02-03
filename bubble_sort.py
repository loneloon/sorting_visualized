from visualizer import Visualizer
import random
import copy

display_visuals = True if input("Enable visuals? [Y/n]").lower() in "yes" else False

min_length = 200
max_length = 500
max_val = 600

input_array = list(random.randint(1, max_val) for i in range(random.randint(min_length, max_length)))


def bubble_sort(input_arr):

    array = copy.deepcopy(input_arr)

    z = 1
    while z < len(array):
        for i in range(len(array) - z):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

                if display_visuals:
                    motion.update_image(array, i)
        z += 1

    return array


if display_visuals:
    print("\nEnter your display resolution:")
    resolution = [int(input("Width: ")), int(input("Height: "))]

    motion = Visualizer(resolution[0], resolution[1], max_val, 0)
    motion.animation_loop(bubble_sort, input_array)

output_array = bubble_sort(input_array)
print("Unsorted input: %s" % input_array)
print("Sorted output: %s" % output_array)