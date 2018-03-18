import os
import os.path
from pathlib import Path
import json

dir_files = os.listdir('..')
output_files = [file for file in dir_files if file.startswith(
    'sentiments') and file.endswith('.txt')]

meta = {}
weeks = []
categories = []
for file in output_files:
    i = file.index('-')
    week = file[10:i]
    category = file[i+7:file.index('.txt')]
    weeks.append(week)
    categories.append(category)

for week in weeks:
    meta[week] = {}
    for category in categories:
        meta[week][category] = {}
        file_name = '../sentiments' + week + '-merged' + category + '.txt'
        max_index = -1
        with open(file_name, 'r') as sentiments:
            content = sentiments.read()

            for sentiment in content.split('\n\n'):
                if len(sentiment) > 0:
                    try:
                        i = sentiment.index(')')
                        indexPart = sentiment[2:i]

                        if len(indexPart) < 7:
                            index = int(indexPart)
                            if index > max_index:
                                max_index = index

                        meta[week][category]['tweets'] = max_index + 1
                    except ValueError:
                        error = None

                    splits = sentiment.split('\n')
                    if len(splits) == 2:
                        value = int(splits[1])

                        if value > 0:
                            if 'positives' not in meta[week][category].keys():
                                meta[week][category]['positives'] = 1
                            else:
                                meta[week][category]['positives'] += 1
                        elif value < 0:
                            if 'negatives' not in meta[week][category].keys():
                                meta[week][category]['negatives'] = 1
                            else:
                                meta[week][category]['negatives'] += 1
                        
            if 'tweets' not in meta[week][category].keys():
                meta[week][category]['tweets'] = 0
            if 'positives' not in meta[week][category].keys():
                meta[week][category]['positives'] = 0
            if 'negatives' not in meta[week][category].keys():
                meta[week][category]['negatives'] = 0
            
            sentiments.close()

result = json.dumps(meta)
with open('meta.js', 'w') as output_file:
    output_file.write('var meta = ' + result + ';')