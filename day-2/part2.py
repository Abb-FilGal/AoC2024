import os
safe_reports = 0

def decrease_tree(report1, report2):
    if report1 - report2 < 4 and report1 - report2 > 0:
        return True
    else:
        return False

def increase_tree(report1, report2):
    if report2 - report1 < 4 and report2 - report1 > 0:
        return True
    else:
        return False

with open("day-2/test.txt") as f:
    lines = f.readlines()

    for line in lines:
        report = list(map(int, line.split()))
        print(f"Processing report: {report}")
        
        is_safe = False
        
        if report[0] > report[1]:
            # Decrease tree
            print("Checking decrease tree...")
            for element in range(len(report) - 1):
                if not decrease_tree(report[element], report[element + 1]):
                    print(f"Failed at elements: {report[element]}, {report[element + 1]}")
                    for i in range(len(report)):
                        fake_list = report[:i] + report[i+1:]
                        if all(decrease_tree(fake_list[j], fake_list[j + 1]) for j in range(len(fake_list) - 1)):
                            is_safe = True
                            print(f"Found safe configuration by removing index {i}: {fake_list}")
                            break
                        else:
                            print(f"Unsafe configuration by removing index {i}: {fake_list}")

            else:
                is_safe = True
                print("All elements passed decrease check.")

        elif report[0] < report[1]:
            # Increase tree
            print("Checking increase tree...")
            for element in range(len(report) - 1):
                if not increase_tree(report[element], report[element + 1]):
                    print(f"Failed at elements: {report[element]}, {report[element + 1]}")
                    for i in range(len(report)):
                        fake_list = report[:i] + report[i+1:]
                        if all(increase_tree(fake_list[j], fake_list[j + 1]) for j in range(len(fake_list) - 1)) or ():
                            is_safe = True
                            print(f"Found safe configuration by removing index {i}: {fake_list}")
                            break
                        else:
                            print(f"Unsafe configuration by removing index {i}: {fake_list}")
                            is_safe = False
                    if is_safe:
                        break
            else:
                is_safe = True
                print("All elements passed increase check.")

        if is_safe:
            safe_reports += 1
            print("Report is safe.")

print(f"Total safe reports: {safe_reports}")


