import itertools
class List2D:
    def __init__(self, list2d):
        self.gen = iter([e for li in list2d for e in li])

    def next(self):
        return next(self.gen)

    def hasNext(self):
        try:
            x = self.next()
            self.gen = itertools.chain(iter([x]), self.gen)
            return True
        except StopIteration:
            return False



list2d = List2D([[1,2],[3],[4,5,6]])
assert list2d.next() == 1
assert list2d.next() == 2
assert list2d.next() == 3
assert list2d.hasNext()
assert list2d.next() == 4
assert list2d.next() == 5
assert list2d.next() == 6
assert not list2d.hasNext()