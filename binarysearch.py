def binary_search(t, item):
    low = 0
    high = len(t) - 1
    
    while low <= high:
        mid = int((low + high) / 2)
        guess = t[mid]
        if guess == item: return mid
        if guess > item: high = mid - 1
        else: low = mid + 1

    return None


def simple_search(t, item):
    for i in t:
        if i == item: return item
    return None


if __name__ == '__main__':
    t = [x for x in range(100234000)]

    print(binary_search(t, 93931493))
    print(simple_search(t, 93931493))