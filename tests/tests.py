from mypackage import myModule

def test_top_n():
    """
    make sure the top_n function works correctly
    """
    assert myModule.top_n([9, 8, 6, 3, 4, 2, 1, 7], 3) == [9,8,7], "incorrect"
    assert myModule.top_n([7, 10, 6, 2,2,2,5], 3) == [10, 7, 6], "incorrect"
    assert myModule.top_n([5, 11, 17, 19, 25, 7], 2) == [25, 19], "incorrect"