"""
The Elf finishes helping with the tent and sneaks back over to you.
 "Anyway, the second column says how the round needs to end:

  X means you need to lose,
   Y means you need to end the round in a draw,
    and Z means you need to win.

     Good luck!"

The total score is still
calculated in the same way,
 but now you need to figure out
  what shape to choose so the round
  ends as indicated.

Following the Elf's instructions for the second column,
what would your total score be if everything goes exactly
 according to your strategy guide?

"""

# Result: { TheirMove: YourMove }
MOVE_LOOKUP = {
    "X": { # WE NEED TO LOSE
        "A": "C",
        "B": "A",
        "C": "B",
    },
    "Y": { # WE NEED TO TIE
        "A": "A",
        "B": "B",
        "C": "C"
    },
    "Z": { # WE NEED TO WIN
        "A": "B",
        "B": "C",
        "C": "A"
    }
}

SHAPE_POINTS = {
    "A": 1,
    "B": 2,
    "C": 3,
}

WIN_POINTS = {
    "X": 0, # Lose
    "Y": 3, # Draw
    "Z": 6 # Win
}

with open("inputs/2a.txt", "r") as f:
    rounds = [game.split(" ") for game in f.read().splitlines()]

    score = 0
    for opp_move, result in rounds:
        our_move = MOVE_LOOKUP[result][opp_move]
        score += SHAPE_POINTS[our_move]
        score += WIN_POINTS[result]

    print(score)


