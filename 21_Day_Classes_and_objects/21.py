class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        data = sorted(self.data)
        n = len(data)
        mid = n // 2
        if n % 2 == 0:
            return (data[mid - 1] + data[mid]) / 2
        else:
            return data[mid]

    def mode(self):
        frequency = {}
        for value in self.data:
            frequency[value] = frequency.get(value, 0) + 1
        max_count = max(frequency.values())
        modes = [value for value, count in frequency.items() if count == max_count]
        if len(modes) == 1:
            return {'mode': modes[0], 'count': max_count}
        return {'mode': modes, 'count': max_count}

    def var(self):
        mean = self.mean()
        squared_diffs = [(x - mean) ** 2 for x in self.data]
        return sum(squared_diffs) / self.count()  # population variance (divide by n)

    def std(self):
        return self.var() ** 0.5

    def freq_dist(self):
        frequency = {}
        for value in self.data:
            frequency[value] = frequency.get(value, 0) + 1
        n = self.count()
        dist = [(round(count / n * 100, 2), value) for value, count in frequency.items()]
        # sort by frequency % descending, then by value descending on ties
        dist.sort(key=lambda pair: (-pair[0], -pair[1]))
        return dist

    def describe(self):
        print('Count:', self.count())
        print('Sum: ', self.sum())
        print('Min: ', self.min())
        print('Max: ', self.max())
        print('Range: ', self.range())
        print('Mean: ', round(self.mean()))
        print('Median: ', self.median())
        print('Mode: ', self.mode())
        print('Variance: ', round(self.var(), 1))
        print('Standard Deviation: ', round(self.std(), 1))
        print('Frequency Distribution: ', self.freq_dist())


# Usage
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count())              # 25
print('Sum: ', data.sum())                 # 744
print('Min: ', data.min())                 # 24
print('Max: ', data.max())                 # 38
print('Range: ', data.range())             # 14
print('Mean: ', round(data.mean()))        # 30
print('Median: ', data.median())           # 29
print('Mode: ', data.mode())               # {'mode': 26, 'count': 5}
print('Standard Deviation: ', round(data.std(), 1))  # 4.2
print('Variance: ', round(data.var(), 1))            # 17.5
print('Frequency Distribution: ', data.freq_dist())
# [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33),
#  (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

data.describe()