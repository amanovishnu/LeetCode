class SnapshotArray:

    def __init__(self, length: int):
        self.cur_id = 0
        self.curVals = [0] * length
        self.snapIdArr = [[-1] for _ in range(length)]
        self.arrVal = [[0] for _ in range(length)]
        self.modified = set()

    def set(self, index: int, val: int) -> None:
        if val == self.arrVal[index][-1]:
            if index in self.modified: self.modified.remove(index)
            return
        self.curVals[index] = val
        if index not in self.modified: self.modified.add(index)

    def snap(self) -> int:
        for idx in self.modified:
            self.snapIdArr[idx].append(self.cur_id)
            self.arrVal[idx].append(self.curVals[idx])
        self.modified.clear()
        self.cur_id += 1
        return self.cur_id - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.snapIdArr[index]
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] <= snap_id:
                l = m + 1
            else: r = m
        return self.arrVal[index][l-1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)