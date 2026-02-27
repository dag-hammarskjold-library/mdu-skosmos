import re
import json
import os

def extract_trans_calls(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    
    # Match pattern liks {{ "some text" | trans() }}
    pattern = r'{{\s"(.*)".*\s}}'
    matches = re.findall(pattern, content)

    return matches

def main():
    project_dir = "./skosmos/custom-templates/"

    files_with_matches = (
        os.path.join(root, file)
        for root, dirs, files in os.walk(project_dir)
        for file in files
        if file.endswith('.twig')
    )

    results = []

    for file_path in files_with_matches:
        matches = extract_trans_calls(file_path)
        results.append({
            'file': file_path,
            'matches': matches
        })

    print(json.dumps(results, indent=4))

if __name__ == "__main__":
    main()
