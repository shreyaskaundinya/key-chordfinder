'''Python script to generate keys and display them '''

import sys
import random

# All the notes

notes = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F',
         'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']

# Key sequences
'''
LEGEND : 
W - Whole step (2 semitones)
H - Half step (1 semitone)
S - Whole + half step (3 semitones)
'''

key_note_seq = {'Major': 'WWHWWWH',
                'Natural Minor': 'WHWWHWW',
                'Harmonic Minor (Asc)': 'WHWWHSH',
                'Harmonic Minor (Desc)': 'WHWWHWH',
                'Melodic Minor (Asc)': 'WHWWWWH',
                'Melodic Minor (Desc)': 'WHWWHWW'
                }
# Short form names for each of the Key types
key_type_short = {'Major': 'M',
                  'Natural Minor': 'm',
                  'Harmonic Minor (Asc)': 'harmasc',
                  'Harmonic Minor (Desc) ': 'harmdesc',
                  'Melodic Minor (Asc)': 'melmasc',
                  'Melodic Minor (Desc)': 'melmdes'}

key_names = [
    'Major',
    'Natural Minor',
    'Harmonic Minor (Asc)',
    'Harmonic Minor (Desc)',
    'Melodic Minor (Asc)',
    'Melodic Minor (Desc)'
]


def uid(keyname, note):
    return note+" "+keyname


def note_picker(note_sequence, root_note):
    '''
    Prepares the keys using the keys sequence using (Whole step/Half step/whole+half step)
    Returns the key of the given key type of the given root note
    '''
    global notes

    # multiple octave notes

    mon = notes+notes+notes+notes

    # root note index

    counter = 0
    for i in notes:
        if root_note == i:
            counter = notes.index(i)
            break
        elif root_note in i:
            counter = notes.index(i)

    # whole step and half step and whole+half step

    w = 2
    h = 1
    s = 3

    notes_in_key = []

    # appending root note
    notes_in_key.append(mon[counter])

    for i in note_sequence:
        if i == "W":
            counter += w
            notes_in_key.append(mon[counter])
        elif i == "H":
            counter += h
            notes_in_key.append(mon[counter])
        elif i == "S":
            counter += s
            notes_in_key.append(mon[counter])

    return notes_in_key


def note_validator(note):
    '''
    Validates if the given note exits in the musical notations
    '''
    global notes

    for i in notes:
        if note in i:
            return True
    else:
        return False


def generate_keys(root_notes):
    '''
    Generates all key types for the root notes given in the parameter
    '''
    global key_note_seq
    keybunch = []

    for root_note in root_notes:
        # to store all the keys available for the particular root note
        allkeys = {
            'Major': [],
            'Natural Minor': [],
            'Harmonic Minor (Asc)': [],
            'Harmonic Minor (Desc)': [],
            'Melodic Minor (Asc)': [],
            'Melodic Minor (Desc)': []}

        # validate root note

        if note_validator(root_note) == True:
            pass
        else:
            print("Root note invalid")
            sys.exit()

        for k in allkeys.keys():
            if k == 'Major':
                allkeys['Major'] = note_picker(
                    key_note_seq['Major'], root_note)

            elif k == 'Natural Minor':
                allkeys['Natural Minor'] = note_picker(
                    key_note_seq['Natural Minor'], root_note)

            elif k == 'Harmonic Minor (Asc)':
                allkeys['Harmonic Minor (Asc)'] = note_picker(
                    key_note_seq['Harmonic Minor (Asc)'], root_note)

            elif k == 'Harmonic Minor (Desc)':
                allkeys['Harmonic Minor (Desc)'] = note_picker(
                    key_note_seq['Harmonic Minor (Desc)'], root_note)

            elif k == 'Melodic Minor (Asc)':
                allkeys['Melodic Minor (Asc)'] = note_picker(
                    key_note_seq['Melodic Minor (Asc)'], root_note)

            elif k == 'Melodic Minor (Desc)':
                allkeys['Melodic Minor (Desc)'] = note_picker(
                    key_note_seq['Melodic Minor (Desc)'], root_note)

        # return the keys
        keybunch.append(allkeys)
    return keybunch


def key_maker(start):
    global notes
    pass


'''
.
..
...
DATABASE UPDATATION
...
..
.
'''
