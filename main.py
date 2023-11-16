from sys import exit
from buttons import *
from button_functions import *


def draw_stop_signs():
    if game.player_is_done:
        screen.blit(stop_text, (858, 580))
    if game.dealer_is_done:
        screen.blit(stop_text, (852, 148))


menu_buttons = [
    Button(start_game, 348, 350, 330, 100, "Nowa gra", font_size=68),
    Button(quit_game, 348, 500, 330, 100, "Zakończ grę", font_size=68)
]

game_buttons = [
    Button(draw_player_card, 670, 314, 250, 64, "Weź Kartę"),
    Button(stop_turn, 670, 394, 250, 64, "Starczy")
]

summary_buttons = [
    Button(play_again, 160, 395, 300, 76, "Jeszcze raz", font_size=50),
    Button(stop_playing, 560, 395, 300, 76, "Koniec", font_size=50),
]

broke_buttons = [
    Button(stop_playing, 362, 395, 300, 76, "Koniec", font_size=50),
]

bet_buttons = [
    Button(confirm_bet, 730, 639, 200, 76, "Postaw", font_size=50),
    Button(add_to_bet, 93, 440, 40, 40, "+", font_size=70, y_offset=-19, value=1),
    Button(subtract_from_bet, 143, 440, 40, 40, "-", font_size=70, y_offset=-19, value=1),
    Button(add_to_bet, 244, 440, 40, 40, "+", font_size=70, y_offset=-19, value=5),
    Button(subtract_from_bet, 294, 440, 40, 40, "-", font_size=70, y_offset=-19, value=5),
    Button(add_to_bet, 394, 440, 40, 40, "+", font_size=70, y_offset=-19, value=10),
    Button(subtract_from_bet, 444, 440, 40, 40, "-", font_size=70, y_offset=-19, value=10),
    Button(add_to_bet, 544, 440, 40, 40, "+", font_size=70, y_offset=-19, value=25),
    Button(subtract_from_bet, 594, 440, 40, 40, "-", font_size=70, y_offset=-19, value=25),
    Button(add_to_bet, 694, 440, 40, 40, "+", font_size=70, y_offset=-19, value=50),
    Button(subtract_from_bet, 744, 440, 40, 40, "-", font_size=70, y_offset=-19, value=50),
    Button(add_to_bet, 844, 440, 40, 40, "+", font_size=70, y_offset=-19, value=100),
    Button(subtract_from_bet, 894, 440, 40, 40, "-", font_size=70, y_offset=-19, value=100)
]

