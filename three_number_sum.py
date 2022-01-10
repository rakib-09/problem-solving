def threeNumberSum(array, targetSum):
    array.sort()
    res = []
    for key, first_val in enumerate(array):
        left = key + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[key] + array[left] + array[right]
            if current_sum == targetSum:
                res.append([array[key], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < targetSum:
                left += 1
            elif current_sum > targetSum:
                right -= 1
    print(res)
