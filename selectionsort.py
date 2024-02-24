import random

def generate_random_numbers(n, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(n)]

arr=[]
arr = generate_random_numbers(1000, 1, 1000)
random.shuffle(arr)
print(arr)

def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
                     
        arr[i], arr[min_idx] = arr[min_idx], arr[i]



selectionSort(arr)

print("\n Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")