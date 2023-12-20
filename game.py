class Game:
    """The class of the game session

    :param p1Went: tracks the player 1 move
    :type p1Went: bool
    :param p2Went: tracks the player 2 move
    :type p2Went: bool
    :param ready: the flag of readiness
    :type ready: bool
    :param id: the identitificator of the game session
    :type id: int
    :param moves: the list of actual moves of the players
    :type moves: list
    :param wins: the number of wins for each player
    :type wins: list
    :param ties: the number of ties in the game
    :type ties: int

    """

    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0

    def get_player_move(self, p):
        """The function of taking the move of the player

        :param p: index of player
        :type p: int
        :return: Move of current player
        :rtype: int
        """
        return self.moves[p]

    def play(self, player, move):
        """The function of changing the move of current player

        :param player: index of player
        :type player: int
        :param move: the actual move of the player
        :type move: str

        """
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        """The function of checking the readiness of the players

        """
        return self.ready

    def bothWent(self):
        """The function of checking the finish of the round

        """
        return self.p1Went and self.p2Went

    def winner(self):
        """The function of checking the winner of the round

        """

        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1

        return winner

    def resetWent(self):
        """The function of reseting the round

        """
        self.p1Went = False
        self.p2Went = False
