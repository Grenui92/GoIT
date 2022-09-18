def factorial(n):
    """ Find factorial of number N """

    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)
def number_of_groups(n, k):
    """ Find how many lists of chelengers we can find

    N - numbers of members. K - how many wins"""
    return int(factorial(n)/(factorial(n-k)*factorial(k)))



