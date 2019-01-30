def findMissingRanges(nums):
    i ,j = 0, 0
    s, e = 0, 0
    flag = False
    res = []
    while i < 100 and j < len(nums):
        if not flag and i == nums[j]:
            j += 1
        elif not flag and i != nums[j]:
            s = i
            flag = True
        elif flag and i == nums[j]:
            e = i-1
            if s == e:
                res.append(str(s))
            else:
                res.append(str(s) + '->' + str(e))
            flag = False
            j += 1
        i += 1
    if i != 100:
        res.append(str(i) + '->' + str(99))
    return res
print(findMissingRanges([0, 1, 3, 50, 75]))
print(findMissingRanges([2, 6]))
print(findMissingRanges([97, 99]))