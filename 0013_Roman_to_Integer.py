class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = ["M", "D", "C", "L", "X", "V", "I"]
        values = [1000, 500, 100, 50, 10, 5, 1]
        
        kvs = dict(zip(symbols, values))
        num_list = []
        
        for c in s:
            num_list.append(kvs[c])
        
        #print(num_list)
        i = 0
        result = 0
        while i < (len(num_list)):
            if i+1 < len(num_list) and num_list[i+1] > num_list[i]:
                result += num_list[i+1] - num_list[i]
                i += 2
            else:
                result += num_list[i]
                i += 1
        return result