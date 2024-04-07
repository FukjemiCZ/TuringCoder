import os
from pathlib import Path
from .ignore_handler import load_ignore_patterns, match_pattern

def add_file_content(APP_DIR, output_file, file_path):
    relative_path = os.path.relpath(file_path, APP_DIR)
    with open(output_file, 'a') as f:
        f.write(f"# {relative_path}\n\n```\n")
        with open(file_path, 'r') as content_file:
            f.write(content_file.read())
        f.write('\n```\n\n')

def process_files(APP_DIR, output_file):
    ignore_patterns = load_ignore_patterns(APP_DIR)

    # Zpracování souborů v aplikaci
    for root, dirs, files in os.walk(APP_DIR):
        paths_to_ignore = [os.path.join(root, d) for d in dirs] + [os.path.join(root, f) for f in files]
        dirs[:] = [d for d in dirs if not match_pattern(os.path.join(root, d), ignore_patterns)]  # Modifier pro os.walk
        for file in files:
            file_path = os.path.join(root, file)
            if not match_pattern(file_path, ignore_patterns):
                add_file_content(APP_DIR, output_file, file_path)