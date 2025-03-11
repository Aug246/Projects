class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        intnums = len(nums)
        for i  in range(len(intnums)):
            n = 1
            while n < (intnums - i):
                sum = nums[i] + nums[i+n]                
                if sum == target:
                    Output = [i,n+i]
                    print (Output)
                    break
                n += 1
        return Output
def main():
    nums = [3,3]
    target = 6
    S = Solution()
    S.twoSum(nums, target)

main()

        