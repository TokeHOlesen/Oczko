import pygame
from variables import *

card_sound = pygame.mixer.Sound("./Assets/Sounds/card.wav")
chip_sound = pygame.mixer.Sound("./Assets/Sounds/chip.wav")
shuffle_sound = pygame.mixer.Sound("./Assets/Sounds/shuffle.wav")
ding_sound = pygame.mixer.Sound("./Assets/Sounds/ding.mp3")
defeat_sound = pygame.mixer.Sound("./Assets/Sounds/defeat.mp3")
victory_sound = pygame.mixer.Sound("./Assets/Sounds/victory.mp3")


def play_result_sound(sound):
    if not game.result_sound_has_played:
        if sound == "Victory":
            victory_sound.play()
        elif sound == "Defeat":
            defeat_sound.play()
        game.result_sound_has_played = True


def play_dealer_ding():
    if not game.dealer_ding_has_played:
        ding_sound.play()
        game.dealer_ding_has_played = True
