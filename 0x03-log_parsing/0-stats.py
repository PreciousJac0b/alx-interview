#!/usr/bin/python3

"""
Handles logs from the file 0-generator.py
"""

import fileinput
import sys


def print_output(passed_dict, file_size):
    """Handles printing the output in the required format."""
    print("File size: {}".format(file_size))
    passed_dict = dict(sorted(passed_dict.items()))

    for key, value in passed_dict.items():
        print("{}: {}".format(key, value))


def get_log():
    """Handles getting information from the log and is the main program"""
    file_size = 0
    status_code = {}
    track_state = False
    try:
        counter = 0
        for lines in fileinput.input():
            try:
                lines = lines.rstrip("\n")
                new_list = lines.split()

                if len(new_list) != 9:
                    continue

                if not new_list[-1].isdigit() or not new_list[-2].isdigit():
                    track_state = True
                    continue

                file_size += int(new_list[-1])
                status_code[int(new_list[-2])] = status_code.get(
                                                int(new_list[-2]), 0) + 1

                counter += 1

                if counter % 10 == 0:
                    print_output(status_code, file_size)

            except Exception as e:
                raise ValueError(e)

        if track_state is True:
            raise ValueError("Not a digit")

    except (KeyboardInterrupt, Exception) as e:
        print_output(status_code, file_size)
        sys.stderr.write("[stderr]: {}\n".format(e))
        sys.exit(1)

    print_output(status_code, file_size)


if __name__ == '__main__':
    get_log()
