"""List Assessment 

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """

    return [number for number in numbers if number%2 != 0]

# # Alternative solution
# def all_odd(numbers):
#     result = []
#     for number in numbers:
#         if number%2 != 0:
#             result.append(number)
#     return result


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

        >>> print_indices(["Toyota", "Jeep", "Toyota", "Volvo"])
        0 Toyota
        1 Jeep
        2 Toyota
        3 Volvo
    
    """

    cnt = 0
    for item in items:
        print str(cnt)+" "+item
        cnt += 1

    ## Alternative solution (Due to the assignment description, not used.)
    # for i, v in enumerate(items):
    #      print str(i)+" "+ v

    # I was trying to make it one line, but could not succeed
    # Is there a way to iterate in one line without making it a list?
    # print [(i, v) for i, v in enumerate(items)]



def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale", "zebra cakes"],
        ...     ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake" ]
        ... )
        ['bagel', 'cake', 'cheese', 'kale']
        
    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """

    # Solution 1 (built in sorted used)
    # return sorted(list(set(foods1) & set(foods2)))

    ##Solution 2 (built in sort used)
    # a = list(set(foods1) & set(foods2))
    # a.sort()
    # return a

    ## Solution 3 (built in append/sorted used)
    # result = []
    # for item in foods1:
    #     if item in foods2:
    #         result.append(item)
    # return sorted(result)

    # # Solution 4 (built in del used)
    # intersection = [food for food in foods1 if food in foods2]
    # for i in range(0,len(intersection)-1):
    #     if intersection[i]>intersection[i+1]:
    #         intersection += [intersection[i]]
    #         del intersection[i]
    # return intersection

    # Solution 5 (set used, built-in del used)
    intersection = list(set(foods1) & set(foods2))
    for i in range(0,len(intersection)-1):
        prev = intersection[i]
        current = intersection[i+1]
        if prev>current:
            intersection += [prev]
            del intersection[i]
    return intersection


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """

    # # Solution 1 (built in function index used)
    # return [item for item in items if items.index(item)%2==0]

    # Solution 2 (no built in function used)
    result = []
    for every_other_index in range(0,len(items),2):
        result+=[items[every_other_index]]
    return result


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """

    # Solution 1 (Built in function sorted used)
    if n ==0: return []
    return sorted(items)[-n:]

    # # Solution 2 (No built in function used.)
    #small_to_larges = []
    #for i in range(0:len(items)-1):
    #   for j in range(0:len(larger_list)-1)       
    #       if items[i]<items[i+1]:
    #       
    # return items[:n]


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
