def mergeOverlappingIntervals(intervals):
    intervals.sort()
    arr = []
    start = None
    end = None
    temp_end = None
    for i in range(len(intervals)):
        final = temp_end if (temp_end and temp_end >= intervals[i][1]) else intervals[i][1]
        if len(intervals) - 1 > i and final >= intervals[i + 1][0]:
            if start is None:
                start = intervals[i][0]
                temp_end = intervals[i][1]
        else:
            if start and end is None:
                end = intervals[i][1] if intervals[i][1] >= temp_end else temp_end
            if start is not None and end is not None:
                arr.append([start, end])
                start, end, temp_end = None, None, None
            else:
                arr.append(intervals[i])
    return arr
