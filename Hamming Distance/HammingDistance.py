"""Hamming Distance Calculator"""
def hamming_distance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    # Use a logical XOR to return '1' where there's a difference.
    xor_bin = x ^ y
    distance = 0
    # While we still have a number to work through.
    while xor_bin > 0:
        distance += xor_bin & 1 # Where 'z' is 1.
        xor_bin >>= 1 # Shift to the next bit.
    return distance

# Hefty Unit Test
X = 680142203
Y = 1111953568
print(hamming_distance(X, Y))
