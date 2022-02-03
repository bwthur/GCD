import timeit

@profile
def GCD_loop(n, m):
    if m == 0:
        return 0
    l = n % m
    while l > 0:
        n = m
        m = l
        l = n % m
    return m

@profile
def GCD_Recursion(n, m):
    if m == 0:
        return n
    else:
        l = n % m
        n = m
        m = l
        return GCD_Recursion(n, m)

def test_loop():
    GCD_loop(90876543343, 203810301)

def test_recursion():
    GCD_Recursion(90876543343, 203810301)

test_loop()
test_recursion()

# print("Recursion time: " + str(timeit.Timer(test_recursion).timeit(number=100)))
# print("Loop time: " + str(timeit.Timer(test_loop).timeit(number=100)))





