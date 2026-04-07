class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        a = [0] * 26                            
        x = t
        for k in range(2):
          y=-1 if k%2==0 else 1
          x = s if x == t else t 
          for i in x:
            arr[ord(i) - ord('a')]+=y                                                                                                    
        return a == arr