import csv
import sys
from sys import argv


def main():


    # TODO: Check for command-line usage
    if len(argv) == 3:
        databaseinput = argv[1]
        sequenceinput = argv[2]
        #print(databaseinput)
        #print(sequenceinput)
    else:
        print("Invalid Command line")
        sys.exit()

    # TODO: Read database file into a variable

    databaserows = []
    sequencerows = []

    with open(databaseinput) as file:
        reader = csv.DictReader(file)
        #print(reader.fieldnames)
        for row in reader:
            databaserows.append(row)

    #print (databaserows)


    # TODO: Read DNA sequence file into a variable

    with open(sequenceinput) as file:
        sequencefromfile = file.read().strip()

    #print (sequencerows)

    # TODO: Find longest match of each STR in DNA sequence
    sequencesinfile = {}
    for subsequence in databaserows[0]:
        if subsequence == "name":
            continue
        else:
            #print ("err")
            #print (subsequence)

            #print (people)
            #print (subsequence)
            longest = longest_match(sequencefromfile, subsequence)
            sequencesinfile[subsequence] = longest
            #print(f"Sequence {subsequence} count: {longest}")

    #print (sequencesinfile)


    countofsubsequences = 0
    for subsequence in sequencesinfile:
        countofsubsequences = countofsubsequences + 1
        #print (countofsubsequences)

    peoplematchs = []
    for people in databaserows:

        peoplepartialmatchs = []
        for subsequence in sequencesinfile:
            #print ( people[subsequence])
            #print (sequencesinfile[subsequence])
            expectedcount = int(people[subsequence])
            realcount = int(sequencesinfile[subsequence])
            if realcount == expectedcount:
                peoplepartialmatchs.append(people[subsequence])

            if len(peoplepartialmatchs) == countofsubsequences:
                peoplematchs.append(people['name'])

    if len(peoplematchs) == 0:
        print("No match")
    else:
       print(peoplematchs[0])

    return


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

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


main()
