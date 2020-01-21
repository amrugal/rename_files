import os
import re
from glob import glob

# directory with files to rename and text file with titles
# directory is sorted and titles also by occurring digits in both
work_dir = f"/home/adrian/Videos/work/"
titles_file = f"titles.txt"

# temporary lists to store processed lists, for each step
temp_list_a = []
temp_list_b = []
temp_list_c = []


# function that returns list with extracted digits and converted to integers
def sort_key(line):
    result = []
    for part in re.findall(r'\d+', line):
        result.append(int(part, 10))
    return result


def main():
    # load file line by line into list
    with open(work_dir+titles_file, 'r') as file:
        loaded_file = file.readlines()
    print(f"LOADED ELEMENTS FROM FILE: {loaded_file}")

    # remove unwanted lines with specified pattern
    for line in loaded_file:
        if not re.search("##", line):
            temp_list_a.append(line)
    print(f'CLEANED LIST FROM LINES WITH "##: "{temp_list_a}')

    # remove list elements with "\n" (empty lines)
    for line in temp_list_a:
        if not line == "\n":
            temp_list_b.append(line)
    print(f'CLEANED LIST FROM EMPTY LINES: {temp_list_b}')

    # remove trailing "\n" (new line) to avoid putting it into renamed files new filename
    for line in temp_list_b:
        temp_list_c.append(line.rstrip("\n"))
    print(f'CLEANED LIST FROM TRAILING "\\n": {temp_list_c}')

    # list files in directory with trailing ".mp4" in filename
    files_in_dir = (glob(work_dir + "*.mp4"))
    print(files_in_dir)

    # "number" variable is used to indicate each title form list (list[0])
    number = 0
    # sorting file names in directory with sorted() and custom regex key and
    # replacing white spaces and dots with underscore
    # os.rename() function takes source(old_file_dir+old_name) and destination(new_file_dir+new_name)
    for item in sorted(files_in_dir, key=sort_key):
        # each new file name is build for os.rename destination argument
        new_filename = temp_list_c[number].replace(".", "").replace(" ", "_")
        print(item, f'{work_dir}{new_filename}')
        # the number of files needs to be exactly the same as number of titles in prepared list
        # os.rename(item, work_dir)
        number += 1


if __name__ == '__main__':
    main()
