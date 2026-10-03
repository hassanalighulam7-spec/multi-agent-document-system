import re

def clean_cell(text: str) -> str:
    text = text.replace("<br>", "\n").replace("**", "")
    text = re.sub(r"^#+\s*", "", text)
    return text.strip()

def markdown_table_to_dicts(text: str) -> list:
    """Markdown table ko list of dict mein badalta hai (header = keys)."""
    if not text:
        return []

    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [clean_cell(c) for c in line.strip("|").split("|")]
        # |---|---| wali separator line chhor dein
        if all(re.fullmatch(r":?-{3,}:?", c) for c in cells if c):
            continue
        rows.append(cells)

    if len(rows) < 2:
        return []

    header, body = rows[0], rows[1:]
    return [dict(zip(header, r)) for r in body]