from graphics import *


# A sprite representing a given card, drawn in a given position depending on it's owner
class CardSprite(pygame.sprite.Sprite):
    def __init__(self, card, owner):
        super().__init__()
        self.rank_string = {
            "Ace": "A_",
            "Two": "2_",
            "Three": "3_",
            "Four": "4_",
            "Five": "5_",
            "Six": "6_",
            "Seven": "7_",
            "Eight": "8_",
            "Nine": "9_",
            "Ten": "10_",
            "Jack": "J_",
            "Queen": "Q_",
            "King": "K_"
        }
        self.card_img_path = f"./Assets/Graphics/Cards/{self.rank_string[card.get_rank()]}{card.get_suit().lower()}.png"
        self.card_img = pygame.image.load(self.card_img_path).convert_alpha()
        self.back_img = pygame.image.load("./Assets/Graphics/card_back.png").convert_alpha()
        self.card_sides = [self.back_img, self.card_img]
        self.curr_side = 0
        self.card_width = self.card_img.get_width()
        self.card_height = self.card_img.get_height()
        self.curr_width = self.card_width
        self.flipping_speed = 8
        self.x_pos = 449
        self.owner = owner

        self.rect = self.card_img.get_rect()
        self.card_position = pygame.math.Vector2(449, 296)
        if owner == "Player":
            self.card_destination = pygame.math.Vector2(48 + 40 * len(player_card_images.sprites()), 555)
        if owner == "Dealer":
            self.card_destination = pygame.math.Vector2(48 + 40 * len(dealer_card_images.sprites()), 37)
        self.speed = 7
        self.direction = self.card_destination - self.card_position
        self.velocity = self.direction.normalize() * self.speed
        self.card_is_moving = True
        self.card_is_being_flipped = True

    def display_card(self):
        # Displays a card flipping animation
        # Two sides of the card are stored in a list; the index is called with a bool variable that can be "flipped"
        if self.card_is_being_flipped:
            image_to_scale = self.card_sides[self.curr_side]
            # Makes sure width stays in the 0 - full width range
            if self.flipping_speed > 0:
                self.curr_width = max(0, self.curr_width - self.flipping_speed)
            elif self.flipping_speed < 0:
                self.curr_width = min(self.card_width, self.curr_width - self.flipping_speed)
            # Changes flipping direction once 0 or full width is reached
            if self.curr_width == 0 or self.curr_width == self.card_width:
                self.flipping_speed = -self.flipping_speed
                # If 0 width is reached, swaps card sides
                if self.curr_width == 0:
                    self.curr_side = not self.curr_side
            # Creates a new scaled image from the original image
            scaled_img = pygame.transform.smoothscale(image_to_scale, (self.curr_width, self.card_height))
            # Sets x coords of the card to make sure the center stays in the same place as the width changes
            self.x_pos = 449 + self.card_width // 2 - scaled_img.get_width() // 2
            screen.blit(scaled_img, (self.x_pos, 296))
            # For this application only - stops flipping when the second side has reached full width
            if self.curr_side == 1 and self.curr_width == self.card_width:
                self.card_is_being_flipped = False
        else:
            if self.owner == "Player" and self.card_position.y + 4 < self.card_destination.y\
                    or self.owner == "Dealer" and self.card_position.y - 4 > self.card_destination.y:
                self.card_position += self.velocity
            else:
                self.card_position = self.card_destination
                self.card_is_moving = False
            self.rect.topleft = self.card_position
            screen.blit(self.card_img, self.rect)

    def update(self):
        self.display_card()


class Arrow(pygame.sprite.Sprite):
    def __init__(self, start_x_pos, y_pos):
        super().__init__()
        self.direction = 1
        self.arrow_img = pygame.image.load("./Assets/Graphics/arrow.png")
        self.rect = self.arrow_img.get_rect()
        self.start_x_pos = start_x_pos
        self.rect.y = y_pos
        self.rect.x = start_x_pos
        self.movement_range = 21
        self.is_visible = False

    def update_pos(self):
        if not self.start_x_pos - self.movement_range < self.rect.x < self.start_x_pos + self.movement_range:
            self.direction = -self.direction
        self.rect.x += self.direction

    def display_arrow(self):
        if self.is_visible:
            screen.blit(self.arrow_img, self.rect)

    def update(self):
        self.update_pos()
        self.display_arrow()


arrow_group = pygame.sprite.Group()
player_arrow = Arrow(700, 530)
dealer_arrow = Arrow(670, 176)
arrow_group.add(player_arrow)
arrow_group.add(dealer_arrow)
