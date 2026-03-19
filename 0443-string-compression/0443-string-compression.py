class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i=0
        j=1
        count=1
        while j<len(chars):
            if chars[j-1]==chars[j]:
                count+=1
            elif count==1:
                i+=1
                chars[i]=chars[j]
            else:
                count_mul=list(str(count))
                for x in count_mul:
                    chars[i+1]=x
                    i+=1
                i+=1
                chars[i]=chars[j]
                count=1
            j+=1
        if count==1:
                i+=1
        else:
            count_mul=list(str(count))
            for x in count_mul:
                chars[i+1]=x
                i+=1
            i+=1
            count=1
        return i

        