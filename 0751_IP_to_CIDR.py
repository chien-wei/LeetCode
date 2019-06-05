from functools import reduce
from operator import add
from math import log
from typing import List
class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        INDICES = [(0, 8), (8, 16), (16, 24), (24, 32)]

        ipint = list(map(int, ip.split('.')))
        value = int(reduce(add, map('{:08b}'.format, ipint), ""), 2)

        res = []
        last = value & -value
        # first find the last digit that is one
        while n >= last:
            bit = '{:032b}'.format(value)
            bitList = list(map(str, [int(bit[s:e], 2) for s,e in INDICES]))
            res.append('.'.join(bitList) + '/' + str(32 - int(log(last, 2))))
            value += last
            n -= last

            last = value & -value

        # now use last is too much, so try one bit a time
        while n != 0:
            if n >= last:
                n -= last
                bit = '{:032b}'.format(value)
                bitList = list(map(str, [int(bit[s:e], 2) for s,e in INDICES]))
                res.append('.'.join(bitList) + '/' + str(32 - int(log(last, 2))))
                value += last
            last >>= 1
        return res
            


s = Solution()
print(s.ipToCIDR("255.0.0.7", 10))
print(s.ipToCIDR("255.0.0.7", 12))
print(s.ipToCIDR("255.0.255.255", 10))
print(s.ipToCIDR("255.0.0.255", 256))
