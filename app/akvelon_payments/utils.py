"""
Function to return n’th number of Fibonacci sequence
"""


def fibonacci(number: int) -> int:
    if not is_valid(number):
        raise ValueError('You entered an unavailable number, please enter an integer from 0 to 100')

    n1, n2 = 0, 1
    sequence = [n1, n2]

    for i in range(0, 100):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        sequence.append(n3)

    return (sequence[number])


def is_valid(number):
    if number < 0:
        return False
    if number > 100:
        return False
    return True


print(fibonacci(0))  # 0
print(fibonacci(6))  # 8
print(fibonacci(7))  # 13
