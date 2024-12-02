import os

with open ("day-1/input.txt") as f:
    lines = f.readlines()

    nums1 = [int(line.split()[0]) for line in lines]
    nums2 = [int(line.split()[1]) for line in lines]
    nums1.sort()
    nums2.sort()

    diff = 0
    for i in range(len(nums1)):
        if nums1[i] == nums2[i]:
            diff += 0
        elif nums1[i] > nums2[i]:
            diff += nums1[i] - nums2[i]
        elif nums2[i] > nums1[i]:
            diff += nums2[i] - nums1[i]
    print(diff)
