# write a program using the Levenshein distance
def memoize(f):
    memo = {}
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in memo:
            memo[key] = f(*args, **kwargs)
        return memo[key]
    return memoizer

@memoize
def levenshtein(s, t):
    """ function to calculate Levenshtein Distance;
    https: // en.wikipedia.org / wiki / Levenshtein_distance """
    if s == '':
        return len(t)
    if t == '':
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    res = min([
        levenshtein(s[:-1], t) + 1,
        levenshtein(s, t[:-1]) + 1,
        levenshtein(s[:-1], t[:-1]) + cost
        ])

    return res

def iterative_levenshtein(s, t, **weight_dict):
    """ iterative_levenshtein(s, t) -> ldist
    ldist is the levenshtein distance between the strings s and t.
    For all i and j, dist[i, j] will contain the levenshtein distance between the first i characters of s and the first j characters of t
    
    weight_dict: keyword parameters setting the costs for characters, the default value for a character will be 1 """

    rows = len(s) + 1
    cols = len(t) + 1

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    w = dict((x, (1, 1, 1)) for x in alphabet + alphabet.upper() + ' ')
    if weight_dict:
        w.update(weight_dict)

    dist = [[0 for x in range(cols)] for x in range(rows)]

    # source prefixes can be transformed into empty strings
    # by deletions:
    for i in range(1, rows):
        dist[i][0] = i

    # target prefixes can be created from an empty source string
    # by inserting the characters
    for i in range(1, cols):
        dist[0][i] = i

    for col in range(1, cols):
        for row in range(1, rows):
            deletes = w[s[row - 1]][0]
            inserts = w[t[col - 1]][1]
            subs = max((w[s[row - 1]][2], w[t[col - 1]][2]))
            if s[row - 1] == t[col - 1]:
                subs = 0
            else:
                subs = subs
            
            dist[row][col] = min(
                dist[row - 1][col] + deletes,         # deletion
                dist[row][col - 1] + inserts,         # insertion
                dist[row - 1][col - 1] + subs)  # substitution

    return dist[row][col]

cities = {
    "Pittsburgh": "Pennsylvania",
    "Tuscon": "Arizona",
    "Cincinnati": "Ohio",
    "Albuquerque": "New Mexico",
    "Culpeper": "Virginia",
    "Asheville": "North Carolina",
    "Worcester": "Massachusetts",
    "Manhattan": "New York",
    "Phoenix": "Arizona",
    "Niagara Falls": "New York"
}

#print(levenshtein('Python', 'Peithon'))
# print(iterative_levenshtein('Phoenix', 'Phenix'))
# print(iterative_levenshtein('abx', 'xyz', x=(3, 2, 8), y=(4, 5, 4), a=(7, 6, 6)))

while True:
    n = input('Capital: ')
    if n in cities:
        print(f'That is in {cities[n]}!\n')
    elif n == 'q':
        break
    else:
        m = None
        name = None
        for s in cities.keys():
            x = iterative_levenshtein(n, s)
            if m == None:
                m = x
                name = s
            elif x < m:
                name = s
                m = x
        x = input(f'Did you mean {name}? ')
        if x == 'y':
            print(f'{name} is in {cities[name]}!\n')
        else:
            
            print('Sorry, we can not help you :(\n')