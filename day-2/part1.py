import os

safe_reports = 0

def decrease_tree(report1, report2):
    #Check if diff < 3
    if report1 - report2 < 4 and report1 - report2 > 0:
        return True
    else:
        return False

def increase_tree(report1, report2):
    #Check if diff > 3
    if report2 - report1 < 4 and report2 - report1 > 0:
        return True
    else:
        return False

with open ("day-2/input.txt") as f:
    lines = f.readlines()

    for line in lines:
        report = list(map(int, line.split()))
        if report[0] > report[1]:
            #Decrease tree
            for element in range(len(report)-1):
                print(report[element], report[element+1])
                if decrease_tree(report[element], report[element+1]) == False:
                    break
            else:
                safe_reports += 1

        elif report[0] < report[1]:
            #Increase tree
            for element in range(len(report)-1):
                print(report[element], report[element+1])
                if increase_tree(report[element], report[element+1]) == False:
                    break
            else:
                safe_reports += 1

print(safe_reports)
