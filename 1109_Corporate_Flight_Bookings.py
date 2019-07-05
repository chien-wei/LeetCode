class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        acc = [0 for _ in range(n+2)]
        for start, end, seats in bookings:
            acc[start] += seats
            acc[end+1] -= seats
        
        cur = 0
        for i in range(len(acc)):
            cur += acc[i]
            acc[i] = cur
        return acc[1:len(acc)-1]