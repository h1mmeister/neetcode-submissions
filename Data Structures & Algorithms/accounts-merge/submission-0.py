class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)
                email_to_name[email] = name

        result = []
        visited = set()

        for email in graph:
            if email not in visited:
                visited.add(email)
                stack = [email]
                components = []

                while stack:
                    curr_email = stack.pop()
                    components.append(curr_email)

                    for neighbor in graph[curr_email]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)

                result.append([email_to_name[email]] + sorted(components))

        return result


        