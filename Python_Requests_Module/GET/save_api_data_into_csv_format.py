def canWePlace(stalls,mid,k):
    n = len(stalls)
    cntcows = 1
    last = stalls[0]
    for i in range(1, n):
        if stalls[i] - last >= mid:
            cntcows += 1
            last = stalls[i]
        if cntcows >= k:
            return True
    return False


def aggressiveCows(stalls, k):
    # Write your code here.
    n = len(stalls)
    low = 1
    high = stalls[-1] - stalls[0]
    res = 0
    while low <= high:
        mid = (low+high) // 2
        if canWePlace(stalls,mid,k):
            res = mid
            low = mid + 1
        else:
            high = mid -1
    return res