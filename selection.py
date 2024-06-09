import random
from typing import List


def find_kth_smallest(arr: List[int], current: int):
    if current == 0:
        return arr[0]
    pivot = random.choice(arr)
    lefts = []
    pivots = []
    rights = []
    for num in arr:
        if num < pivot:
            lefts.append(num)
        elif num > pivot:
            rights.append(num)
        else:
            pivots.append(num)
    if current < len(lefts):
        return find_kth_smallest(lefts, current)
    current -= len(lefts)
    if current < len(pivots):
        return pivot
    current -= len(pivots)
    return find_kth_smallest(rights, current)


def main():
    nums = []
    for i in range(15):
        num = random.randrange(20, 100)
        nums.append(num)
    sorted_nums = sorted(nums)
    print(f"nums are:{nums}")
    print(f"sorted nums are:{sorted_nums}")
    print(f"the 10th smallest number is: {find_kth_smallest(nums, 9)}")


if __name__ == "__main__":
    main()
