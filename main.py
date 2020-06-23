import chord_finder
import key_finder
import pprint


def chords_menu():
    # Get all the root notes
    o = input("Enter g for chords of given notes and k for chord in a given key :")
    if o == "g":
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
        pp = pprint.PrettyPrinter(depth=6)
        pp.pprint(chords)

    elif o == "k":
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
        pp = pprint.PrettyPrinter(depth=6)
        pp.pprint(chords)


def keys_menu():
    root_notes = tuple(
        input("Enter root notes separated with commas : ").split(","))
    print(root_notes)
    keys = key_finder.generate_keys(root_notes)
    print()
    for i in range(len(root_notes)):
        print("ALL KEYS for {} : \n".format(root_notes[i]))
        for kname, knotes in keys[i].items():
            print(kname, knotes)
        print()


c = input("Enter k for key related functions and c for chord related functions :")
if c == "k":
    keys_menu()
if c == "c":
    chords_menu()
