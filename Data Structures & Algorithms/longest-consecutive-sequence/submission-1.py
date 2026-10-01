class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        x=set(nums)
        longest=1
        for i in x:
            if (i-1) not in x:
                current_num = i
                current_streak = 1
                while (current_num + 1) in x:
                    current_num += 1
                    current_streak += 1
                longest = max(longest, current_streak)
        return longest