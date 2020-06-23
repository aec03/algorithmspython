def findLargest(t):
    max = t[0]
    max_index = 0
    for i in range(1, len(t)):
        if t[i] > max:
            max = t[i]
            max_index = i
    return max_index


def selectionSort(t):
    nl = []
    for _ in range(len(t)):
        max = findLargest(t)
        nl.append(t.pop(max))
    return nl