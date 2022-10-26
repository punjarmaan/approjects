import csv
import sys
import pandas as pd


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Error Usage")
        exit(1)

    # Read database file into a variable
    data = []
    database = open(sys.argv[1], "r")
    dataReader = csv.DictReader(database)
    strs = dataReader.fieldnames[1:]
    row_ct = 0
    for row in dataReader:
        data.append(row)
        row_ct += 1

    items = len(data[0])

    # Read DNA sequence file into a variable
    seq = open(sys.argv[2], "r")
    seqString = seq.read()

    # Find longest match of each STR in DNA sequence
    matchCount = []

    for item in strs:
        matchCount.append({item: str(longest_match(seqString, item))})

    # Check database for matching profiles
    for line in dataReader:
        if match(strs, matchCount, line):
            print(f"line['name']")
            exit(0)
        else:
            continue

    database.close()
    seq.close()

    print("No match")
    exit(1)


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

def match(strs, matchCount, row):
    for item in strs:
        if matchcount[item] != int(row[item]):
            return False
    return True

main()
