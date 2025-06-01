from functools import reduce # Why import? it's  so basic! 

# Input: a number
# Output: "Even" or "Odd"
def even_odd(n):
    if n % 2 == 0: return "Even"
    else: return "Odd"


# Print numbers 1 to 100
# But if divisible by 3 → "Fizz", by 5 → "Buzz", by both → "FizzBuzz"
def fizz_buzz():
    for i in range(1, 101): 
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Input: list of numbers
# Output: the max value (without using max())
def find_max(arr):
    for i in range(len(arr)):
        max = arr[i]
        if arr[i] > max:
            max = arr[i]
    return max

# Input: "hello"
# Output: "olleh"
def remove_string(s):
    return s[1:]

# Input: string
# Output: number of vowels (a, e, i, o, u)
def count_vowels(s):
    count = 0
    for i in range(len(s)):
        if s[i] in "aeiou":
            count += 1
    return count

# Filtering in python
def filter_nums(n):
    # For practice, lets print even and odds
    even = list(filter(lambda num : num % 2 == 0, n))
    odd = list(filter(lambda num : num % 2 != 0, n))
    print(even)
    print(odd)

# Maps in python
def double_nums(n):
    print(list(map(lambda num : num * 2, n)))

# Reduce in python
def sum_nums(n):
    print(reduce(lambda a, b: a + b, n))

# Output: sum of all numbers below 1000 divisible by 3 or 5
def sum_nums_with_extra_logics(n):
    # 1: Filter to be under 1000
    range_filter = filter(lambda num: num < 1000, n)
    # 2: Filter to be divisible by 3 or 5; its OR!
    # Or is not || in py xD
    math_filter = filter(lambda num: num % 3 == 0 or num % 5 == 0, range_filter)
    # 3: Sum all the filtered items using reducer ofc 
    return reduce(lambda a, b: a + b, math_filter)

# Input: "racecar"
# Output: True if it's a palindrome
def is_palindrome(string):
    return string == string[::-1]

