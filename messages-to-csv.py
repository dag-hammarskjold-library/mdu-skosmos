import json
import os
import re
import pandas

locale_folder = './skosmos/resource/translations/'

message_keys = set()
data = {}

for file_name in os.listdir(locale_folder):
    match_obj = re.match(r'messages.([a-z][a-z]).json', file_name)

    if file_name.endswith('.json'):
        lang = match_obj.group(1)
        with open(os.path.join(locale_folder, file_name)) as file:
            messages = json.load(file)
            data[lang] = messages
            message_keys.update(messages.keys())
    
# Create DataFrame with 'key' as first column
df_data = {'key': sorted(message_keys)}
for lang in sorted(data.keys()):
    df_data[lang] = [data[lang].get(key, '') for key in sorted(message_keys)]

df = pandas.DataFrame(df_data)

df.to_csv('combined_translations.csv', encoding='utf-8', index=False)