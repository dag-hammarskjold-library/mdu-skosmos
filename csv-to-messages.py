import csv
import json
import os
import shutil

csv_file = 'combined_translations.csv'
locale_folder = './skosmos/resource/translations/'

# Create locale folder if it doesn't exist
os.makedirs(locale_folder, exist_ok=True)

# Backup existing messages files
for file_name in os.listdir(locale_folder):
    if file_name.startswith('messages.') and file_name.endswith('.json'):
        original_path = os.path.join(locale_folder, file_name)
        backup_path = original_path + '.bak'
        shutil.copy2(original_path, backup_path)
        print(f'Backed up {file_name} to {file_name}.bak')

# Initialize dictionaries for each language
languages = {}

# Read CSV and populate language dictionaries
with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        key = row['key']
        
        # Iterate through all columns except 'key'
        for lang, value in row.items():
            if lang != 'key' and value:  # Skip 'key' column and empty values
                if lang not in languages:
                    languages[lang] = {}
                languages[lang][key] = value

# Write JSON files for each language
for lang, messages in languages.items():
    file_path = os.path.join(locale_folder, f'messages.{lang}.json')
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(messages, file, ensure_ascii=False, indent=2)
    print(f'Generated {file_path}')

print(f'Successfully created {len(languages)} language files.')