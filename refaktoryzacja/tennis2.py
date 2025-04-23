class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name: # usunięcie zmiennej hard-coded "player1"
            self.p1_score()
        else:
            self.p2_score()

    def score(self):
        result = ""
        if self.p1points == self.p2points and self.p1points < 3:
            _, result = self.players_results() # Dodanie funkcji
            result += "-All"
        if self.p1points == self.p2points and self.p1points > 2:
            result = "Deuce"

        # p1res = ""
        # p2res = ""
        # if self.p1points > 0 and self.p2points == 0:
        #     if self.p1points == 1:
        #         p1res = "Fifteen"
        #     if self.p1points == 2:
        #         p1res = "Thirty"
        #     if self.p1points == 3:
        #         p1res = "Forty"

        #     p2res = "Love"
        #     result = p1res + "-" + p2res
        # if self.p2points > 0 and self.p1points == 0: Niepotrzbne
        #     if self.p2points == 1:
        #         p2res = "Fifteen"
        #     if self.p2points == 2:
        #         p2res = "Thirty"
        #     if self.p2points == 3:
        #         p2res = "Forty"

        #     p1res = "Love"
        #     result = p1res + "-" + p2res

        if (self.p1points > self.p2points and self.p1points < 4) or (self.p2points > self.p1points and self.p2points < 4):
            p1res, p2res = self.players_results() # zamiana na funkcje
            result = p1res + "-" + p2res
        # if self.p2points > self.p1points and self.p2points < 4: usuniecie 
        #     if self.p2points == 2:
        #         p2res = "Thirty"
        #     if self.p2points == 3:
        #         p2res = "Forty"
        #     if self.p1points == 1:
        #         p1res = "Fifteen"
        #     if self.p1points == 2:
        #         p1res = "Thirty"
        #     result = p1res + "-" + p2res

        if self.p1points > self.p2points and self.p2points >= 3:
            result = "Advantage player1"

        if self.p2points > self.p1points and self.p1points >= 3:
            result = "Advantage player2"

        if (
            self.p1points >= 4
            and self.p2points >= 0
            and (self.p1points - self.p2points) >= 2
        ):
            result = "Win for player1"
        if (
            self.p2points >= 4
            and self.p1points >= 0
            and (self.p2points - self.p1points) >= 2
        ):
            result = "Win for player2"
        return result

    # def set_p1_score(self, number):
    #     for i in range(number):
    #         self.p1points += 1

    # def set_p2_score(self, number):
    #     for i in range(number):
    #         self.p2points += 1

    def p1_score(self):
        self.p1points += 1

    def p2_score(self):
        self.p2points += 1

    # Dodana funkcja
    def players_results(self):
        score_names = ["Love", "Fifteen","Thirty", "Forty"]
        if self.p1points < 4 and self.p2points < 4:
            p1res = score_names[self.p1points]
            p2res = score_names[self.p2points]

        return (p1res, p2res)
