class Solution:
    def customSortString(self, order: str, s: str) -> str:
        charMap = defaultdict(int)
        
        for index, char in enumerate(order):
            charMap[char] = index
        
        orders = []
        for char in s:
            if char not in charMap:
                orders.append((-1, char))
                continue
            pos = charMap[char]
            orders.append((pos, char))
            
        return "".join([tup[1] for tup in sorted(orders, key=lambda x: x[0])])
            
        