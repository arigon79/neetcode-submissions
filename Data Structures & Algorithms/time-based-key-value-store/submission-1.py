class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [[value, timestamp]]
        else:
            self.timeMap[key].append([value, timestamp])
        print(self.timeMap)

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        values = self.timeMap.get(key, [])
        l = 0
        r = len(values) - 1

        while l <= r:
            mid = l + (r- l)//2
            
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res