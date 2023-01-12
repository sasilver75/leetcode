"""
You're playing the following Nim Game with your friend:

    * Initially, there is a heap of stones on the table
    * You and your friend will alternate taking turns, and YOU GO FIRST
    * On each turn, the person whose turn it is will remove 1-3 stones frmo the heap
    * The one who REMOVES THE LAST STONE is the winner

Given n, the number of initial stones, return TRUE if you can win the game
ASSUMING B OTH YOU AND YOUR FRIEND PLAY OPTIMALLY, otherwise return FALSE.
"""

def can_i_win(n: int) -> bool:
    # While there are stones left...
    while n > 0:
        """My Turn"""
        if n <= 3:
            return True
        else:
            # It seems like I'd love to give my opponent a turn at 4, since then they have to give it back to me at 3 or lower
            steps = max(1, n - (n // 3) * 3 + 1) # (distance from n to the closest multiple of 3 plus one...ie "4")
            n -= steps

        """My Opponent's Turn"""
        if n <= 3:
            return False
        else:
            steps = max(1, n - (n // 3) * 3 + 1) # (distance from n to the closest multiple of 3 plus one...ie "4")
            n -= steps


assert can_i_win(n=4) == False
assert can_i_win(n=1) == True
assert can_i_win(n=2) == True