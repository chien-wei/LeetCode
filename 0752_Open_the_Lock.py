class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # classic BFS
        NUM_DIGIT = 4
        
        que = ["0000"]
        seen = set()
        dead = set(deadends)
        move = 0
        while len(que):
            newQue = []
            while len(que):
                cur = que.pop(0)
                
                if cur in dead:
                    continue
                    
                for i in range(NUM_DIGIT):
                    print(i, cur)
                    nxt1 = cur[:i] + str((int(cur[i]) + 11) % 10) + cur[i+1:]
                    nxt2 = cur[:i] + str((int(cur[i]) + 9) % 10) + cur[i+1:]
                    if nxt1 == target or nxt2 == target:
                        return move + 1
                    if nxt1 not in seen:
                        newQue.append(nxt1)
                        seen.add(nxt1)
                    if nxt2 not in seen:
                        newQue.append(nxt2)
                        seen.add(nxt2)
            que = newQue
            move += 1
            
        return -1