def bowling_throws1(n, throws):
    pins = list(range(1,n+1))
    print('pins = '+str(pins))
    throws_expanded = []
    for throw_start, throw_end in throws:
        this_throw = list(range(throw_start, throw_end + 1))
        print(this_throw)
        throws_expanded.extend(this_throw)
    print('removed_pins = '+str(throws_expanded))
    pins_result = []
    for pin in pins:
        pins_result.append(0 if pin in throws_expanded else 1)
    print(pins_result)

def bowling_throws2(n, throws):
    pins = list(range(1,n+1))
    print('pins = '+str(pins))
    throws_expanded = []
    for throw_start, throw_end in throws:
        this_throw = list(range(throw_start, throw_end + 1))
        print(this_throw)
        throws_expanded.extend(this_throw)
    print('removed_pins = '+str(throws_expanded))
    pins_result = [0 if pin in throws_expanded else 1 for pin in pins]
    print(pins_result)

def bowling_throws3(n, throws):
    print(throws)
    pins = list(range(1,n+1))
    print('pins = '+str(pins))
    throws_expanded_p1 = [list(range(throw[0], throw[1]+1)) for throw in throws]
    print('intermediate list = '+str(throws_expanded_p1))
    throws_expanded_p2 = []
    for sublist in throws_expanded_p1:
        throws_expanded_p2+=sublist
    print('removed_pins = '+str(throws_expanded_p2))
    pins_result = [0 if pin in throws_expanded_p2 else 1 for pin in pins]
    print(pins_result)

def bowling_throws4(n, throws):
    print(throws)
    pins = list(range(1,n+1))
    print('pins = '+str(pins))
    throws_expanded_p1 = [list(range(throw[0], throw[1]+1)) for throw in throws]
    print('intermediate list = '+str(throws_expanded_p1))
    from functools import reduce
    throws_expanded_p2 = reduce(lambda a, b: a + b, throws_expanded_p1)
    print('removed_pins = '+str(throws_expanded_p2))
    pins_result = [0 if pin in throws_expanded_p2 else 1 for pin in pins]
    print(pins_result)

def bowling_throws5(n, throws):
    from functools import reduce
    throws_expanded = reduce(lambda a, b: a + b, [list(range(throw[0], throw[1] + 1)) for throw in throws])
    print([0 if pin in throws_expanded else 1 for pin in list(range(1, n + 1))])

bowling_throws5(12, [(1,3), (4,5), (7,10)])