def moveElementToEnd(array, toMove):
    i = 0  # find out toMove
    j = len(array) - 1  # find out different numbers

    while i < j:
        if array[i] == toMove and array[j] != toMove:
            array[i] = array[j]
            array[j] = toMove
            i += 1
            j -= 1
        elif (array[i] == toMove and array[j] == toMove) or (array[i] != toMove and array[j] == toMove):
            j -= 1
        elif array[i] != toMove and array[j] != toMove:
            i += 1
    return array


class Solution:
    def moveZeroes(self, array) -> None:
        i = 0  # find out 0
        j = 0  # find out different numbers

        while j < len(array) and i < len(array):
            print(array[i], array[j])
            if array[i] == 0 and array[j] != 0:
                array[i] = array[j]
                array[j] = 0
                i += 1
            elif array[i] != 0:
                i += 1
            j += 1
        return array