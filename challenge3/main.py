
def fun(stringa):
    letters = dict()
    for char in stringa:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 0

    values = sorted(letters.values())
    prev = values[0]
    diffs = 0
    for val in values:
        diffs += val - prev

    if diffs < 2:
        return "valido"
    else:
        return "non valido"


stringa = str(input())
print(fun(stringa))
