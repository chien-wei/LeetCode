# first draft dfs: TLE
def maxVacationDays(flights, days):

    def recur(city, week, acc):
        if week == len(days[0]):
            return acc
        mx = 0
        for j in range(len(flights[city])):
            if flights[city][j] == 1 or city == j:
                mx = max(mx, recur(j, week+1, acc+days[j][week]))
        return mx

    return recur(0, 0, 0)

# Improved by memorization, top-down DP
def maxVacationDays(flights, days):

    def recur(city, week, acc, memo):
        if week == len(days[0]):
            return acc
        if memo[city][week] > 0:
            return memo[city][week]
        mx = 0
        for j in range(len(flights[city])):
            if flights[city][j] == 1 or city == j:
                mx = max(mx, recur(j, week+1, acc+days[j][week], memo))
        memo[city][week] = mx
        print(memo)
        return mx

    memo = [[0 for _ in days[0]] for _ in flights]
    return recur(0, 0, 0, memo)



print(maxVacationDays([[0,1,1],[1,0,1],[1,1,0]], [[1,3,1],[6,0,3],[3,3,3]]))
print(maxVacationDays([[0,0,0],[0,0,0],[0,0,0]], [[1,1,1],[7,7,7],[7,7,7]]))
print(maxVacationDays([[0,1,1],[1,0,1],[1,1,0]], [[7,0,0],[0,7,0],[0,0,7]]))

