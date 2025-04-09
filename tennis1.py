class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name: # usunięcie zmiennej hard-coded "player1"
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        result = ""
        if self.p1points == self.p2points:
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")
        elif self.p1points >= 4 or self.p2points >= 4: # Wyekstraktowanie if-else do osobnej funkcji
            result = self.advantage_or_win()
        else:
            result = self.standard_score() # Wekstraktowanie do osobnej funkcji
        return result
    

    #-----------------Dodane funkcje------------------
    
    def standard_score(self):
        result = ""
        for player in range(1, 3): # zmiana nic niemówiącej zmiennej (Mysterious Name)
            if player == 1:
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[self.p1points]
            else: # Usunięcie zmiennych temp i skrócenie zapisu (Temporary Field)
                result += ("-" + {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[self.p2points])
        return result
    
    def advantage_or_win(self):
        minus_result = self.p1points - self.p2points
        if minus_result == 1:
            result = "Advantage player1"
        elif minus_result == -1:
            result = "Advantage player2"
        elif minus_result >= 2:
            result = "Win for player1"
        else:
            result = "Win for player2"

        return result
