from typing import List

# refer to https://ganeshpr227.medium.com/logarithmic-algorithm-for-finding-median-of-two-sorted-arrays-of-different-sizes-aaecf302057e
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        
        if m == 0:
            if n % 2:
                return nums2[n // 2 + 1]
            else:
                return (nums2[n // 2] + nums2[n // 2 + 1]) / 2

        elif n == 0:
            if m % 2:
                return nums1[m // 2 + 1]
            else:
                return (nums1[m // 2] + nums1[m // 2 + 1]) / 2

        if m > n:
            m, n = n, m
            nums1, nums2 = nums2, nums1

        first_half_size = (m + n + 1) // 2
        min_nums1_contributes, max_nums1_contributes = 0, m

        while min_nums1_contributes <= max_nums1_contributes:
            nums1_contributes = min_nums1_contributes + (max_nums1_contributes - min_nums1_contributes) // 2
            nums2_contributes = first_half_size - nums1_contributes

            if nums1_contributes > 0 and nums1[nums1_contributes - 1] > nums2[nums2_contributes]:
                max_nums1_contributes = nums1_contributes - 1
            
            elif nums1_contributes < len(nums1) and nums1[nums1_contributes] < nums2[nums2_contributes - 1]:
                min_nums1_contributes = nums1_contributes + 1

            else:
                if nums1_contributes == 0:
                    last_of_left_half = nums2[nums2_contributes - 1]
                elif nums2_contributes == 0:
                    last_of_left_half = nums1[nums1_contributes - 1]
                else:
                    last_of_left_half = max(nums1[nums1_contributes - 1], nums2[nums2_contributes - 1])

                if (m + n) % 2 == 1:
                    return last_of_left_half

                if nums1_contributes == m:
                    first_of_right_half = nums2[nums2_contributes]
                elif nums2_contributes == n:
                    first_of_right_half = nums1[nums1_contributes]
                else:
                    first_of_right_half = min(nums1[nums1_contributes], nums2[nums2_contributes])
                
                return (last_of_left_half + first_of_right_half) / 2