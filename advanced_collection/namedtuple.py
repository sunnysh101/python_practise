# Advanced collections

# To access the advanced collection import collections module.
# eg:
# namedtuple                  Tuple with named fields
# OrderedDict, defaultdict    Dictionaries with special properties
# Counter                     Counts distinct values
# deque                       Double-ended list object

import collections

def main():
    # Define an object from the namedtuple
    Point = collections.namedtuple('Point', 'x y')
    
    # Once initialized the value can be added as:
    p1 = Point(10, 20)
    p2 = Point(20, 40)

    # Namedtuple can be printed as:
    print(p1)

    # Individual datapoints can be printed as
    print(p1.x, p2.y)

    # And it can be replaced using the _replace function
    p1 = p1._replace(x=100)
    print(p1)

    # Simple example
    Area = collections.namedtuple('Area', 'length breadth')
    area1 = Area(10, 20)
    print('Area of Area1 =', area1.length*area1.breadth)

if __name__ == "__main__":
    main()
