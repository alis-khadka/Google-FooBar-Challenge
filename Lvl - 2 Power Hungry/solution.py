import functools


def solution(xs):
    """Solar Panels array maximum output."""
    positive = sorted(list(filter(lambda a: a > 0, xs)), reverse=True)
    negative = sorted(list(filter(lambda a: a < 0, xs)))

    if (not(positive) and not(negative)) or ((0 in xs) and len(negative) == 1):
        return '0'
    elif (not(positive) and len(negative) == 1):
        return str(negative[0])

    if len(negative) % 2 == 0:
        neg_subset = negative
    else:
        neg_subset = negative[:-1]

    pos_prod = functools.reduce(
        lambda x, y: x * y, positive) if positive else 1
    neg_prod = functools.reduce(
        lambda x, y: x * y, neg_subset) if neg_subset else 1

    return str(pos_prod * neg_prod)


print(solution([0, -4]))
