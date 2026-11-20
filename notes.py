import json

class EmptyNoteError(Exception): pass

with open("notes.json", "r+", encoding="utf-8") as notes_file:
    try:
        data = json.load(notes_file)
        new_note = input("New note: ").strip()
    except FileNotFoundError as e:
        print(e)

    if new_note:
        if not new_note in data:
            try:
                data.append(new_note)
                notes_file.seek(0)
                json.dump(data, notes_file, indent=2)
                notes_file.truncate()
                print("Note saved.")
            except Exception as e:
                print(e)
        else:
            print('Already saved that')
    else:
        raise EmptyNoteError('Empty note')
