class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #sortednums = sorted(nums)
        #for i in range(len(sortednums)-1):
            #if sortednums[i] == sortednums[i+1]:
                #return True
            #elif sortednums[i] != sortednums[i+1]:
                #return False

        return len(nums) != len(set(nums))
