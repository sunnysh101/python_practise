""" Defaultdict
"""

from collections import defaultdict

def main():
    sports = ['football', 'basketball', 'cricket', 'swimming',
            'football', 'basketball']

    # defaultdict will assign a default to int 0 value
    sportsCounter = defaultdict(int)

    # Use lambda to assign anything else
    # sportsCounter = defaultdict(lambda: 'Hello World')
    for sport in sports:
        sportsCounter[sport] += 1

    for k, v in sportsCounter.items():
        print(k,": ", v)

if __name__ == '__main__':
    main()