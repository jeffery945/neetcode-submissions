class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False, False, False]
        for triplet in triplets:
            res[0] |= (triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2])
            res[1] |= (triplet[0] <= target[0] and triplet[1] == target[1] and triplet[2] <= target[2])
            res[2] |= (triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] == target[2])

            if res[0] and res[1] and res[2]:
                return True
        return False
