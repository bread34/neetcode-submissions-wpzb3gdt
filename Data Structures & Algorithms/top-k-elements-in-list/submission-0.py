class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t={}
        for i in range(len(nums)):
          #check the size as well
          if nums[i] in t:
            t[nums[i]]+=1
          else:
            t[nums[i]]=1
        t=[(j,i) for i,j in t.items()]
        t=sorted(t)[-k:]
        _,t=zip(*t)
        return list(t)