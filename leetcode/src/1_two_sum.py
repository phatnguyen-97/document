from typing import List


class Solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        enumerate_list = enumerate(nums)
        for index, ele in enumerate_list:
            difference = target - ele
            # Check if the difference is already in the dictionary
            if difference in dict:
                # If it is, return the indices of the two numbers
                return [dict[difference], index]
            dict[ele] = index
        return []


list_elements = [0, 2, 4, 7, 12, 3, 9, 6, 11]
target = 9
solution = Solution()
solution.twosum(nums=list_elements, target=target)
