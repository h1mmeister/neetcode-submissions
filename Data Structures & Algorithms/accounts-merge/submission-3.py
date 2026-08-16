class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n

    def find(self, value):
        curr_value = value
        while curr_value != self.parents[curr_value]:
            curr_value = self.parents[curr_value]

        return curr_value

    def union(self, value1, value2):
        value1_repr = self.find(value1)
        value2_repr = self.find(value2)

        if value1_repr == value2_repr:
            return False
        
        if self.ranks[value1_repr] > self.ranks[value2_repr]:
            self.parents[value2_repr] = value1_repr
        elif self.ranks[value1_repr] < self.ranks[value2_repr]:
            self.parents[value1_repr] = value2_repr
        else:
            self.parents[value2_repr] = value1_repr
            self.ranks[value1_repr] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        email_to_account_idx = {}
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account_idx:
                    uf.union(idx, email_to_account_idx[email])
                email_to_account_idx[email] = idx

        email_groups = defaultdict(list)
        for email, account_idx in email_to_account_idx.items():
            representative = uf.find(account_idx)
            email_groups[representative].append(email)

        result = []
        for account_idx, emails in email_groups.items():
            name = accounts[account_idx][0]
            result.append([name] + sorted(emails))

        return result


        