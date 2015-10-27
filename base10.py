import collections

def digit_set(n):
    """good if you want the set, ie repeated elements are removed"""

    n = int(n)
    digit_set = set()
    while n > 0:
        digit_set.add(n % 10)
        n = (n - (n % 10)) // 10

    return digit_set


def digit_counter(n):
    """good if you want to keep repeated elements but don't care about order"""

    n = int(n)
    d_counter = collections.Counter()
    while n > 0:
        d_counter[(n % 10)] += 1
        n = (n - (n % 10)) // 10

    return d_counter


