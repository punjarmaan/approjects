import csv
import sys
import random
import math
import pandas as pd
import numpy as np


# w, h = 8, 69
# d = 2
# verb_conj = [[0 for x in range(h)] for y in range(w)]
# with open("Verbs.csv", "r") as file:
#     reader = csv.reader(file)
#     j = 0
#     for row in reader:
#         i = 0
#         # defin = row['definition']
#             # yo = row['yo']
#             # tú = row['tú']
#             # él_ella_ud = row['él/ella/ud']
#             # nosotros = row['nosotros']
#             # vosotros = row['vosotros']
#             # ellos_ellas_uds = row['ellos/ellas/uds']
#         verb_conj[i][j] = row[i]
#         verb_conj[i + 1][j] = row[i + 1]
#         verb_conj[i + 2][j] = row[i + 2]
#         verb_conj[i + 3][j] = row[i + 3]
#         verb_conj[i + 4][j] = row[i + 4]
#         verb_conj[i + 5][j] = row[i + 5]
#         verb_conj[i + 6][j] = row[i + 6]
#         verb_conj[i + 7][j] = row[i + 7]
#         j += 1

verbs_df = pd.read_csv("Verbs.csv")
verbs_np = verbs_df.to_numpy()
pns_arr = ['infinitive', 'definition', 'yo', 'tú', 'él/ella/ud', 'nosotros', 'vosotros', 'ellos/ellas/uds']
SIZE = len(verbs_np) - 1

def main():
        studyMode()


def verbCon():
    j = 0
    while j < 5:
        pn = random.randint(2, 7)
        infin_id = random.randint(0, SIZE)
        pronoun = pns_arr[pn]
        verb_id = verbs_np[infin_id][0]
        verb_ans = verbs_np[infin_id][pn]

        conj_answer = input(f"{pronoun} form of {verb_id}: ")

        answer = verbs_np[infin_id][pn]

        i = 0
        while i < 3:
            if conj_answer.lower() == answer:
                print(f"Correct! The {pronoun} form of {verb_id} is {verb_ans}.")
                break
            else:
                conj_answer = input("Try again: ")
            i += 1

        if i >= 3:
            print(f"Sorry! The correct {pronoun} form of {verb_id} is {verb_ans}.")

        j += 1

        if j % 5 == 0 and j > 0:
            next_s = input("Would you like to continue? ")
            if next_s.lower() in ["yes", "y", "es", "yeah", "yep"]:
                j = 0
            else:
                studyMode()


def verbDef():
    j = 0
    while j < 5:
        verb = random.randint(0, SIZE)
        verb_id = verbs_np[verb][0]
        def_id = verbs_np[verb][1]
        def_answer = input(f"What does {verb_id} mean? ").lower()

        i = 0
        while i < 3:
            if def_answer == verbs_np[1][verb]:
                print(f"Correct! {verb_id} means {def_id}")
                break
            else:
                def_answer = input("Try Again: ")
            i += 1

        if i >= 3:
            print(f"Sorry! {verb_id} means {def_id}")

        j += 1

        if j % 5 == 0 and j > 0:
            next_s = input("Would you like to continue? ")
            if next_s.lower() in ["yes", "y", "es", "yeah", "yep"]:
                j = 0
            else:
                studyMode()


def studyMode():
    mode = input("Select Study Mode (Verb Conjugation, Verb Definition, More to Come!, Exit): ")
    match mode:
        case "Verb Conjugation":
            print("Entering Verb Conjugation Study Mode...")
            verbCon()
        case "Verb Definition":
            print("Entering Verb Definition Study Mode...")
            verbDef()
        case "Exit":
            print("Have A Good Day!")
            exit()


if __name__ == "__main__":
    main()
