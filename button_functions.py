from sprites import *
from sounds import *


def start_game():
    game.state = "Bet"


def quit_game():
    pygame.quit()
    exit()


def play_again():
    game.reset()
    player_cards.clear()
    dealer_cards.clear()
    player_card_images.empty()
    dealer_card_images.empty()
    player_arrow.is_visible = False
    dealer_arrow.is_visible = False
    if deck.no_of_playable_cards() < 22:
        deck.shuffle()
        game.state = "Shuffling"
        shuffle_sound.play()
    else:
        game.state = "Bet"


def stop_playing():
    game.state = "Menu"
    game.reset()
    game.reset_cash()
    deck.shuffle()
    player_cards.clear()
    dealer_cards.clear()
    player_card_images.empty()
    dealer_card_images.empty()
    player_arrow.is_visible = False
    dealer_arrow.is_visible = False


def draw_player_card():
    card_sound.play()
    game.new_player_card = deck.draw_card()
    player_cards.add(game.new_player_card)
    player_card_images.add(CardSprite(game.new_player_card, "Player"))
    game.player_has_moved = True


def stop_turn():
    game.player_is_done = True
    player_arrow.is_visible = False
    game.player_has_moved = True
    if game.dealer_points > game.player_points:
        game.winner = "Dealer"
        game.state = "Summary"
        defeat_sound.play()
    else:
        if not game_is_finished():
            ding_sound.play()


def add_to_bet(value):
    if game.player_cash >= value:
        chip_sound.play()
        game.current_bet += value
        game.player_cash -= value


def subtract_from_bet(value):
    if value <= game.current_bet:
        chip_sound.play()
        game.current_bet -= value
        game.player_cash += value


def confirm_bet():
    if game.current_bet > 0:
        game.state = "Drawing cards"
