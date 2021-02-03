from visualizer import Visualizer
import random


display_visuals = True if input("Enable visuals? [Y/n]").lower() in "yes" else False

min_length = 700
max_length = 1000
max_val = 600

input_array = list(random.randint(1, max_val) for i in range(random.randint(min_length, max_length)))


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        if display_visuals:
            motion.update_image(arr, i)

        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if display_visuals:
    print("\nEnter your display resolution:")
    resolution = [int(input("Width: ")), int(input("Height: "))]

    motion = Visualizer(resolution[0], resolution[1], max_val, 0)
    motion.animation_loop(heap_sort, input_array)


print("Unsorted input: %s" % input_array)
heap_sort(input_array)
print("Sorted output: %s" % input_array)
