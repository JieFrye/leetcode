# Time Based Key-Value Store

# Create a timebased key-value store class TimeMap, that supports two operations.
#
# 1. set(string key, string value, int timestamp)
#
# Stores the key and value, along with the given timestamp.
# 2. get(string key, int timestamp)
#
# Returns a value such that set(key, value, timestamp_prev) was called
# previously, with timestamp_prev <= timestamp.
# If there are multiple such values, return value with the largest timestamp_prev.
# If there are no values, it returns the empty string ("").

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        '''
        ideas:
        use dic to hold {key: [(time, value)]}
        '''
        self.dic[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        '''
        ideas:
        use bisection to find idx instead of sort then loop
        The timestamps for all TimeMap.set operations are strictly increasing.
        '''
        arr = self.dic[key]
        n = len(arr)
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            if arr[mid][0] <= timestamp:
                low = mid + 1
            elif arr[mid][0] > timestamp:
                high = mid
        if high > 0: # high - 1 >= 0
            return arr[high-1][1]
        else:
            return ""




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
