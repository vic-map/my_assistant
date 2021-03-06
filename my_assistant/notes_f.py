import json
from pathlib import Path
from sys import platform
import os


note_path = os.path.abspath('.') + "\\notes\\"


def write_note(arguments):
    title = arguments.split(sep=', ')[0]
    tags = arguments.split(sep=', ')[1].split(sep='; ')
    text = arguments.split(sep=', ')[2]
    note = {'name': title, 'tags': tags, 'text': text}
    message = dump_note(note)
    return message


def dump_note(note):
    path = note_path + note['name'] + '.json'
    with open(path, "w") as fh:
        json.dump(note, fh)
        message = f"note {note['name']} has been written"
    return message


def get_note(title):
    path = note_path + title + '.json'
    with open(path, 'r') as fh:
        note = json.load(fh)
    return note


def find_note(title):
    filename = title + '.json'
    message = 'there is no such note'
    for item in Path(note_path).iterdir():
        if item.name == filename:
            message = get_note(title)
    return message


def change_note(arguments):
    title = arguments.split(sep=', ')[0]
    text = arguments.split(sep=', ')[1]
    note = get_note(title)
    note['text'] = text
    dump_note(note)
    message = f"note {note['name']} has been changed"
    return message


def edit_note(name):
    filename = note_path + name + '.json'
    print('finish editing in external editor')
    if platform == "linux" or platform == "linux2":
        osCommandString = f"nano {filename}"
        os.system(osCommandString)
    elif platform == "darwin":
        osCommandString = f"Text Edit {filename}"
        os.system(osCommandString)
    elif platform == "win32":
        osCommandString = f"notepad.exe {filename}"
        os.system(osCommandString)
    return f'the note {name} has been adited'


def remove_note(title):
    path = Path(note_path + title + '.json')
    path.unlink()
    message = f'the note {title} has been removed'
    return message


def add_tag(arguments):
    title = arguments.split(sep=', ')[0]
    tag = arguments.split(sep=', ')[1]
    note = get_note(title)
    if tag in note['tags']:
        message = f'there is such tag in the note {title}'
    else:
        note['tags'].append(tag)
        dump_note(note)
        message = f'the tag {tag} was added to note {title}'
    return message


def remove_tag(arguments):
    title = arguments.split(sep=', ')[0]
    tag = arguments.split(sep=', ')[1]
    note = get_note(title)
    if tag in note['tags']:
        note['tags'].remove(tag)
        dump_note(note)
        message = f'the tag {tag} was removed from note {title}'
    else:
        message = f"the tag {tag} is not exist in note {title}"
    return message


def find_tag(tag):
    note_list = []
    for item in Path(note_path).iterdir():
        note = get_note(item.name.split(sep='.')[0])
        if tag in note['tags']:
            note_list.append(note['name'])
            message = f"the {tag} is in notes:\n {note_list}"
    return message


# def read_note(title):
#     filename = title + '.json'
#     for item in default_notes_path.iterdir():
#         if item == filename:
#             message = get_note(title)['text']
#     return message
