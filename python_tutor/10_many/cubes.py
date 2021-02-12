'''
    Source: https://pythontutor.ru/lessons/sets/problems/cubes/
    Condition
    Anya and Borya love to play multi-colored cubes,
    each of which has its own set and in each set all the cubes are different in color.
    Once the children became interested in how many colors exist such that cubes of each color are present in both sets.
    To do this, they numbered all the colors with random numbers from 0 to 108.
    On this their enthusiasm ran out, so you are invited to help them in the rest.
    The first line of the input contains the numbers N and M - the number of cubes for Ani and Bori.
    The next N lines contain the color numbers of Ani cubes. The last M lines of the color numbers Bori.
    Find three sets: the color numbers of the cubes that are in both sets;
    the color numbers of the cubes that Ani has only; and the color numbers of the cubes that Bori has only.
    For each of the sets print first the number of elements in it, and then the elements themselves, sorted in ascending order.
'''
def cubes(n, m):
    print(len(n.intersection(m)))
    print(n.intersection(m))
    print(len(n.difference(m)))
    print(sorted(n.difference(m)))
    print(len(m.difference(n)))
    print(sorted(m.difference(n)))
    print(len([x for x in n if x not in m]))
    print(sorted([x for x in n if x not in m]))
    print(len([x for x in m if x not in n]))
    print(sorted([x for x in m if x not in n]))

cubes({0, 2, 1, 10, 9}, {1, 2, 3, 0})