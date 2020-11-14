
def fun(days):
    reductions = 0
    increments = 0
    neutral = 0

    for day in days:
        if day == 0:
            neutral += 1
        elif day > 0:
            increments += 1
        else:
            reductions += 1

    reductions /= len(days)
    increments /= len(days)
    neutral /= len(days)

    increments = round(increments * 100, 1)
    if int(increments) == increments:
        increments = int(increments)

    reductions = round(reductions * 100, 1)
    if int(reductions) == reductions:
        reductions = int(reductions)

    neutral = round(neutral * 100, 1)
    if int(neutral) == neutral:
        neutral = int(neutral)

    print(increments)
    print(reductions)
    print(neutral)


n = int(input())
days = [int(x) for x in input().split()]
fun(days)
