#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!


def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        # Return False if the input file does not exist
        return False

    with open(path_reading, 'r') as infile:
        lines = infile.readlines()

    if not lines:
        # Write an empty output file if the input file is empty
        with open(path_writing, 'w') as outfile:
            pass
        return

    # Start processing lines
    output_lines = ["Firstname,Lastname"]

    for line in lines[1:]:  # Skip the header
        line = line.strip()
        if not line:
            # Add an empty line with a single comma for blank lines
            output_lines.append(",")
        elif ';' in line:
            # Handle format: lastname; firstname
            lastname, firstname = line.split(';', 1)
            output_lines.append(f"{firstname.strip()},{lastname.strip()}")
        else:
            # Handle format: firstname lastname
            parts = line.split(' ', 1)
            if len(parts) == 2:
                output_lines.append(f"{parts[0].strip()},{parts[1].strip()}")

    # Write the processed lines to the output file
    with open(path_writing, 'w') as outfile:
        outfile.write("\n".join(output_lines))


# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
INPUT_PATH = "task/my_data.txt"
OUTPUT_PATH = "task/my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")
