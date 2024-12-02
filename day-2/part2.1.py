def is_decreasing(report):
    for i in range(len(report) - 1):
        if not (0 < report[i] - report[i + 1] < 4):
            return False
    return True

def is_increasing(report):
    for i in range(len(report) - 1):
        if not (0 < report[i + 1] - report[i] < 4):
            return False
    return True

def is_safe(report):
    if is_increasing(report) or is_decreasing(report):
        return True
    return False

def can_be_safe_with_one_removal(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False

safe_reports = 0
new_safe_reports = 0

with open("day-2/input.txt") as f:
    lines = f.readlines()

    for line in lines:
        report = list(map(int, line.split()))
        
        if len(report) < 2:
            print("Report with only one element is not safe")
            continue
        
        if is_safe(report):
            safe_reports += 1
        elif can_be_safe_with_one_removal(report):
            new_safe_reports += 1

print("Safe reports:", safe_reports)
print("Reports safe with one removal:", new_safe_reports)
print ("Total reports:", safe_reports + new_safe_reports)
