class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      r=[]
      def s(x):
        y=1
        for i in range(len(x)):
            y=y*x[i]
        return y
      for i in range(len(nums)):
        x=nums[i]
        nums[i]=1
        r.append(s(nums))
        nums[i]=x
      return r