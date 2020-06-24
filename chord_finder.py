''' Python Script to
        - Find chords in a certain key
        - Find the keys of the given chord
        - Find chords based on the given notes
'''

import key_finder
import random


notes = key_finder.notes
key_note_seq = key_finder.key_note_seq
key_type_short = key_finder.key_type_short


'''
C C# D D# E F F# G G# A A# B C
1 2  3 4  5 6
C D E F G A B C D E  F  G  A  B
1 2 3 4 5 6 7 8 9 1o 11 12 13 14


Major - 1,3,5 - C E G
Minor - 1,2,5 - C D# G *
Diminished - 1,2,4 - C D# F# *
Major Seventh - 1,3,5,7 - C E G B
Minor Seventh - 1,2,5,6 - C D# G A# *
Dominant Seventh - 1,3,5,6 - C E G A# *
Suspended2 - 1,2-,5 - C D G *
Suspended4 - 1,3+,5 - C F G corr
Augmented - 1,3,6 - C E G# *


'''


chord_seq = {
    "Major": "1,3,5",
    "Minor": "1,2,5",
    "Diminished": "1,2,4",
    "Major Seventh": "1,3,5,7",
    "Minor Seventh": "1,2,5,6",
    "Dominant Seventh": "1,3,5,6",
    "Half Diminished": "1,2,4,6",
    "Suspended2": "1,2-,5",
    "Suspended4": "1,3+,5",
    "Augmented": "1,3,6",
}

all_chord_types = [i for i in chord_seq.keys()]


def make_chord(root_notes, ctype):
    '''
    Generate chords of the given types for all the root notes given
    '''
    global chord_seq, notes

    if type(ctype) == str:
        ctype = [ctype, ]
    else:
        ctype = list(ctype)

    if type(root_notes) == str:
        root_notes = [root_notes, ]

    chord_strings = {}

    for root_note in root_notes:
        chord_strings[root_note] = {}
        for t in ctype:
            # Get the chord sequence
            cseq = chord_seq[t]
            chord_strings[root_note][t] = [root_note, ]
            # Keep note count for getting the notes from the octaves list
            note_count = 1
            # Get the major key of the root note so that the relative chord can be made
            major_key = key_finder.generate_keys(root_note)[0]['Major']

            for num in (cseq.split(',')[1::]):
                # cseq.split(',')[1::] because the root note is already put in
                if num in "3,5,7":
                    k = int(num)
                    chord_strings[root_note][t].append(major_key[k-1])
                elif num in "2,6":
                    k = int(num)
                    # append the note before the major key index of k such as 3,5,7
                    chord_strings[root_note][t].append(
                        notes[(notes.index(major_key[k]))-1])
                elif num == "2-":
                    k = 2
                    # append 2 notes before the major key index of k such as 3,5,7 [for suspended2]
                    chord_strings[root_note][t].append(
                        notes[(notes.index(major_key[k]))-2])
                elif num == "3+":
                    k = 3
                    # append 1 notes after the major key index of k such as 3,5,7 [for suspended4]
                    chord_strings[root_note][t].append(
                        notes[(notes.index(major_key[k]))])
                elif num == "4":
                    k = int(num)
                    chord_strings[root_note][t].append(
                        notes[(notes.index(major_key[k]))-1])

    return chord_strings


def chords_in_key(key):
    '''
    Returns dictionary of all the chords in a given key
    '''
    compatible_chords = {}
    for note in key[0:6]:
        all_chords = make_chord(note, all_chord_types)

        for cname, cnotes in all_chords[note].items():
            b = 0
            for n in cnotes:
                if n in key:
                    b += 0
                else:
                    b += 1
            if b == 0:
                chord_name = key_finder.uid(cname, note)
                compatible_chords[chord_name] = cnotes
    return compatible_chords


def find_chord(chord):
    '''
    Returns dictionary of all compatible chord names for the given notes 
    '''
    compatible_chords = {}
    for note in chord:
        all_chords = make_chord(note, all_chord_types)
        for cname, cnotes in all_chords[note].items():
            b = 0
            for n in cnotes:
                if n in chord:
                    b += 0
                else:
                    b += 1
            if b == 0:
                chord_name = key_finder.uid(cname, note)
                compatible_chords[chord_name] = cnotes
    return compatible_chords


def r_p_g(key, no):
    '''
    Returns a random chord progression of the given key and number of chords
    '''
    compatible_chords = chords_in_key(key)
    # Will return randomly chosen keys of the compatible chords
    generated_prog_keys = random.sample(list(compatible_chords.keys()), no)
    prog = {}
    for i in generated_prog_keys:
        prog[i] = compatible_chords[i]

    return prog
