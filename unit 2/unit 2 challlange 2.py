class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Example usage
batsman = Batsman()
batsman.play()  # Output: The batsman is batting.

bowler = Bowler()
bowler.play()  # Output: The bowler is bowling.
