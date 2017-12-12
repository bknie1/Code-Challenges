"""Finds the longest common prefix in a list of strings."""

def longest_common_prefix(strings):
    """
    Determines longest common prefix.
    """
    if not strings:
        return "" # No words, so empty.

    prefix = min(strings, key=len) # Uses the shortest length string.

    for i, char in enumerate(prefix): # Index: value of prefix.
        for word in strings:
            if word[i] != char: # Iterate through until we hit our difference.
                return prefix[:i] # Slice just before our difference.
    return prefix

# MAIN

STRINGS = ["leets", "leetcode", "leet", "leeds"]

print(longest_common_prefix(STRINGS))
