#PART A
more = [x + 1 for x in [1,2,3,4]]     # List, in order, the values that x takes at each step.
                                            # 1, 2, 3, 4
print()                               # What is the value of more at this point?
                                            # [2, 3, 4, 5]

#PART B
def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and each return value.
                                                # n=1, return 1; n=2, return 4; n=3, return 9; n=4, return 16
squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the values above?
print()                                         # squares=[1, 4, 9, 16] those are the return values for each n

#PART C
def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and each return value.
                                                # n=1, return False; n=2, return False; n=3, True; n=4, True; n=5, True
answerC = [x for x in range(5) if check(x)]   # What is the value of answer?
print()                                         # answer=[3, 4, 5]

#PART D
def inc(m:int) -> int:
    return m + 1                         # Record, in order of the calls, each value of m and each return value.
                                                # m=3, return 4; m=4, return 5; m=5, return 6
def check(n:int) -> bool:
    return n > 2                         # Record, in order of the calls, each value of n and each return value.
                                                # n=1, return False; n=2, return False; n=3, True; n=4, True; n=5, True
answerD = [inc(x) for x in range(5) if check(x)]   # What is the value of answer?
print()                                                 # answer = [4, 5, 6]