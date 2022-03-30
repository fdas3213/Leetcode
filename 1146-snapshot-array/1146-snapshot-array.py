class SnapshotArray:

    def __init__(self, length: int):
        #use a hashmap {0:{snap_id:val}}
        self.snapArray = defaultdict(defaultdict)
        self.count = 0
        
    def set(self, index: int, val: int) -> None:
        self.snapArray[self.count][index] = val

    def snap(self) -> int:
        cur = self.count
        self.count += 1
        # copy the previous snapshot to current snapshot
        self.snapArray[self.count] = self.snapArray[cur].copy()
        return cur

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.snapArray[snap_id]:
            return 0
        return self.snapArray[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)