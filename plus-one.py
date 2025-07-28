class Solution(object):
    def plusOne(self, digits):
            if digits[-1]==9:
                  return [1,0]
            digits[-1]+=1
            return digits
        

        