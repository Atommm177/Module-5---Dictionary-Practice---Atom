# This program reads bloodTypes.txt and counts blood types using three
# dictionaries: one for the full blood type (like "A-pos"), one for
# just the letter (A, B, AB, O), and one for just the Rh factor
# (pos or neg). Each line in the file is one person, like "O-pos".
# The counts are printed at the end.

# Every dictionary starts with each key set to 0
full_counts = {
    "A-pos": 0, "A-neg": 0,
    "B-pos": 0, "B-neg": 0,
    "AB-pos": 0, "AB-neg": 0,
    "O-pos": 0, "O-neg": 0
}
letter_counts = {"A": 0, "B": 0, "AB": 0, "O": 0}
rh_counts = {"pos": 0, "neg": 0}

with open("bloodTypes.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue   # skip empty lines

        # split("-") breaks "O-pos" into ["O", "pos"]
        parts = line.split("-")
        letter = parts[0]
        rh = parts[1]

        full_counts[line] += 1
        letter_counts[letter] += 1
        rh_counts[rh] += 1

print("Counts by full blood type:")
for blood_type in full_counts:
    print(blood_type + ": " + str(full_counts[blood_type]))

print()
print("Counts by letter (ignoring Rh factor):")
for letter in letter_counts:
    print(letter + ": " + str(letter_counts[letter]))

print()
print("Counts by Rh factor (ignoring letter):")
for rh in rh_counts:
    print(rh + ": " + str(rh_counts[rh]))
