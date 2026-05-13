class Solution:

    def encode(self, strs: List[str]) -> str:
      def x(strs):
        if strs !="": return "$".join(map(str, map(ord,strs))) + "#"
        else: return "&"
      return "".join(map(x,strs))
    def decode(self, s: str) -> List[str]:
      n,h,x,i="","",[],0
      while i< len(s):
        if s[i]=="&":
            x.append("")
            i+=1
        else:
            if s[i]!="$":
                n+=s[i]
                i+=1
            elif s[i]=="$":
                h+=chr(int(n))
                n=""
                i+=1
            if s[i]=="#":
                h+=chr(int(n))
                n=""
                x.append(h)
                h=""
                i+=1
      return x