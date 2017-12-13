"""
Given an integer value, print the associated word value.
"""

def int_to_text(num):
    """
    Find integer to string association.
    """
    single = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
              6: "Six", 7:"Seven", 8:"Eight", 9:"Nine"}

    tens = {10: "Ten", 11: "Eleven", 12: "Twelve", 13:"Thirteen",
            14: "Fourteen", 15:"Fifteen", 16:"Sixteen", 17: "Seventeen",
            18: "Eighteen", 19:"Nineteen"}

    double = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty",
              7: "Seventy", 8: "Eighty", 9: "Ninety"}

    if len(str(num)) == 1:
        return single[num]

    values = list(str(num))

    if values[0] == '1':
        return tens[num]

    return double[int(values[0])] + " " + single[int(values[1])]

# MAIN ###############

for i in range(0, 100):
    print(int_to_text(i))
