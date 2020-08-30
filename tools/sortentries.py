import re
import argparse
from pathlib import Path
from typing import List, Optional


def _find_next_entries(lineno: int, lines: List[str]) -> List[str]:
    entries = []

    while lineno < len(lines):
        line = lines[lineno]

        if not line:
            lineno += 1
            continue

        m = re.match(r"^- ", line)
        if m is None:
            break

        entries.append(line)
        lineno += 1

    return entries


def _parse_sort_key(line: str) -> Optional[str]:
    m = re.match(r"^<!-- sort_by:(?P<key>\S+) -->$", line)
    if m is None:
        return None
    return m.group("key")


def _by_entry_name(text: str) -> str:
    # NOTE: we assume name is inside a Markdown link, eg '[<name>](<url>)'.
    m = re.match(r"^- \[(?P<name>[^\]]+)\]", text)
    assert m is not None
    return m.group("name").lower()


def _by_entry_date(text: str) -> str:
    # NOTE: we don't require date to be a specific format.
    m = re.match(r"^- (?P<date>[\d-]+) -", text)
    if m is None:
        assert text.startswith("- _Undated_")
        return ""  # Put undated entries last.
    return m.group("date")


ENTRY_SORT_KEYS: dict = {
    "name": (_by_entry_name, {}),
    "date": (_by_entry_date, {"reverse": True}),
}


def _sort_entries(entries: List[str], key: str) -> List[str]:
    keyfunc, kwargs = ENTRY_SORT_KEYS[key]
    return sorted(entries, key=keyfunc, **kwargs)


def _check_entries(entries: List[str], sort_key: str) -> int:
    is_sorted = _sort_entries(entries, key=sort_key) == entries
    return 0 if is_sorted else 1


DESCRIPTION = f"""
Sort lists of entries in README.md.

Sorting is done according to comment lines left above the Markdown lists. For example:

```markdown
<!-- sort_by:name -->

- [Name 1](link1) - Description 1
- [Name 2](link2) - Description 2
- [Name 3](link3) - Description 3
```

Supported sort keys: {', '.join(ENTRY_SORT_KEYS)}
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter,  # Don't line-wrap the description.
    )
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    check = args.check

    readme = Path("README.md")
    lines = readme.read_text().splitlines()

    result = 0
    lineno = 0

    while lineno < len(lines):
        # Parse any sort command.
        line = lines[lineno]
        sort_key = _parse_sort_key(line)
        if sort_key is None:
            lineno += 1
            continue
        if sort_key not in ENTRY_SORT_KEYS:
            print(f"Line {lineno}: unknown sort key {sort_key!r}, skipping...")
            lineno += 1
            continue

        # Skip forward to a non-empty line (i.e. the first list bullet point).
        while True:
            lineno += 1
            line = lines[lineno]
            if line:
                break

        # Parse list of entries, then sort them.
        entries = _find_next_entries(lineno, lines)
        sorted_entries = _sort_entries(entries, key=sort_key)

        new_lineno = lineno + len(entries)

        if entries != sorted_entries:
            if check:
                print(
                    f"ERROR: {readme.absolute()}:{lineno}: entries not sorted by {sort_key!r}"
                )
                result = 1
            else:
                print(f"{readme.absolute()}:{lineno}: Fixing entries...")
                lines[lineno:new_lineno] = sorted_entries
                new_lineno = lineno + len(sorted_entries)

        lineno = new_lineno

        lineno += 1

    if check and result:
        print("\nSome entries are not sorted. Run 'scripts/lint' to fix.")

    if not check:
        readme.write_text("\n".join(lines) + "\n")

    return result


if __name__ == "__main__":
    exit(main())
