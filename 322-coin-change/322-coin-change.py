class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return amount
        
        visited = [True]+[False]*amount
        # (curstep, curValue)
        queue = deque([(1,0)])
        
        while queue:
            curStep, curVal = queue.popleft()
            for coin in coins:
                nxtVal = curVal+coin
                if nxtVal==amount:
                    return curStep
                elif nxtVal<amount and not visited[nxtVal]:
                    visited[nxtVal] = True
                    queue.append((curStep+1, nxtVal))
        
        return -1