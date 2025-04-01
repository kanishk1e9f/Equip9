from collections import defaultdict

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res

def maintenance_log_analysis(maintenance_logs, queries):
    date_to_cost = defaultdict(int)
    dates = []

    for _, date, cost in maintenance_logs:
        date_to_cost[date] += cost
        dates.append(date)

    dates = sorted(set(dates))
    date_index = {date: i for i, date in enumerate(dates)}

    cost_array = [date_to_cost[date] for date in dates]
    segment_tree = SegmentTree(cost_array)

    result = []
    for start, end in queries:
        if start not in date_index or end not in date_index:
            result.append(0)
        else:
            result.append(segment_tree.query(date_index[start], date_index[end]))

    return result

maintenance_logs = [
    (101, "2024-01-01", 500),
    (102, "2024-01-10", 300),
    (101, "2024-01-15", 700)
]
queries = [("2024-01-01", "2024-01-10"), ("2024-01-01", "2024-01-15")]

print(maintenance_log_analysis(maintenance_logs, queries))
