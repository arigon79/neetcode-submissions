class TimeMap:

    def __init__(self):
        self.timeMap = {}

    # O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append([value, timestamp])
        else:
            self.timeMap[key] = [[value, timestamp]]
        print(self.timeMap)
    # O(logn)
    def get(self, key: str, timestamp: int) -> str:
        res = ''
        values = self.timeMap.get(key, [])
        if not values:
            return res
        l, r = 0, len(values) - 1

        while l <= r:
            m = l + (r - l) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
