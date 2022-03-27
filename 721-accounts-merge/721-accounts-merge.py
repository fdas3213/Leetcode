class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        
        for account in accounts:
            first_email = account[1]
            
            for email in account[2:]:
                graph[email].append(first_email)
                graph[first_email].append(email)
        
        visited = set()
        
        def dfs(email, mergedList):
            for neighbor in graph[email]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    mergedList.append(neighbor)
                    dfs(neighbor, mergedList)
        
        ans = []
        
        for account in accounts:
            name = account[0]
            first_email = account[1]
            if first_email in visited:
                # avoid adding duplicate
                continue
            curList = [name]
            curList.append(first_email)
            visited.add(first_email)
            dfs(first_email, curList)
            curList[1:] = sorted(curList[1:])
            ans.append(curList)
            
        return ans
    