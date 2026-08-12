class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = math.floor(len(nums) / 3)
        print(length)

        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        res = []

        for key, val in count.items():
            print(key, val)
            print(length)
            if val > length:
                print("adding key:", key)
                res.append(key)
        
        return res

        

        