class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        value = {}
        i = 0
        for eq in equations:
            if eq[1] == '=':
                if eq[0] in value:
                    value[eq[3]] = value[eq[0]]
                elif eq[3] in value:
                    value[eq[0]] = value[eq[3]]
                else:
                    value[eq[3]] = i
                    value[eq[0]] = i
                    i += 1
                
        for eq in equations:
            if eq[1] == '!' and eq[0] == eq[3]:
                return False
            if eq[1] == '!' and eq[0] in value and eq[3] in value and value[eq[0]] == value[eq[3]]:
                return False
        return True