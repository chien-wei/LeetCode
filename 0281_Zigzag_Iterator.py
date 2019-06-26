class iterator:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.in_v1 = True

    def next(self):
        res = None
        if len(self.v1) > 0 and self.in_v1:
            res = self.v1.pop(0)
            self.in_v1 = False
        elif len(self.v2) > 0:
            res = self.v2.pop(0)
            self.in_v1 = True
        elif len(self.v1) > 0:
            res = self.v1.pop(0)
        return res

i = iterator([1,2],[3,4,5,6])
print(i.next())
print(i.next())
print(i.next())
print(i.next())
print(i.next())
print(i.next())
