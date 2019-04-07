class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        end, end2 = -1, 0
        result = 0
        print(sorted(clips))
        for s, e in sorted(clips):
            if end2 >= T or s > end2:
                break
            elif end < s <= end2:
                result += 1
                end = end2
            end2 = max(end2, e)
            print(s,e,end, end2)
        return result if end2 >= T else -1