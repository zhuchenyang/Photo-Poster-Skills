"""Build one poster skill ZIP, with no publishing or network side effects."""
import argparse
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skill')
    parser.add_argument('version')
    args = parser.parse_args()
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.skill):
        parser.error('Use a lowercase hyphenated skill directory name')
    if not re.fullmatch(r'\d+\.\d+(?:\.\d+)?(?:-[a-zA-Z0-9.-]+)?', args.version):
        parser.error('Invalid version')
    root = Path(__file__).resolve().parents[1]
    source = root / 'posters' / args.skill
    skill_file = source / 'SKILL.md'
    if not skill_file.is_file():
        parser.error('Skill not found under posters/')
    text = skill_file.read_text(encoding='utf-8')
    frontmatter = re.match(r'\A---\s*\n(.*?)\n---', text, re.S)
    version = re.search(r'^\s+version:\s*[\"\x27]?([^\s\"\x27]+)', frontmatter.group(1), re.M) if frontmatter else None
    if not version or version.group(1) != args.version:
        parser.error('Version must match SKILL.md metadata.version')
    files = sorted(p for p in source.rglob('*') if p.is_file())
    if any(p.is_symlink() for p in source.rglob('*')):
        parser.error('Symlinks are not supported in release packages')
    files = [p for p in files if not any(part in {'.git', '__pycache__', '.DS_Store'} for part in p.relative_to(source).parts)]
    destination = root / 'dist' / f'{args.skill}-v{args.version}.zip'
    destination.parent.mkdir(exist_ok=True)
    if destination.exists():
        parser.error(f'Package already exists: {destination}')
    with ZipFile(destination, 'w', ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, Path(args.skill) / path.relative_to(source))
    print(destination)


if __name__ == '__main__':
    main()
