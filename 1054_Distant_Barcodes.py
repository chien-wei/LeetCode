class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = {}
        for b in barcodes:
            freq[b] = freq.get(b, 0) + 1
        sorted_dict = list(sorted(freq.items(), key=lambda k: -k[1]))
        
        res = [0 for _ in range(len(barcodes))]
        for odd in range(0, len(barcodes), 2):
            res[odd] = sorted_dict[0][0]
            if sorted_dict[0][1] == 1:
                sorted_dict.pop(0)
            else: sorted_dict[0] = (sorted_dict[0][0], sorted_dict[0][1] - 1)
        
        for even in range(1, len(barcodes), 2):
            res[even] = sorted_dict[0][0]
            if sorted_dict[0][1] == 1:
                sorted_dict.pop(0)
            else: sorted_dict[0] = (sorted_dict[0][0], sorted_dict[0][1] - 1)
        return res