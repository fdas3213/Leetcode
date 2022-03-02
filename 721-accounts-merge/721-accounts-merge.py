class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        
        #use the first email to build a graph
        # add edge between first email to all other emails in the account
        for account in accounts:
            first_email = account[1]
            
            for email in account[2:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
        
        #initialize visited set
        visited = set()
        
        #dfs traverse
        def dfs(account, first_email):
            if first_email not in graph:
                return
            
            for email in graph[first_email]:
                if email not in visited:
                    account.append(email)
                    visited.add(email)
                    dfs(account, email)
        
        #traverse through the input array again
        res = []
        for account in accounts:
            name, first_email = account[0],account[1]
            
            #if this email is already visited, then no need to continue
            if first_email not in visited:
                mergedAccount = []
                mergedAccount.append(name)
                mergedAccount.append(first_email)
                visited.add(first_email)
                dfs(mergedAccount, first_email)

                mergedAccount[1:] = sorted(mergedAccount[1:])
                res.append(mergedAccount)
        
        return res
        
            
            