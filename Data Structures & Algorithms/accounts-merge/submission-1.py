class UnionFind:

    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, value):
        while value != self.parents[value]:
            self.parents[value] = self.parents[self.parents[value]]
            value = self.parents[value]
        return value

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parents[root_b] = root_a
        self.size[root_a] += self.size[root_b]

        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_account = {}

        # Merge accounts that share an email
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    uf.union(idx, email_to_account[email])
                else:
                    email_to_account[email] = idx

        # Group emails by account leader
        email_groups = defaultdict(list)

        for email, idx in email_to_account.items():
            leader = uf.find(idx)
            email_groups[leader].append(email)

        # Build result
        result = []

        for leader, emails in email_groups.items():
            name = accounts[leader][0]
            result.append([name] + sorted(emails))

        return result