class Game:
    def __init__(self, players):
        self.players = players

    def play_match(self, player1, player2):
        # player1, player2��� win_lose_history��� update������
        # elo rating ��������������� ������ ��������� current_rating��� update��� ���
        # https://namu.wiki/w/Elo%20%EB%A0%88%EC%9D%B4%ED%8C%85 ������
        pass

    def match_players(self):

        ...

    def simulate(self):
        pass


class Player:
    def __init__(self, player_id, initial_rating=1000, actual_rating=1000):
        self.win_lose_history = []
        self.current_rating = initial_rating
        self.actual_rating = actual_rating

    def __str__(self):
        return str(self.player_id)