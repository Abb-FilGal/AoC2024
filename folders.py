import os

for i in range(1, 25):
    folder_name = f"day-{i}"
    os.mkdir(folder_name)
    for part in ["part1", "part2"]:
        file_name = f"{folder_name}/{part}.py"
        with open(file_name, "w") as f:
            pass
