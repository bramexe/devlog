import json
from argparse import ArgumentParser
from pathlib import Path


notes_path = Path(__file__).with_name("notes.json")

parser = ArgumentParser(description="Manage your devlog")
commands = parser.add_subparsers(dest="command", required=True)

add_parser = commands.add_parser("add", help="add a devlog entry")
add_parser.add_argument("--minutes", "--min", dest="minutes", type=int,
                        help="minutes spent")
add_parser.add_argument("--topic", "--tpc", help="entry topic")
add_parser.add_argument("--note", "--nte", help="entry notes")

commands.add_parser("list", help="list all devlog entries")

args = parser.parse_args()


def load_notes():
    try:
        contents = notes_path.read_text().strip()
    except FileNotFoundError:
        return []

    if not contents:
        return []

    try:
        notes = json.loads(contents)
    except json.JSONDecodeError as exc:
        parser.error(f"{notes_path.name} contains invalid JSON: {exc}")

    if not isinstance(notes, list):
        parser.error(f"{notes_path.name} must contain a JSON list")
    return notes


notes = load_notes()

if args.command == "add":
    entry = {
        key: value
        for key, value in vars(args).items()
        if key in ("minutes", "topic", "note") and value is not None
    }

    minutes = entry.get("minutes")
    if minutes is not None and (minutes > 959 or minutes < 1):
        parser.error("Minutes must be between 1 and 959")

    topic = entry.get("topic")
    if topic is None:
         parser.error('Topic empty!')

    if not entry:
        add_parser.error("provide at least one of --minutes, --topic, or --note")

    notes.append(entry)
    notes_path.write_text(json.dumps(notes, indent=2))
    print("Entry saved.")
elif args.command == "list":
    if not notes:
        print("No entries yet.")
    for index, entry in enumerate(notes, start=1):
        print(
            f"{index}. Topic: {entry.get('topic', '')}, "
            f"minutes: {entry.get('minutes', '')}, "
            f"note: {entry.get('note', '')}"
        )
