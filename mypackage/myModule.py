def top_n(items, n):
    """
    Return the top n items in an array in descending order
    args:
        items-array/list-like object
        n(int): number of items to return
    returns:
        array: top n items in descorder
    examples:
        top_n([8, 5, 3, 7, 4, 9], 3)
        >>> [9,8,7]
    """
    for i in range(n):  # keep sorting until we have the top n 
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:

                items[j],items[j+1] = items[j+1], items[j]  # swap the numbers
    
    top_n = items[-n:]

    return top_n[::-1]