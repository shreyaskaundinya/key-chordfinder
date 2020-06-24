import chord_finder
import key_finder
import chord_theory


def print_nested(val, nesting=-5):
    if type(val) == dict:
        print('')
        nesting += 5
        for k in val:
            print(nesting * ' ', end='')
            print(k, end=' : ')
            print_nested(val[k], nesting)
    else:
        print(val)


def chords_menu():
    # Get all the root notes
    o = input(
        """Enter 
        g for chords of given notes
        k for chord in a given key 
        t for theory
        f for finding name of chord 
        r for random chord progression generator :"""
    )

    if o == "g":
        # get all the chords of a given note
        root_notes = tuple(
            input("Enter root notes separated with commas : ").split(","))

        # Get the chord types
        for i in range(len(chord_finder.all_chord_types)):
            print(i+1, chord_finder.all_chord_types[i])

        ctypeints = tuple(
            input("Enter all the numbers of the chord types you want : ").split(","))

        ctypes = []

        for i in ctypeints:
            c = int(i)
            ctypes.append(chord_finder.all_chord_types[c-1])

        chords = chord_finder.make_chord(root_notes, ctypes)
        print_nested(chords)

    elif o == "k":
        # get all the chords in the key of the given root note and key type
        root_note = input(
            "Enter root note of key :")
        root_note = (root_note,)
        keys = key_finder.generate_keys(root_note)
        print()
        print("ALL KEYS for {} : \n".format(root_note))
        count = 1
        for kname, knotes in keys[0].items():
            print(count, kname, knotes)
            count += 1

        ok = int(input(
            "Enter key number to get chords of that key :"))
        print()
        print()
        print()

        chords = chord_finder.chords_in_key(
            keys[0][key_finder.key_names[ok-1]])

        print(keys[0][key_finder.key_names[ok-1]])
        print_nested(chords)

    elif o == "t":
        # display chord theory
        theory = chord_theory.chords_theory()
        print(theory)

    elif o == "f":
        # get the name of the given chord
        chord = tuple(
            input("Enter the notes of the chord separated with commas : ").split(","))
        chord_names = chord_finder.find_chord(chord)
        print_nested(chord_names)

    elif o == "r":
        # recieve random chord progression of given key and no of chords
        root_note = input(
            "Enter root note of key :")
        root_note = (root_note,)
        keys = key_finder.generate_keys(root_note)
        print()
        print("ALL KEYS for {} : \n".format(root_note))
        count = 1
        for kname, knotes in keys[0].items():
            print(count, kname, knotes)
            count += 1

        ok = int(input(
            "Enter key number to get chords of that key :"))
        no = int(input("Enter the number of chords you desire :"))

        req_key = keys[0][key_finder.key_names[ok-1]]

        want = True

        while want == True:
            generated_prog = chord_finder.r_p_g(req_key, no)
            print_nested(generated_prog)
            print()
            want = bool(input(
                "Enter anything for more chord progressions of the same scale, click enter to exit : "))


def keys_menu():
    root_notes = tuple(
        input("Enter root notes separated with commas : ").split(","))
    keys = key_finder.generate_keys(root_notes)
    print()
    '''for i in range(len(root_notes)):
        print("ALL KEYS for {} : \n".format(root_notes[i]))
        for kname, knotes in keys[i].items():
            print(kname, knotes)
        print()'''

    for i in root_notes:
        print()
        print("ALL KEYS FOR  :", i)
        print_nested(keys[root_notes.index(i)])


c = input("Enter k for key related functions and c for chord related functions :")
if c == "k":
    keys_menu()
if c == "c":
    chords_menu()
