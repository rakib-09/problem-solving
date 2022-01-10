def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    runner_array = arrayOne if len(arrayOne) > len(arrayTwo) else arrayTwo
