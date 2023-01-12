"""
Rock Paper Scissors Tournament

The winner of the whole tournament is the player with the highest score.
Your total score is the sum of your scores for each round.
The score for a single round is the score for the shape you selected
 (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome
of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Score = (Your Shape Choice) + (6 points if you won, or 3 if tied, else 0)


For example, suppose you were given the following strategy guide:

A Y
B X
C Z

Since you can't be sure if the Elf is trying to help you or trick you,
you should calculate the score you would get if you were
to follow the strategy guide.

First col: Opponent's Choice
A: Rock
B: Paper
C: Scissors

Second col: Our choice
X: Rock
Y: Paper
Z: Scissors

What would your total score be if everything goes exactly according
to your strategy guide?
"""

# All from our perspective
WIN_LOOKUP = {
    "X": "C",
    "Y": "A",
    "Z": "B",
}

TIE_LOOKUP = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

VALUE_LOOKUP = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

# Lose Lookup is not needed -- it's implied

if __name__ == "__main__":
    with open("inputs/2a.txt", "r") as f:
        rounds = [round.split(" ") for round in f.read().splitlines()] # [(them, me), ...]

        score = 0
        for opponent_move, our_move in rounds:
            score += VALUE_LOOKUP[our_move]
            if WIN_LOOKUP[our_move] == opponent_move:
                score += 6
            elif TIE_LOOKUP[our_move] == opponent_move:
                score += 3
            # Else 0 score for losing

        print(score)
