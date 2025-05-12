def sum(candidates, target):
    def uniqueelem(start, path, target):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates [i] > target:
                break
            uniqueelem(i + 1, path + [candidates[i]], target - candidates[i])
    candidates.sort()
    result = []
    uniqueelem(0, [], target)
    return result
candidates = [2, 5, 2, 1, 2]
target = 5
comsum = sum(candidates, target)
for combo in comsum:
    print(combo)
candidates = [10, 1, 2 ,7, 6, 1, 5]
target = 8
comsum = sum(candidates, target)
for combo in comsum:
    print(combo)