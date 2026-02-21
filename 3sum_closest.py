from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()  # Step 1: Sort the array
        n = len(nums)
        
        # Step 2: Initialize closest sum
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # Step 3: Fix one element
        for i in range(n - 2):
            
            left = i + 1
            right = n - 1
            
            # Step 4: Two-pointer approach
            while left < right:
                
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Step 5: Update closest sum if needed
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Step 6: Move pointers
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # Exact match
        
        return closest_sum