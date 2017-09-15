"""Hamming Distance Calculator"""

def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    # Format to 8 binary bits:
        # {} places a variable into a string.
        # 0 takes the variable at argument position 0.
        # : adds formatting options for this variable.
        #   - (otherwise it would represent the decimal x or y).
        # 08 formats the number to eight digits zero-padded on the left.
        # b converts the number to its binary representation.
    str_x = '{0:08b}'.format(x)
    str_y = '{0:08b}'.format(y)

    # If of equal length...
    assert len(str_x) == len(str_y)
    # Pass both strings to zip. Iterate through and tally any differences.
    return sum(el_1 != el_2 for el_1, el_2 in zip(str_x, str_y))

X = 1
Y = 4
print(hammingDistance(X, Y))
