#PART A
def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body.
    return total                        # num=4, total=4; num=9, total=13; num=2, total=15; num=1, total=16

resultA = tally([4, 9, 2, 1])

#PART B
def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):        # Record each value of new_list and idx at the end of the loop body.
        new_list.append(nums[idx])        # new_list=[4], idx=0; new_list=[4,9], idx=1;
    return new_list                       # new_list=[4,9,2], idx=2; new_list=[4,9,2,1], idx=3
                                        # How does this loop differ from that above?
resultB = copy([4, 9, 2, 1])              # it creates a copy of the list as opposed to adding the values

#PART C
def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:                  # Record each value of new_list and value at the end of the loop body.
        new_list.append(value + 1)        # new_list=[5], value=4; new_list=[5,10], value=9;
    return new_list                       # new_list=[5,10,3], value=2; new_list=[5,10,3,2], value=1

resultC = increment_all([4, 9, 2, 1])