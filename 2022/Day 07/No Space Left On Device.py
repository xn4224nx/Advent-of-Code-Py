# -*- coding: utf-8 -*-
"""

--- Day 7: No Space Left On Device ---

To begin, find all of the directories with a total size of at most 100000,
then calculate the sum of their total sizes. In the example above, these
directories are a and e; the sum of their total sizes is 95437 (94853 + 584).
(As in this example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000.
What is the sum of the total sizes of those directories?

Created on Wed Dec  7 20:39:31 2022

@author: FAKENAME
"""

import re


def curr_fp(arr):

    if arr:
        return root_dir + "/".join(arr) + "/"

    else:
        return root_dir


# Command Variables
ls_com = "$ ls"
cd_com = "$ cd "
up_com = ".."

# Regex to extract folder and file info
file_re = r"(\d+) (\S+)"
dir_re = r"dir (\S+)"

# Root directory, the first cd dir in the file
root_dir = None

# Define the struture to store the file system infomation
filesys = {}

# An array that stores the curr directories file path
curr_dir_arr = None

# Temp Variables to store folder info
temp_subfolders = []
temp_filenames = []
temp_filesizes = []

# Load the instructions from disk and split the commands
instruct_ls = open("input.txt", "r").read().split('\n')[:-1]

# Loop over the instructions and create a directory structure
for instruct in instruct_ls:

    # Detect command
    if cd_com in instruct:

        mov_dir = instruct.replace(cd_com, "")

        # Assign Root Dir
        if not root_dir:
            root_dir = mov_dir

        # detect going up a level
        if mov_dir == up_com:
            curr_dir_arr.pop()

        # detect going back to root
        elif mov_dir == root_dir:
            curr_dir_arr = []

        # Detect going down a level
        else:
            curr_dir_arr.append(mov_dir)

        # Save the current folder info into `file_sys_dict`
        if curr_fp(curr_dir_arr) not in filesys:

            filesys[curr_fp(curr_dir_arr)] = {
                "Sub Dir": [],
                "File Nm": [],
                "File Sz": []
                }

        continue

    # Detect directory
    elif re.match(dir_re, instruct):

        sub_dir_name = re.search(dir_re, instruct).group(1)

        filesys[curr_fp(curr_dir_arr)]["Sub Dir"] \
            .append(curr_fp(curr_dir_arr + [sub_dir_name]))

    # Detect file
    elif re.match(file_re, instruct):

        file_name = re.search(file_re, instruct).group(2)
        file_size = int(re.search(file_re, instruct).group(1))

        filesys[curr_fp(curr_dir_arr)]["File Nm"].append(file_name)
        filesys[curr_fp(curr_dir_arr)]["File Sz"].append(file_size)

    # ls doesn't matter
    elif ls_com in instruct:
        pass

    # Raise error if it gets this far
    else:
        raise Exception(f"Unknown Instruction \"{instruct}\"")


# Traverse the structure and create a record of each folder and the size of
# everything within it.


# Dict to store the results in
ret_dict = {}

for dir_ in filesys:

    # Save the results
    ret_dict[dir_] = {
        "Deep Sz": 0,
        "Shal Sz": sum(filesys[dir_]["File Sz"])
        }

    # The size of the files in the folder and subfolder
    deep_size = 0

    # loop over the file system again
    for dir_2 in filesys:

        # Check that the folder is a sub dir
        if dir_2.startswith(dir_):

            deep_size += sum(filesys[dir_2]["File Sz"])

    ret_dict[dir_]["Deep Sz"] += deep_size


# Find all of the directories with a total size of at most 100000.
# What is the sum of the total sizes of those directories?

dir_sum = sum([f["Deep Sz"] for f in ret_dict.values() \
               if f["Deep Sz"] <= 100000])


total_disk_space = 70000000

space_needed = 30000000

space_used = sum([f["Shal Sz"] for f in ret_dict.values()])

min_size_of_dir = space_needed - (total_disk_space - space_used)

best_cand = 3000000000000000

for dir_ in ret_dict:

    if ret_dict[dir_]["Deep Sz"] < best_cand and ret_dict[dir_]["Deep Sz"] > min_size_of_dir:

        best_cand = ret_dict[dir_]["Deep Sz"]
