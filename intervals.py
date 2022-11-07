import typing
import functools

def find_free_time(working_time: typing.List[typing.List[int]]):
    """

    merged_intervals = [[1, 2],[1, 3],[4, 5],[6, 8],[7, 8],[7, 10]]

    """
    def compare(interval1, interval2):
        if interval1[0] == interval2[0]:
            return interval1[1] - interval2[1]
        else:
            return interval1[0] - interval2[0]

    stack = []
    res = []
    merged_intervals = [interval for worker_time in working_time for interval in worker_time]
    merged_intervals.sort(key=functools.cmp_to_key(compare))

    for interval in merged_intervals:
        if stack and stack[-1][1] >= interval[0]:
            p_interval = stack.pop(-1)
            stack.append([p_interval[0], interval[1]])
        else:
            stack.append(interval)
        print(stack)
    
    for i in range(len(stack) - 1):
        res.append([stack[i][1], stack[i+1][0]])

    return res