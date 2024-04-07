from pathlib import Path

def load_ignore_patterns(app_dir):
    ignore_file = Path(app_dir) / '.turingignore'
    if ignore_file.exists():
        with open(ignore_file, 'r') as file:
            patterns = file.read().splitlines()
            # odstranění prázdných řádků a komentářů
            patterns = [p for p in patterns if p and not p.startswith('#')]
            return patterns
    return []

def match_pattern(path, patterns):
    from fnmatch import fnmatch
    return any(fnmatch(path, pattern) for pattern in patterns)
