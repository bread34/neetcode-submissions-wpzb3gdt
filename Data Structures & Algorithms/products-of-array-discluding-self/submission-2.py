class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      r=[]
      def s(x): return __import__("math").prod(x)
      for i in range(len(nums)):
        x=nums[i]
        nums[i]=1
        r.append(s(nums))
        nums[i]=x
      return r