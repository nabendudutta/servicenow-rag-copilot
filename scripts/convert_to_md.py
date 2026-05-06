import json, os

with open("data/raw/incidents.json") as f:
    incidents = json.load(f)

os.makedirs("data/markdown", exist_ok=True)

for inc in incidents:
    content = f"""# {inc.get("number")}

**Short Description:** {inc.get("short_description")}
**Priority:** {inc.get("priority")}
**State:** {inc.get("state")}

## Description
{inc.get("description")}

## Resolution
{inc.get("close_notes")}
"""

    with open(f'data/markdown/{inc["number"]}.md', "w") as f:
        f.write(content)