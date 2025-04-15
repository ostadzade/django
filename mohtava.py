import os
import re

def create_structure_from_text(text_file):
    with open(text_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match file sections
    pattern = r'=== (.*?) ===\n(.*?)(?=\n===|$)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for filepath, file_content in matches:
        # Create directory if not exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Write file content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(file_content.strip())
    
    print(f"Successfully created {len(matches)} files!")

# Usage
create_structure_from_text('accounting_module.txt')