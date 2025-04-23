class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name #n -> p1_name
        self.p2_name = player2_name #n -> p2_name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, player_name): # zmiana n na player_name
        if player_name == self.p1_name: # usunięcie zmiennej hard-coded "player1"
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            score_names = ["Love", "Fifteen", "Thirty", "Forty"] # p -> score_names
            player1_score = score_names[self.p1] # n -> player1_score
            return player1_score + "-All" if (self.p1 == self.p2) else player1_score + "-" + score_names[self.p2]
        else:
            if self.p1 == self.p2:
                return "Deuce"
            winner_or_ahead_name = self.p1_name if self.p1 > self.p2 else self.p2_name # s -> winner_or_ahead_name
            return (
                "Advantage " + winner_or_ahead_name
                if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1)
                else "Win for " + winner_or_ahead_name
            )

    #------------dodane funkcje ----------
