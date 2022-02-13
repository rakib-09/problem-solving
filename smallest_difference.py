def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    print(arrayOne, arrayTwo)
    i, j, f_a, s_a, lw = 0, 0, None, None, None
    while i < len(arrayOne) and j < len(arrayTwo):
        if arrayOne[i] < 0 and arrayTwo[j] < 0:
            diff = abs(abs(arrayOne[i]) - abs(arrayTwo[j]))
        else:
            diff = abs(arrayOne[i] - arrayTwo[j])
        if diff == 0:
            return [arrayOne[i], arrayTwo[j]]
        if lw is None or (diff < lw):
            lw = diff
            f_a = arrayOne[i]
            s_a = arrayTwo[j]
        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else:
            j += 1
    return [f_a, s_a]
