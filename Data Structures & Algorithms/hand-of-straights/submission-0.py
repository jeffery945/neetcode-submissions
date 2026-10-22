class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        hand.sort()
        count = Counter(hand)
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize): # check that if it can form a straight from num to num + groupSize
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True