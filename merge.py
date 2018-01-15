import os
import os.path
from pathlib import Path

from fetchTweets import queries


dir_files = os.listdir()
output_files = [file for file in dir_files if file.startswith(
    'output') and file.endswith('.txt')]

MERGE_RANGE_START = 1
MERGE_RANGE_END = 5

file_categories = {}
for key in queries:
    file_categories[key] = []

for file in output_files:
    for key in file_categories:
        if key in file:
            index = file.find(key)
            n = int(file[6:index])
            if n >= MERGE_RANGE_START and n <= MERGE_RANGE_END:
                file_categories[key].append(file)
            break


for key in file_categories:
    file_name = 'merged' + key + '.txt'

    with open(file_name, 'w') as output:
        output.close()

    with open(file_name, 'a') as output:
        for file in file_categories[key]:
            with open(file, 'r') as input_file:
                for line in input_file:
                    if not line.startswith('\n') and not line.startswith('('):
                        output.write(line)

            input_file.close()

        output.close()