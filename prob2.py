# Time Complexity : O(N)
# Space Complexity : O(1) as no extra space
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : No


def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
      
        p1 = m - 1  
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1