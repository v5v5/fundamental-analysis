def find_imports_in_pyfile(filename):
    from pathlib import Path
    # filename = 'main.py'
    with open(Path('.') / filename, 'r') as file:
        lines = file.readlines()
    # to get name of module needs to get 2nd group from this regex
    regex_extract_imports = r'^(?!\s*#)\s*(import|from)\s+(\w*)'
    import re
    imports = set(filter(lambda l: l != None, map(
        lambda l: re.search(regex_extract_imports, l), lines)))
    importnames = set(map(lambda i: i.group(2), imports))
    importnames = set(filter(lambda f: not (Path(f + '.py')).exists(), importnames))
    return importnames

def find_all_pyfiles():
    from pathlib import Path
    files = set(map(lambda p: str(p), list(Path('.').glob(r'**/*.py'))))
    excludes = {'.venv', '.vscode'}
    files = {f for f in files if all(not f.startswith(e) for e in excludes)}
    return files

def get_requirements():
    files = find_all_pyfiles()
    requirements = set()
    for f in files:
        imports = find_imports_in_pyfile(f)
        requirements.update(imports)
    requirements_not_installed = set()
    for r in requirements:
        try:
            import importlib
            importlib.import_module(r)
        except:
            requirements_not_installed.add(r)
    return requirements_not_installed


def create_requirements():
    import os
    with open('requirements.txt', 'w') as f:
        for r in get_requirements():
            f.write(r)
            f.write('\n')

if __name__ == '__main__':
    create_requirements()
