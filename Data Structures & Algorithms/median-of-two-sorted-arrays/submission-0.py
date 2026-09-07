class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        
        # the shorter list is A, and we binary search it
        l, r = 0, len(A) - 1
        half = (len(A) + len(B)) // 2
        while True:
            boarderAInd = (l + r) // 2
            boarderBInd = half - boarderAInd - 2
            
            Aleft = A[boarderAInd] if boarderAInd >= 0 else float("-infinity")
            Aright = A[boarderAInd + 1] if boarderAInd + 1 < len(A) else float("infinity")
            Bleft = B[boarderBInd] if boarderBInd >= 0 else float("-infinity")
            Bright = B[boarderBInd + 1] if boarderBInd + 1 < len(B) else float("infinity")
            
            # if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                if (len(A) + len(B)) % 2: #odd
                    return min(Aright, Bright)
                else: #even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            else:
                if Aleft > Bright:
                    r = boarderAInd - 1
                else:
                    l = boarderAInd + 1
