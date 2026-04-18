'''
> Date Created: 18/04/2026
> Author: Ishaan Rastogi
> Purpose: Script to quickly update the Quick Index in README.md
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working

NOTES-
 To run it, type this in terminal:
 python Extras/update_index.py

'''

import os
import re
from pathlib import Path

def parse_file(filepath):
    purpose = "N/A"
    date_created = "N/A"
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # Read first 1000 characters to find the metadata header
            content = f.read(1000)
            
            purpose_match = re.search(r'(?:>\s*Purpose:|Purpose:)\s*(.+)', content, re.IGNORECASE)
            if purpose_match:
                purpose = purpose_match.group(1).strip()
                
            date_match = re.search(r'(?:>\s*Date Created:|Date:)\s*([\d\-/]+)', content, re.IGNORECASE)
            if date_match:
                date_created = date_match.group(1).strip()
    except Exception:
        pass
            
    return purpose, date_created

def natural_key(text):
    """
    Sorts strings containing numbers in a natural way (e.g. 2 comes before 10).
    Pads numbers with leading zeros for reliable string comparison.
    """
    return [f"{int(c):06d}" if c.isdigit() else c.lower() for c in re.split(r'(\d+)', str(text))]

def get_markdown_for_dir(base_dir_path, ext_list, project_root):
    path = project_root / base_dir_path
    if not path.exists(): 
        return ""
    
    # 1. Collect all matching files traversing the tree
    files = []
    for ext in ext_list:
        files.extend(path.rglob(f"*{ext}"))
        
    # 2. Group files by immediate relative directory acting as heading
    grouped_files = {}
    for f in files:
        try:
            rel_parent = f.parent.relative_to(path)
            group_name = str(rel_parent).replace('\\', '/')
            if group_name == ".":
                group_name = "(Root)"
        except ValueError:
            group_name = "(Root)"
            
        if group_name not in grouped_files:
            grouped_files[group_name] = []
        grouped_files[group_name].append(f)
        
    # 3. Sort groups and prioritize "(Root)" folder if it exists
    groups = sorted(list(grouped_files.keys()), key=natural_key)
    if "(Root)" in groups:
        groups.remove("(Root)")
        groups.insert(0, "(Root)")
        
    output = ""
    # 4. Generate markdown tables for each group
    for group in groups:
        if group != "(Root)":
            output += f"#### {group}\n\n"
            
        group_files = sorted(grouped_files[group], key=lambda f: natural_key(f.name))
        
        table = "| S. No. | File Name | Purpose | Date |\n| --- | --- | --- | --- |\n"
        s_no = 1
        for f_path in group_files:
            purpose, date = parse_file(f_path)
            display_name = f_path.name
            
            # Absolute to relative URL format for correct Markdown hyperlink
            rel_path = str(f_path.relative_to(project_root))
            link = rel_path.replace('\\', '/').replace(" ", "%20")
            
            table += f"| {s_no} | [{display_name}]({link}) | {purpose} | {date} |\n"
            s_no += 1
            
        output += table + "\n"
        
    return output

def update_readme():
    try:
        # Resolve the root automatically based on this script's location
        project_root = Path(__file__).parent.parent.resolve()
        readme_path = project_root / "README.md"
        
        if not readme_path.exists():
            print("README.md not found in the project root directory!")
            return

        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # The region bounds between which the markdown script gets generated
        start_marker = "## Quick Index"
        end_marker = "## Repository Map"
        
        start_idx = content.find(start_marker)
        if start_idx == -1: 
            print("'## Quick Index' not found in README.md")
            return
        start_idx += len(start_marker)
        
        end_idx = content.find(end_marker)
        if end_idx == -1: 
            print("'## Repository Map' not found in README.md")
            return
        
        # Build new index contents 
        new_index = "\n\n### 1. [Python](python/)\n\n"
        new_index += get_markdown_for_dir("python", [".py"], project_root)
        
        new_index += "### 2. [Java](src/)\n\n"
        new_index += get_markdown_for_dir("src", [".java"], project_root)
        
        # Inject our generated layout back between markers
        updated_content = content[:start_idx] + new_index + content[end_idx:]
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
            
        print("Successfully updated the Quick Index in README.md!")
        
    except Exception as e:
        print(f"Error occurred while updating README: {e}")

if __name__ == '__main__':
    update_readme()
