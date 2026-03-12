import csv
import json
import os
import re
import pandas

locale_folder = './skosmos/resource/translations/'
csv_path = 'translations.csv'

message_keys = set()
data = {}

for file_name in os.listdir(locale_folder):
    match_obj = re.match(r'messages.([a-z][a-z]).json', file_name)

    if file_name.endswith('.json'):
        lang = match_obj.group(1)
        with open(os.path.join(locale_folder, file_name)) as file:
            data[lang] = json.load(file)
    
df = pandas.read_json(data)

df.to_csv('combined_translations.csv', encoding='utf-8')