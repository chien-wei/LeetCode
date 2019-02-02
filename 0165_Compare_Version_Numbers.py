class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if len(version1) == 0 and len(version2) == 0:
            return 0
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in range(len(v1)):
            if i < len(v2) and int(v1[i]) > int(v2[i]):
                return 1
            elif i < len(v2) and int(v1[i]) < int(v2[i]):
                return -1
            elif i >= len(v2) and int(v1[i]) > 0:
                return 1 
        for j in range(len(v1), len(v2)):
            if int(v2[j]) > 0:
                return -1
        return 0