class GameVariables:
    def __init__(self):
        self.current_bet = 0
        self.player_points = 0
        self.dealer_points = 0
        self.player_cash = 100
        self.dealer_cash = 100000
        self.dealer_delay = 80
        self.shuffling_delay = 180
        self.player_is_done = False
        self.dealer_is_done = False
        self.current_turn = "Player"
        self.player_has_moved = False
        self.player_wins = False
        self.dealer_wins = False
        self.dealer_lost = False
        self.player_lost = False
        self.winner = ""
        self.state = "Menu"
        self.new_player_card = None
        self.new_dealer_card = None
        self.result_sound_has_played = False
        self.dealer_ding_has_played = False

    def reset(self):
        self.current_bet = 0
        self.player_points = 0
        self.dealer_points = 0
        self.player_is_done = False
        self.dealer_is_done = False
        self.current_turn = "Player"
        self.player_has_moved = False
        self.player_wins = False
        self.dealer_wins = False
        self.dealer_lost = False
        self.player_lost = False
        self.winner = ""
        self.new_player_card = None
        self.new_dealer_card = None
        self.result_sound_has_played = False
        self.dealer_ding_has_played = False

    def reset_cash(self):
        self.player_cash = 100
        self.dealer_cash = 1000000


game = GameVariables()


def game_is_finished():
    if (game.player_is_done and game.dealer_is_done) or game.dealer_lost or game.player_lost:
        return True
    return False


def determine_winner():
    if game.player_lost:
        game.winner = "Dealer"
    elif game.dealer_lost:
        game.winner = "Player"
    elif game.player_is_done and game.dealer_is_done:
        if game.player_points > game.dealer_points:
            game.winner = "Player"
        elif game.player_points < game.dealer_points:
            game.winner = "Dealer"
        elif game.player_points == game.dealer_points:
            game.winner = "Draw"

    if game.winner == "Player":
        game.player_cash += game.current_bet * 2
        game.dealer_cash -= game.current_bet
    elif game.winner == "Dealer":
        game.dealer_cash += game.current_bet
    elif game.winner == "Draw":
        game.player_cash += game.current_bet

    if game.player_cash == 0:
        game.winner = "Player Broke"
    elif game.dealer_cash <= 0:
        game.winner = "Dealer Broke"
