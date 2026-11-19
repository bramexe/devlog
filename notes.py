import json

with open("notes.json", "r+", encoding="utf-8") as notes_file:
    data = json.load(notes_file)
    new_note = input("New note: ").strip()

    if new_note:
        data.append(new_note)
        notes_file.seek(0)
        json.dump(data, notes_file, indent=2)
        notes_file.truncate()
        print("Note saved.")