# Game loop
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game.state == "Menu":
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in menu_buttons:
                    button.run_command()

        screen.blit(background_img, (0, 0))
        screen.blit(oczko_text, (512 - oczko_text.get_width() // 2, 100))
        screen.blit(copyright_text, (512 - copyright_text.get_width() // 2, 720))

        for button in menu_buttons:
            button.draw()

    elif game.state == "Bet":
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in bet_buttons:
                    button.run_command()

        screen.blit(background_img, (0, 0))
        screen.blit(postaw_text, (512 - postaw_text.get_width() // 2, 50))
        chosen_bet_text = bet_font.render(f"{game.current_bet} ZŁ", True, "#FFFFFF")
        screen.blit(chosen_bet_text, (512 - chosen_bet_text.get_width() // 2, 150))
        your_funds_text = bet_font.render(f"Masz jeszcze: {game.player_cash} ZŁ", True, "#FFFFFF")
        screen.blit(your_funds_text, (80, 650))

        screen.blit(chip_1_img, (75, 300))
        screen.blit(chip_5_img, (225, 300))
        screen.blit(chip_10_img, (375, 300))
        screen.blit(chip_25_img, (525, 300))
        screen.blit(chip_50_img, (675, 300))
        screen.blit(chip_100_img, (825, 300))

        for button in bet_buttons:
            button.draw()

    elif game.state == "Summary":
        screen.blit(background_img, (0, 0))
        player_card_images.update()
        dealer_card_images.update()
        draw_playing_field_text()
        winner_text = ""

        if game.winner == "Player":
            winner_text = player_wins_text
            play_result_sound("Victory")
        elif game.winner == "Dealer":
            winner_text = dealer_wins_text
            play_result_sound("Defeat")
        elif game.winner == "Draw":
            winner_text = draw_text
            play_result_sound("Victory")
        elif game.winner == "Player Broke":
            winner_text = player_broke_text
            play_result_sound("Defeat")
        elif game.winner == "Dealer Broke":
            winner_text = dealer_broke_text
            play_result_sound("Victory")

        screen.blit(winner_text, (512 - winner_text.get_width() // 2, 270))

        if game.winner not in ["Player Broke", "Dealer Broke"]:
            for button in summary_buttons:
                button.draw()
        else:
            for button in broke_buttons:
                button.draw()

        draw_stop_signs()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.winner not in ["Player Broke", "Dealer Broke"]:
                    for button in summary_buttons:
                        button.run_command()
                else:
                    for button in broke_buttons:
                        button.run_command()

    elif game.state == "Drawing cards":
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and game.current_turn == "Player":
                for button in game_buttons:
                    button.run_command()

        screen.blit(background_img, (0, 0))
        arrow_group.update()
        draw_playing_field_text()

        draw_bet_text()

        screen.blit(card_back_img, (449, 296))

        for button in game_buttons:
            button.draw()

        draw_stop_signs()

        player_card_images.update()
        dealer_card_images.update()

        if game.current_turn == "Player":
            if game.player_is_done:
                game.current_turn = "Dealer"
            else:
                player_arrow.is_visible = True
                if game.player_has_moved:
                    game.current_turn = "Dealer"
                    game.player_has_moved = False
                    game.state = "Card animation"

        elif game.current_turn == "Dealer":
            dealer_arrow.is_visible = True
            if game.dealer_delay == 0 or game.dealer_is_done:
                game.dealer_delay = 80
                if not game.dealer_is_done:
                    card_sound.play()
                    game.new_dealer_card = deck.draw_card()
                    dealer_cards.add(game.new_dealer_card)
                    dealer_card_images.add(CardSprite(game.new_dealer_card, "Dealer"))
                    game.state = "Card animation"
                else:
                    game.state = "Adding points"
                game.current_turn = "Player"

            else:
                game.dealer_delay -= 1

    elif game.state == "Adding points":
        game.player_points = player_cards.get_value()
        game.dealer_points = dealer_cards.get_value()
        if game.player_points > 21:
            game.player_lost = True
        elif game.dealer_points > 21:
            game.dealer_lost = True
        if game.dealer_points == 21 or dealer_cards.perskie_oko():
            game.dealer_is_done = True
            if not game_is_finished():
                play_dealer_ding()
        if game.dealer_points >= 17 and not 22 > game.player_points > game.dealer_points:
            if game.dealer_points > 21:
                game.dealer_lost = True
            else:
                game.dealer_is_done = True
                if not game_is_finished():
                    play_dealer_ding()
        if game.player_is_done and 22 > game.dealer_points > game.player_points:
            game.dealer_is_done = True

        if game_is_finished():
            determine_winner()
            game.state = "Summary"
        else:
            game.state = "Drawing cards"
            player_arrow.is_visible = False
            dealer_arrow.is_visible = False

    elif game.state == "Card animation":
        screen.blit(background_img, (0, 0))
        arrow_group.update()
        draw_playing_field_text()
        draw_bet_text()
        draw_stop_signs()
        screen.blit(card_back_img, (449, 296))
        player_card_images.update()
        dealer_card_images.update()
        for button in game_buttons:
            button.draw()

        all_cards_are_in_place = True
        for card_image in player_card_images:
            if card_image.card_is_moving:
                all_cards_are_in_place = False
        for card_image in dealer_card_images:
            if card_image.card_is_moving:
                all_cards_are_in_place = False
        if all_cards_are_in_place:
            game.state = "Adding points"

    elif game.state == "Shuffling":
        screen.blit(background_img, (0, 0))
        draw_playing_field_text()
        screen.blit(tasowanie_text, (532 - tasowanie_text.get_width() // 2, 330))
        if game.shuffling_delay == 0:
            game.shuffling_delay = 180
            game.state = "Bet"
        else:
            game.shuffling_delay -= 1

    pygame.display.update()
    clock.tick(60)
