"""Judge Route Circle"""
def nav_tracker(moves):
    """
    :type moves: str
    :rtype: bool

    The sum of opposing moves indicates whether or not we made enough opposing
    moves to return to our original position.
    """
    return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")

TEST_CASE = "UD"
print(nav_tracker(TEST_CASE))
TEST_CASE = "LL"
print(nav_tracker(TEST_CASE))
