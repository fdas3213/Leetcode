class SnapshotArray:

    def __init__(self, length: int):
        self.cache = []
        self.arr = {}
        self.snap_count = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val
        
    def snap(self) -> int:
        self.cache.append(dict(self.arr))
        self.snap_count += 1
        return self.snap_count-1

    def get(self, index: int, snap_id: int) -> int:
        # print("get: ", self.snap_hist)
        arr = self.cache[snap_id]
        return arr[index] if index in arr else 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)