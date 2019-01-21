class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        hsh = {}
        for (eq, v) in zip(equations, values):
            hsh[eq[0]] = hsh.get(eq[0], {})
            hsh[eq[0]][eq[1]] = v
            hsh[eq[1]] = hsh.get(eq[1], {})
            hsh[eq[1]][eq[0]] = 1/v
        
        def find(s, t, hsh, vted, acc):
            if s not in hsh:
                return -1.0
            if t in hsh[s]:
                return acc * hsh[s][t]
            else:
                vted.add(s)
                for mid in hsh[s]:
                    if mid not in vted:
                        r = find(mid, t, hsh, set(vted), acc * hsh[s][mid])
                        if r > 0.0:
                            return r
            return -1.0
        
        res = []
        for q in queries:
            res.append(find(q[0], q[1], hsh, set(), 1.0))
        return res