import pygame
from variables import *
from card_classes import *


def draw_bet_text():
    screen.blit(stawka_text, (130, 330))
    current_bet_text = casino_font.render(f"{game.current_bet} PLN", True, "#FFFFFF")
    screen.blit(current_bet_text, (130 + (stawka_text.get_width() - current_bet_text.get_width()) // 2, 400))


def draw_playing_field_text():
    if game.player_points == 21:
        player_points_text = points_font.render("Oczko!", True, "#FFFFFF")
    elif player_cards.perskie_oko():
        player_points_text = points_font.render("Perskie Oczko!", True, "#FFFFFF")
    else:
        player_points_text = points_font.render(str(game.player_points), True, "#FFFFFF")
    player_cash_text = points_font.render(f"{game.player_cash} zł", True, "#FFFFFF")
    if game.dealer_points == 21:
        dealer_points_text = points_font.render("Oczko!", True, "#FFFFFF")
    elif dealer_cards.perskie_oko():
        dealer_points_text = points_font.render("Perskie Oczko!", True, "#FFFFFF")
    else:
        dealer_points_text = points_font.render(str(game.dealer_points), True, "#FFFFFF")
    dealer_cash_text = points_font.render(f"{game.dealer_cash} zł", True, "#FFFFFF")
    screen.blit(gracz_text, (810, 545))
    screen.blit(bankier_text, (780, 190))
    screen.blit(punktow_text, (620, 625))
    screen.blit(player_points_text, (755, 625))
    screen.blit(kasa_text, (620, 685))
    screen.blit(player_cash_text, (700, 685))
    screen.blit(punktow_text, (620, 100))
    screen.blit(dealer_points_text, (755, 100))
    screen.blit(kasa_text, (620, 40))
    screen.blit(dealer_cash_text, (700, 40))
    pygame.draw.line(screen, "#FFFFFF", (16, 252), (1008, 252), 3)
    pygame.draw.line(screen, "#FFFFFF", (16, 516), (1008, 516), 3)


pygame.init()

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Oczko")
pygame.display.set_icon(pygame.image.load("./Assets/Graphics/cardicon.png"))
clock = pygame.time.Clock()

# Sprite groups for cards
player_card_images = pygame.sprite.Group()
dealer_card_images = pygame.sprite.Group()

# Background green felt graphic
background_img = pygame.image.load("./Assets/Graphics/background.png").convert()

# Back of card graphic
card_back_img = pygame.image.load("./Assets/Graphics/card_back.png").convert_alpha()

# Chips graphics
chip_1_img = pygame.image.load("./Assets/Graphics/Chips/chip_1.png").convert_alpha()
chip_5_img = pygame.image.load("./Assets/Graphics/Chips/chip_5.png").convert_alpha()
chip_10_img = pygame.image.load("./Assets/Graphics/Chips/chip_10.png").convert_alpha()
chip_25_img = pygame.image.load("./Assets/Graphics/Chips/chip_25.png").convert_alpha()
chip_50_img = pygame.image.load("./Assets/Graphics/Chips/chip_50.png").convert_alpha()
chip_100_img = pygame.image.load("./Assets/Graphics/Chips/chip_100.png").convert_alpha()

# Fonts
logo_font = pygame.font.Font("./Assets/Graphics/Ritzyremix.ttf", size=200)
casino_font = pygame.font.Font("./Assets/Graphics/Ritzyremix.ttf", size=48)
points_font = pygame.font.Font("./Assets/Graphics/BebasNeue.ttf", size=38)
game_results_font = pygame.font.Font("./Assets/Graphics/BebasNeue.ttf", size=90)
stop_font = pygame.font.Font("./Assets/Graphics/BebasNeue.ttf", size=38)
bet_font = pygame.font.Font("./Assets/Graphics/BebasNeue.ttf", size=50)
copyright_font = pygame.font.Font("./Assets/Graphics/BebasNeue.ttf", size=28)

# Text renders
oczko_text = logo_font.render("Oczko", True, "#FFFFFF")
copyright_text = copyright_font.render("© 2023 Toke Henrik Olesen", True, "#FFFFFF")
postaw_text = game_results_font.render("Twój Zakład:", True, "#FFFFFF")
gracz_text = casino_font.render("Gracz", True, "#FFFFFF")
bankier_text = casino_font.render("Bankier", True, "#FFFFFF")
stawka_text = casino_font.render("Stawka:", True, "#FFFFFF")
punktow_text = points_font.render("Punktów:", True, "#FFFFFF")
kasa_text = points_font.render("Kasa:", True, "#FFFFFF")
stop_text = stop_font.render("STOP", True, "#EE2200")
player_wins_text = game_results_font.render("Wygrywasz!", True, "#FFFFFF")
dealer_wins_text = game_results_font.render("Bank wygrywa!", True, "#FFFFFF")
draw_text = game_results_font.render("Remis!", True, "#FFFFFF")
player_broke_text = game_results_font.render("Jesteś bankrutem!", True, "#FFFFFF")
dealer_broke_text = game_results_font.render("Rozbiłeś bank!", True, "#FFFFFF")
tasowanie_text = game_results_font.render("Trwa tasowanie...", True, "#FFFFFF")
