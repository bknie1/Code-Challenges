"""Prints Fizz if n % 3, Buzz if n % 5, Fizz Buzz if n % 15."""
def fizz_buzz(target):
    result = []
    for i in range(1, target + 1):

        if not i % 3 and not i % 5:
            result.append("FizzBuzz")
            continue

        elif not i % 3:
            result.append("Fizz")
            continue

        elif not i % 5:
            result.append("Buzz")
            continue

        else:
            result.append(i)
    return result

print(fizz_buzz(15))
