def arrayOfProducts(array):
    res = [1] * len(array)
    left, right = 1, 1
    for i in range(len(array)):
        res[i] = left
        left *= array[i]
    for i in reversed(range(len(array))):
        res[i] *= right
        right *= array[i]

    return res
