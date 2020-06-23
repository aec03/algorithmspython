def memoize(f):
    results = {}
    def helper(n):
        if n not in results:
            results[n] = f(n)
        return results[n]
    return helper

def factors_set():
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    yield (i, j, k, l)

@memoize
def linear_combination(n):
    """ returns the tuple (i, j, k, l) satisfying """
    weighs = (1, 3, 9, 27)

    for factors in factors_set():
        sum = 0
        for i in range(len(factors)):
            sum += factors[i] * weighs[i]
        if sum == n:
            return factors

def weigh(pounds):
    weighs = (1, 3, 9, 27)
    lbs = linear_combination(pounds)
    left = '+' + str(pounds)
    right = ''
    for i in range(len(lbs)):
        if lbs[i] < 0:
            left += ' +' + str(weighs[i])
        elif lbs[i] > 0:
            right += ' +' + str(weighs[i])
        else:
            continue

    return left + '\t\t|\t' + right

for i in range(1, 41):
    print(weigh(i))
