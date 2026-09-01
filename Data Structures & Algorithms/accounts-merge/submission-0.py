class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToName = {}
        graph = defaultdict(list)

        for account in accounts:
            name = account[0]
            first_email = account[1]

            emailToName[first_email] = name
            
            for i in range(2, len(account)):
                email = account[i]
                
                graph[first_email].append(email)
                graph[email].append(first_email)

                emailToName[email] = name
        
        for account in accounts:

            graph[account[1]]
            emailToName[account[1]] = account[0]

        visited = set()
        result = []

        def dfs(email, component):
            visited.add(email)
            component.append(email)

            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)
        
        for email in graph:
            if email in visited:
                continue
            component = []
            dfs(email, component)

            component.sort()

            result.append([emailToName[email]] + component)
        
        return result

                
        