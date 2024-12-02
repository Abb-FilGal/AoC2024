import os

with open ("day-1/input.txt") as f:
    lines = f.readlines()

    nums1 = [int(line.split()[0]) for line in lines]
    nums2 = [int(line.split()[1]) for line in lines]
    score = 0
    apperance = 0

    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                apperance += 1
        score += apperance * nums1[i]
        apperance = 0

    print(score)
