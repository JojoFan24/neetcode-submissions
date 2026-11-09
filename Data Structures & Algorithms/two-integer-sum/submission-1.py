class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_map = {}
        for i in range(len(nums)):
            remainder = (target - nums[i])
            if remainder in nums_map.keys():
                return [nums_map[remainder], i]
            else:
                nums_map[nums[i]] = i

        return [0,0]



        