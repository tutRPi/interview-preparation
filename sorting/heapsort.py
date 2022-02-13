# Sample Data: [14,46,43,27,57,41,45,21,70]
# Expected Result : [14, 21, 27, 41, 43, 45, 46, 57, 70]

def build_max_heap(arr):
    for i in reversed(range(len(arr))):
        parent_index = int((i - 1) / 2)
        step_down(arr, parent_index, len(arr) - 1)


def step_down(arr, parent_index, max_index):
    left_child = 2 * parent_index + 1
    swap_index = parent_index
    if left_child <= max_index and arr[left_child] > arr[swap_index]:
        swap_index = left_child
    if left_child + 1 <= max_index and arr[left_child + 1] > arr[swap_index]:
        swap_index = left_child + 1
    if swap_index == parent_index:
        return
    else:
        # swap numbers
        arr[parent_index], arr[swap_index] = arr[swap_index], arr[parent_index]
        step_down(arr, swap_index, max_index)


def heapsort(arr):
    if len(arr) <= 1:
        return

    build_max_heap(arr)

    for n in reversed(range(len(arr))):
        arr[0], arr[n] = arr[n], arr[0]
        step_down(arr, 0, n-1)


x = [14, 46, 43, 27, 57, 41, 45, 21, 70]
heapsort(x)
assert x == [14, 21, 27, 41, 43, 45, 46, 57, 70]
