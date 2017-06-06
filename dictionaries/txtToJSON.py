# -*- coding: utf-8 -*-
import json
import sys
import io
from pprint import pprint
file = io.open('dict.json', 'r', encoding='utf-8-sig')
data = json.load(file)
o = open("e.txt", "w", encoding='utf-8')
for item in data['boosters']:
    print(item, data['boosters'][item], file=o)
file.close()
o.close()