class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        N = len(rooms)
        if N == 0:
            return True
        que = [0]
        seen = [False for _ in range(N)]
        while len(que) > 0:
            inRoom = que.pop(0)
            seen[inRoom] = True
            for r in rooms[inRoom]:
                if not seen[r]:
                    que.append(r)
                    
        for check in seen:
            if not check:
                return False
        return True