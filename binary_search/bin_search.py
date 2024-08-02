def binary_search(array, target):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        center = (left + right) // 2
        if target == array[center]:
            return True
        elif target < array[center]:
            right = center - 1
        else:
            left = center + 1
    
    return False
        
def find_first_greater_or_equal(array, target):
    left = 0
    right = len(array)

    while left <= right - 1:
        center = (left + right) // 2
        if array[center] >= target:
            right = center
        else:
            left = center + 1

    return right

def find_first_greater(array, target):
    left = 0
    right = len(array)

    while left <= right - 1:
        center = (left + right) // 2
        if array[center] > target:
            right = center
        else:
            left = center + 1

    return right

n = int(input())
numbers = input().split()
numbers = [int(num) for num in numbers]

k = int(input())
requests = input().split()
requests = [int(req) for req in requests]


for request in requests:
    if binary_search(numbers, request):
        print(1, 
              find_first_greater_or_equal(numbers, request),
              find_first_greater(numbers, request))
    else:
        print(0, 
              find_first_greater_or_equal(numbers, request),
              find_first_greater(numbers, request))