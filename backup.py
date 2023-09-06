"""
Roman Littmann

Art that I borrowed because this isn't an art class:
Background Image for Farm - Not Mine
https://www.gamedevmarket.net/asset/2d-pixel-art-background-10-sky-cloud-2/
Background Image for Store - Not Mine
https://www.colourbox.com/vector/pixel-art-village-seamless-background-detailed-vector-illustration-vector-37132219
Win The Game Image - Not Mine
http://pixelartmaker.com/art/6a1747f209fdc0c
Shop Button - Not Mine
http://pixelartmaker.com/art/ede5b2a47d16616
Back Button - Not Mine
http://pixelartmaker.com/art/52eb800c23e7b88

Code to display number of coins and crops taken from ClearCode on YouTube (Lines 141-158)

All other art made by Roman Littmann (me!)
"""

import pygame
from sys import exit

pygame.init()
main_screen = pygame.display.set_mode((1000, 640))
pygame.display.set_caption('Farming Game')
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 50)


def display_time():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    time_surf = game_font.render(f'{current_time}', False, 'Red')
    time_rect = time_surf.get_rect(bottomleft=(890, 620))
    time_rect_big = time_surf.get_rect(bottomleft=(890, 620))
    time_rect_big.inflate_ip(30, 30)
    pygame.draw.rect(main_screen, 'Black', time_rect_big, 0, 40)
    main_screen.blit(time_surf, time_rect)


def game_time():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    return int(current_time)


def draw_background():
    if current_screen == 'sprites/background.jpg':
        main_screen.blit(background_surface, (0, 0))
    elif current_screen == 'sprites/store.jpg':
        main_screen.blit(store_background, (0, 0))
    elif current_screen == 'sprites/you_win.png':
        main_screen.blit(win_background_surface, (0, 0))


def draw_scene():
    main_screen.blit(coin_surface, coin_rectangle)
    main_screen.blit(food_surface, food_rectangle)
    if current_screen == 'sprites/background.jpg':
        # Store Button
        main_screen.blit(storebtn_surf, store_rect)
        # Crops
        if carrot:
            main_screen.blit(carrots_surface, carrots_rectangle)
        elif potato:
            main_screen.blit(potatos_surface, potatos_rectangle)

        if second_crop_unlocked is True:
            main_screen.blit(change_crop_surf, change_crop_rect)
        # Farms
        main_screen.blit(farm1_surf, farm_1_rect)
        main_screen.blit(farm2_surf, farm_2_rect)
        main_screen.blit(farm3_surf, farm_3_rect)
        if extra_farms is True:
            main_screen.blit(farm4_surf, farm_4_rect)
            main_screen.blit(farm5_surf, farm_5_rect)
            main_screen.blit(farm6_surf, farm_6_rect)
    elif current_screen == 'sprites/store.jpg':
        # Back button
        main_screen.blit(backbtn_surf, back_rect)
        # Store Actions
        main_screen.blit(sell_btn_surf, sell_btn_rect)
        main_screen.blit(double_button_surf, double_button_rect)
        main_screen.blit(extra_farms_surf, extra_farms_rect)
        main_screen.blit(unlock_potatos_surf, unlock_potatos_rect)
        main_screen.blit(change_name_surf, change_name_rect)
        main_screen.blit(victory_surface, victory_rectangle)


def change_acive_crop():
    global carrot, potato
    if carrot is True:
        return False, True
    elif carrot is False:
        return True, False


# The Following functions are the power-ups on the store screen
def sell_crops():
    global crop_count, player_coins
    if crop_count > 0:
        crop_count -= 1
        player_coins += crop_price


def double_coins():
    global crop_price, player_coins, crop_price_doubled
    if crop_price_doubled is False:
        crop_price_doubled = True
        crop_price = 40
        player_coins -= 20
    elif crop_price_doubled is True:
        pass


def buy_more_farms():
    global player_coins, extra_farms
    if extra_farms is False:
        extra_farms = True
        player_coins -= 20
    elif extra_farms is True:
        pass


def unlock_potatos():
    global second_crop_unlocked, player_coins
    if second_crop_unlocked is False:
        second_crop_unlocked = True
        player_coins -= 20
    elif second_crop_unlocked is True:
        pass


def change_name():
    global farm_names, counter, player_coins
    pygame.display.set_caption(farm_names[counter])
    player_coins -= 20
    if counter < 6:
        counter += 1
    else:
        counter = 0


# Score Managment
def update_score():
    score_surf = game_font.render(f'{player_coins}', False, 'Gold')
    score_rect = score_surf.get_rect(topright=(920, 20))
    score_rect_big = score_surf.get_rect(topright=(920, 20))
    score_rect_big.inflate_ip(30, 30)
    pygame.draw.rect(main_screen, 'Dark Green', score_rect_big, 0, 40)
    main_screen.blit(score_surf, score_rect)


# Crop Managment
def update_crop_count():
    crop_count_surf = game_font.render(f'{crop_count}', False, 'Gold')
    crop_count_rect = crop_count_surf.get_rect(topright=(920, 90))
    crop_count_rect_big = crop_count_surf.get_rect(topright=(920, 90))
    crop_count_rect_big.inflate_ip(30, 30)
    pygame.draw.rect(main_screen, 'Brown', crop_count_rect_big, 0, 40)
    main_screen.blit(crop_count_surf, crop_count_rect)


# Variables
player_coins = 0
crop_price = 20
crop_price_doubled = False
extra_farms = False
crop_count = 0
carrot = True
potato = False
second_crop_unlocked = False
mouse_position = ()
mouse_x_pos = 0
mouse_y_pos = 0
current_screen = 'sprites/background.jpg'
farm_names = ['Carrot Farm', 'Potato Estate', 'Blue Sky Farm','Hay Day?', 'Thanks For Playing!',
              'Special thanks to UVM Game Dev Club', 'Roman\'s Farm']
counter = 0

# For Timers
start_time = 0
start_ticks = int(pygame.time.get_ticks() / 1000)

# Background
background_surface = pygame.image.load('sprites/background.jpg').convert()
background_surface = pygame.transform.scale(background_surface, (1000, 640))
store_background = pygame.image.load('sprites/store.jpg').convert()
store_background = pygame.transform.scale(store_background, (1000, 640))
win_background_surface = pygame.image.load('sprites/you_win.png').convert()
win_background_surface = pygame.transform.scale(win_background_surface, (1000, 640))

# Store & Back
storebtn_surf = pygame.image.load('sprites/market.png').convert_alpha()
storebtn_surf = pygame.transform.scale(storebtn_surf, (150, 50))
store_rect = storebtn_surf.get_rect(topleft=(10, 10))

backbtn_surf = pygame.image.load('sprites/back.png').convert_alpha()
backbtn_surf = pygame.transform.scale(backbtn_surf, (170, 65))
back_rect = backbtn_surf.get_rect(topleft=(150, 10))

# Change Crops and Food/Coin Icons
change_crop_surf = pygame.image.load('sprites/change_crop.png').convert_alpha()
change_crop_surf = pygame.transform.scale(change_crop_surf, (100, 100))
change_crop_rect = change_crop_surf.get_rect(topleft=(870, 290))

carrots_surface = pygame.image.load('sprites/carrots.png').convert_alpha()
carrots_surface = pygame.transform.scale(carrots_surface, (100, 100))
carrots_rectangle = carrots_surface.get_rect(topleft=(870, 200))

potatos_surface = pygame.image.load('sprites/potatos.png').convert_alpha()
potatos_surface = pygame.transform.scale(potatos_surface, (100, 100))
potatos_rectangle = potatos_surface.get_rect(topleft=(870, 380))

coin_surface = pygame.image.load('sprites/coin.png').convert_alpha()
coin_surface = pygame.transform.scale(coin_surface, (100, 100))
coin_rectangle = coin_surface.get_rect(topleft=(920, -13))

food_surface = pygame.image.load('sprites/food.png').convert_alpha()
food_surface = pygame.transform.scale(food_surface, (100, 100))
food_rectangle = food_surface.get_rect(topleft=(920, 57))

# Sell Button
sell_btn_surf = pygame.image.load('sprites/sell.png').convert_alpha()
sell_btn_surf = pygame.transform.scale(sell_btn_surf, (200, 200))
sell_btn_rect = sell_btn_surf.get_rect(center=(250, 200))
# Double Coins Button
double_button_surf = pygame.image.load('sprites/double_coins.png').convert_alpha()
double_button_surf = pygame.transform.scale(double_button_surf, (200, 200))
double_button_rect = double_button_surf.get_rect(center=(500, 200))
# Extra Farms Button
extra_farms_surf = pygame.image.load('sprites/extra_farms.png').convert_alpha()
extra_farms_surf = pygame.transform.scale(extra_farms_surf, (200, 200))
extra_farms_rect = extra_farms_surf.get_rect(center=(750, 200))
# Unlock Potatos
unlock_potatos_surf = pygame.image.load('sprites/unlock_potatos.png').convert_alpha()
unlock_potatos_surf = pygame.transform.scale(unlock_potatos_surf, (200, 200))
unlock_potatos_rect = unlock_potatos_surf.get_rect(center=(250, 480))
# Rename The Farm
change_name_surf = pygame.image.load('sprites/rename.png').convert_alpha()
change_name_surf = pygame.transform.scale(change_name_surf, (200, 200))
change_name_rect = change_name_surf.get_rect(center=(500, 480))
# Win the game Button
victory_surface = pygame.image.load('sprites/victory.png').convert_alpha()
victory_surface = pygame.transform.scale(victory_surface, (200, 200))
victory_rectangle = victory_surface.get_rect(center=(750, 480))

# Farm 1
farm1_surf = pygame.image.load('sprites/template_farm.png').convert_alpha()
farm1_surf = pygame.transform.scale(farm1_surf, (200, 200))
farm_1_rect = farm1_surf.get_rect(center=(250, 200))
farm1_current_surf = "sprites/template_farm.png"
# Farm 2
farm2_surf = pygame.image.load('sprites/template_farm.png').convert_alpha()
farm2_surf = pygame.transform.scale(farm2_surf, (200, 200))
farm_2_rect = farm2_surf.get_rect(center=(500, 200))
farm2_current_surf = "sprites/template_farm.png"
# Farm 3
farm3_surf = pygame.image.load('sprites/template_farm.png').convert_alpha()
farm3_surf = pygame.transform.scale(farm3_surf, (200, 200))
farm_3_rect = farm3_surf.get_rect(center=(750, 200))
farm3_current_surf = "sprites/template_farm.png"
# Farm 4
farm4_surf = pygame.image.load('sprites/template_farm.png').convert_alpha()
farm4_surf = pygame.transform.scale(farm4_surf, (200, 200))
farm_4_rect = farm4_surf.get_rect(center=(250, 480))
farm4_current_surf = "sprites/template_farm.png"
# Farm 5
farm5_surf = pygame.image.load('sprites/template_farm.png').convert_alpha()
farm5_surf = pygame.transform.scale(farm5_surf, (200, 200))
farm_5_rect = farm5_surf.get_rect(center=(500, 480))
farm5_current_surf = "sprites/template_farm.png"
# Farm 6
farm6_surf = pygame.image.load('sprites/template_farm.png').convert_alpha()
farm6_surf = pygame.transform.scale(farm6_surf, (200, 200))
farm_6_rect = farm6_surf.get_rect(center=(750, 480))
farm6_current_surf = "sprites/template_farm.png"

if __name__ == '__main__':
    # The Game Runs in this While loop!
    while True:
        # Allows the player to close the game
        # pygame.QUIT is referencing the 'X' btn in the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        mouse_position = pygame.mouse.get_pos()
        mouse_x_pos, mouse_y_pos = mouse_position

        # Go to Store or Farm when clicked (change screens)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == 'sprites/background.jpg' and pygame.Rect.collidepoint(store_rect, mouse_x_pos,
                                                                                       mouse_y_pos):
                current_screen = 'sprites/store.jpg'
                draw_background()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == 'sprites/store.jpg' and pygame.Rect.collidepoint(back_rect, mouse_x_pos, mouse_y_pos):
                current_screen = 'sprites/background.jpg'
                draw_background()

        # Update Farm 1 when clicked
        if event.type == pygame.MOUSEBUTTONUP and pygame.Rect.collidepoint(farm_1_rect, mouse_x_pos, mouse_y_pos):
            if farm1_current_surf == 'sprites/template_farm.png' and current_screen == 'sprites/background.jpg':
                if carrot:
                    farm1_surf = pygame.image.load('sprites/carrot_stage1.png').convert_alpha()
                    farm1_surf = pygame.transform.scale(farm1_surf, (200, 200))
                    farm1_current_surf = 'sprites/carrot_stage1.png'
                elif potato:
                    farm1_surf = pygame.image.load('sprites/potato_stage1.png').convert_alpha()
                    farm1_surf = pygame.transform.scale(farm1_surf, (200, 200))
                    farm1_current_surf = 'sprites/potato_stage1.png'
            elif farm1_current_surf == 'sprites/carrot_stage3.png' or farm1_current_surf == 'sprites/potato_stage3.png':
                if current_screen == 'sprites/background.jpg':
                    farm1_surf = pygame.image.load('sprites/used_farm.png').convert_alpha()
                    farm1_surf = pygame.transform.scale(farm1_surf, (200, 200))
                    farm1_current_surf = 'sprites/used_farm.png'
                    crop_count += 1

        if game_time() % 15 == 0:
            if farm1_current_surf == 'sprites/carrot_stage1.png':
                farm1_surf = pygame.image.load('sprites/carrot_stage2.png').convert_alpha()
                farm1_surf = pygame.transform.scale(farm1_surf, (200, 200))
                farm1_current_surf = 'sprites/carrot_stage2.png'
            elif farm1_current_surf == 'sprites/potato_stage1.png':
                farm1_surf = pygame.image.load('sprites/potato_stage2.png').convert_alpha()
                farm1_surf = pygame.transform.scale(farm1_surf, (200, 200))
                farm1_current_surf = 'sprites/potato_stage2.png'

        if game_time() % 30 == 0:
            if farm1_current_surf == 'sprites/carrot_stage2.png':
                farm1_surf = pygame.image.load('sprites/carrot_stage3.png').convert_alpha()
                farm1_surf = pygame.transform.scale(farm1_surf, (200, 200))
                farm1_current_surf = 'sprites/carrot_stage3.png'
            elif farm1_current_surf == 'sprites/potato_stage2.png':
                farm1_surf = pygame.image.load('sprites/potato_stage3.png').convert_alpha()
                farm1_surf = pygame.transform.scale(farm1_surf, (200, 200))
                farm1_current_surf = 'sprites/potato_stage3.png'

        if game_time() % 7 == 0 and farm1_current_surf == 'sprites/used_farm.png':
            farm1_surf = pygame.image.load('sprites/template_farm.png').convert_alpha()
            farm1_surf = pygame.transform.scale(farm1_surf, (200, 200))
            farm1_current_surf = 'sprites/template_farm.png'

        # Farm button actions
        if event.type == pygame.MOUSEBUTTONDOWN and current_screen == 'sprites/background.jpg':
            if pygame.Rect.collidepoint(change_crop_rect, mouse_x_pos, mouse_y_pos):
                carrot, potato = change_acive_crop()
                pygame.time.wait(100)

        # Update Farm 2 when clicked
        if event.type == pygame.MOUSEBUTTONUP and pygame.Rect.collidepoint(farm_2_rect, mouse_x_pos, mouse_y_pos):
            if farm2_current_surf == 'sprites/template_farm.png' and current_screen == 'sprites/background.jpg':
                if carrot:
                    farm2_surf = pygame.image.load('sprites/carrot_stage1.png').convert_alpha()
                    farm2_surf = pygame.transform.scale(farm2_surf, (200, 200))
                    farm2_current_surf = 'sprites/carrot_stage1.png'
                elif potato:
                    farm2_surf = pygame.image.load('sprites/potato_stage1.png').convert_alpha()
                    farm2_surf = pygame.transform.scale(farm2_surf, (200, 200))
                    farm2_current_surf = 'sprites/potato_stage1.png'
            elif farm2_current_surf == 'sprites/carrot_stage3.png' or farm2_current_surf == 'sprites/potato_stage3.png':
                if current_screen == 'sprites/background.jpg':
                    farm2_surf = pygame.image.load('sprites/used_farm.png').convert_alpha()
                    farm2_surf = pygame.transform.scale(farm2_surf, (200, 200))
                    farm2_current_surf = 'sprites/used_farm.png'
                    crop_count += 1

        if game_time() % 15 == 0:
            if farm2_current_surf == 'sprites/carrot_stage1.png':
                farm2_surf = pygame.image.load('sprites/carrot_stage2.png').convert_alpha()
                farm2_surf = pygame.transform.scale(farm2_surf, (200, 200))
                farm2_current_surf = 'sprites/carrot_stage2.png'
            elif farm2_current_surf == 'sprites/potato_stage1.png':
                farm2_surf = pygame.image.load('sprites/potato_stage2.png').convert_alpha()
                farm2_surf = pygame.transform.scale(farm2_surf, (200, 200))
                farm2_current_surf = 'sprites/potato_stage2.png'

        if game_time() % 30 == 0:
            if farm2_current_surf == 'sprites/carrot_stage2.png':
                farm2_surf = pygame.image.load('sprites/carrot_stage3.png').convert_alpha()
                farm2_surf = pygame.transform.scale(farm2_surf, (200, 200))
                farm2_current_surf = 'sprites/carrot_stage3.png'
            elif farm2_current_surf == 'sprites/potato_stage2.png':
                farm2_surf = pygame.image.load('sprites/potato_stage3.png').convert_alpha()
                farm2_surf = pygame.transform.scale(farm2_surf, (200, 200))
                farm2_current_surf = 'sprites/potato_stage3.png'

        if game_time() % 7 == 0 and farm2_current_surf == 'sprites/used_farm.png':
            farm2_surf = pygame.image.load('sprites/template_farm.png').convert_alpha()
            farm2_surf = pygame.transform.scale(farm2_surf, (200, 200))
            farm2_current_surf = 'sprites/template_farm.png'

        # Update Farm 3 when clicked
        if event.type == pygame.MOUSEBUTTONUP and pygame.Rect.collidepoint(farm_3_rect, mouse_x_pos, mouse_y_pos):
            if farm3_current_surf == 'sprites/template_farm.png' and current_screen == 'sprites/background.jpg':
                if carrot:
                    farm3_surf = pygame.image.load('sprites/carrot_stage1.png').convert_alpha()
                    farm3_surf = pygame.transform.scale(farm3_surf, (200, 200))
                    farm3_current_surf = 'sprites/carrot_stage1.png'
                elif potato:
                    farm3_surf = pygame.image.load('sprites/potato_stage1.png').convert_alpha()
                    farm3_surf = pygame.transform.scale(farm3_surf, (200, 200))
                    farm3_current_surf = 'sprites/potato_stage1.png'
            elif farm3_current_surf == 'sprites/carrot_stage3.png' or farm3_current_surf == 'sprites/potato_stage3.png':
                if current_screen == 'sprites/background.jpg':
                    farm3_surf = pygame.image.load('sprites/used_farm.png').convert_alpha()
                    farm3_surf = pygame.transform.scale(farm3_surf, (200, 200))
                    farm3_current_surf = 'sprites/used_farm.png'
                    crop_count += 1

        if game_time() % 15 == 0:
            if farm3_current_surf == 'sprites/carrot_stage1.png':
                farm3_surf = pygame.image.load('sprites/carrot_stage2.png').convert_alpha()
                farm3_surf = pygame.transform.scale(farm3_surf, (200, 200))
                farm3_current_surf = 'sprites/carrot_stage2.png'
            elif farm3_current_surf == 'sprites/potato_stage1.png':
                farm3_surf = pygame.image.load('sprites/potato_stage2.png').convert_alpha()
                farm3_surf = pygame.transform.scale(farm3_surf, (200, 200))
                farm3_current_surf = 'sprites/potato_stage2.png'

        if game_time() % 30 == 0:
            if farm3_current_surf == 'sprites/carrot_stage2.png':
                farm3_surf = pygame.image.load('sprites/carrot_stage3.png').convert_alpha()
                farm3_surf = pygame.transform.scale(farm3_surf, (200, 200))
                farm3_current_surf = 'sprites/carrot_stage3.png'
            elif farm3_current_surf == 'sprites/potato_stage2.png':
                farm3_surf = pygame.image.load('sprites/potato_stage3.png').convert_alpha()
                farm3_surf = pygame.transform.scale(farm3_surf, (200, 200))
                farm3_current_surf = 'sprites/potato_stage3.png'

        if game_time() % 7 == 0 and farm3_current_surf == 'sprites/used_farm.png':
            farm3_surf = pygame.image.load('sprites/template_farm.png').convert_alpha()
            farm3_surf = pygame.transform.scale(farm3_surf, (200, 200))
            farm3_current_surf = 'sprites/template_farm.png'

        if extra_farms:
            # Update Farm 4 when clicked
            if event.type == pygame.MOUSEBUTTONUP and pygame.Rect.collidepoint(farm_4_rect, mouse_x_pos, mouse_y_pos):
                if farm4_current_surf == 'sprites/template_farm.png' and current_screen == 'sprites/background.jpg':
                    if carrot:
                        farm4_surf = pygame.image.load('sprites/carrot_stage1.png').convert_alpha()
                        farm4_surf = pygame.transform.scale(farm4_surf, (200, 200))
                        farm4_current_surf = 'sprites/carrot_stage1.png'
                    elif potato:
                        farm4_surf = pygame.image.load('sprites/potato_stage1.png').convert_alpha()
                        farm4_surf = pygame.transform.scale(farm4_surf, (200, 200))
                        farm4_current_surf = 'sprites/potato_stage1.png'
                elif farm4_current_surf == 'sprites/carrot_stage3.png' or farm4_current_surf == 'sprites/potato_stage3.png':
                    if current_screen == 'sprites/background.jpg':
                        farm4_surf = pygame.image.load('sprites/used_farm.png').convert_alpha()
                        farm4_surf = pygame.transform.scale(farm4_surf, (200, 200))
                        farm4_current_surf = 'sprites/used_farm.png'
                        crop_count += 1

            if game_time() % 15 == 0:
                if farm4_current_surf == 'sprites/carrot_stage1.png':
                    farm4_surf = pygame.image.load('sprites/carrot_stage2.png').convert_alpha()
                    farm4_surf = pygame.transform.scale(farm4_surf, (200, 200))
                    farm4_current_surf = 'sprites/carrot_stage2.png'
                elif farm4_current_surf == 'sprites/potato_stage1.png':
                    farm4_surf = pygame.image.load('sprites/potato_stage2.png').convert_alpha()
                    farm4_surf = pygame.transform.scale(farm4_surf, (200, 200))
                    farm4_current_surf = 'sprites/potato_stage2.png'

            if game_time() % 30 == 0:
                if farm4_current_surf == 'sprites/carrot_stage2.png':
                    farm4_surf = pygame.image.load('sprites/carrot_stage3.png').convert_alpha()
                    farm4_surf = pygame.transform.scale(farm4_surf, (200, 200))
                    farm4_current_surf = 'sprites/carrot_stage3.png'
                elif farm4_current_surf == 'sprites/potato_stage2.png':
                    farm4_surf = pygame.image.load('sprites/potato_stage3.png').convert_alpha()
                    farm4_surf = pygame.transform.scale(farm4_surf, (200, 200))
                    farm4_current_surf = 'sprites/potato_stage3.png'

            if game_time() % 7 == 0 and farm4_current_surf == 'sprites/used_farm.png':
                farm4_surf = pygame.image.load('sprites/template_farm.png').convert_alpha()
                farm4_surf = pygame.transform.scale(farm4_surf, (200, 200))
                farm4_current_surf = 'sprites/template_farm.png'

            # Update Farm 5 when clicked
            if event.type == pygame.MOUSEBUTTONUP and pygame.Rect.collidepoint(farm_5_rect, mouse_x_pos, mouse_y_pos):
                if farm5_current_surf == 'sprites/template_farm.png' and current_screen == 'sprites/background.jpg':
                    if carrot:
                        farm5_surf = pygame.image.load('sprites/carrot_stage1.png').convert_alpha()
                        farm5_surf = pygame.transform.scale(farm5_surf, (200, 200))
                        farm5_current_surf = 'sprites/carrot_stage1.png'
                    elif potato:
                        farm5_surf = pygame.image.load('sprites/potato_stage1.png').convert_alpha()
                        farm5_surf = pygame.transform.scale(farm5_surf, (200, 200))
                        farm5_current_surf = 'sprites/potato_stage1.png'
                elif farm5_current_surf == 'sprites/carrot_stage3.png' or farm5_current_surf == 'sprites/potato_stage3.png':
                    if current_screen == 'sprites/background.jpg':
                        farm5_surf = pygame.image.load('sprites/used_farm.png').convert_alpha()
                        farm5_surf = pygame.transform.scale(farm5_surf, (200, 200))
                        farm5_current_surf = 'sprites/used_farm.png'
                        crop_count += 1

            if game_time() % 15 == 0:
                if farm5_current_surf == 'sprites/carrot_stage1.png':
                    farm5_surf = pygame.image.load('sprites/carrot_stage2.png').convert_alpha()
                    farm5_surf = pygame.transform.scale(farm5_surf, (200, 200))
                    farm5_current_surf = 'sprites/carrot_stage2.png'
                elif farm5_current_surf == 'sprites/potato_stage1.png':
                    farm5_surf = pygame.image.load('sprites/potato_stage2.png').convert_alpha()
                    farm5_surf = pygame.transform.scale(farm5_surf, (200, 200))
                    farm5_current_surf = 'sprites/potato_stage2.png'

            if game_time() % 30 == 0:
                if farm5_current_surf == 'sprites/carrot_stage2.png':
                    farm5_surf = pygame.image.load('sprites/carrot_stage3.png').convert_alpha()
                    farm5_surf = pygame.transform.scale(farm5_surf, (200, 200))
                    farm5_current_surf = 'sprites/carrot_stage3.png'
                elif farm5_current_surf == 'sprites/potato_stage2.png':
                    farm5_surf = pygame.image.load('sprites/potato_stage3.png').convert_alpha()
                    farm5_surf = pygame.transform.scale(farm5_surf, (200, 200))
                    farm5_current_surf = 'sprites/potato_stage3.png'

            if game_time() % 7 == 0 and farm5_current_surf == 'sprites/used_farm.png':
                farm5_surf = pygame.image.load('sprites/template_farm.png').convert_alpha()
                farm5_surf = pygame.transform.scale(farm5_surf, (200, 200))
                farm5_current_surf = 'sprites/template_farm.png'

            # Update Farm 6 when clicked
            if event.type == pygame.MOUSEBUTTONUP and pygame.Rect.collidepoint(farm_6_rect, mouse_x_pos, mouse_y_pos):
                if farm6_current_surf == 'sprites/template_farm.png' and current_screen == 'sprites/background.jpg':
                    if carrot:
                        farm6_surf = pygame.image.load('sprites/carrot_stage1.png').convert_alpha()
                        farm6_surf = pygame.transform.scale(farm6_surf, (200, 200))
                        farm6_current_surf = 'sprites/carrot_stage1.png'
                    elif potato:
                        farm6_surf = pygame.image.load('sprites/potato_stage1.png').convert_alpha()
                        farm6_surf = pygame.transform.scale(farm6_surf, (200, 200))
                        farm6_current_surf = 'sprites/potato_stage1.png'
                elif farm6_current_surf == 'sprites/carrot_stage3.png' or farm6_current_surf == 'sprites/potato_stage3.png':
                    if current_screen == 'sprites/background.jpg':
                        farm6_surf = pygame.image.load('sprites/used_farm.png').convert_alpha()
                        farm6_surf = pygame.transform.scale(farm6_surf, (200, 200))
                        farm6_current_surf = 'sprites/used_farm.png'
                        crop_count += 1

            if game_time() % 15 == 0:
                if farm6_current_surf == 'sprites/carrot_stage1.png':
                    farm6_surf = pygame.image.load('sprites/carrot_stage2.png').convert_alpha()
                    farm6_surf = pygame.transform.scale(farm6_surf, (200, 200))
                    farm6_current_surf = 'sprites/carrot_stage2.png'
                elif farm6_current_surf == 'sprites/potato_stage1.png':
                    farm6_surf = pygame.image.load('sprites/potato_stage2.png').convert_alpha()
                    farm6_surf = pygame.transform.scale(farm6_surf, (200, 200))
                    farm6_current_surf = 'sprites/potato_stage2.png'

            if game_time() % 30 == 0:
                if farm6_current_surf == 'sprites/carrot_stage2.png':
                    farm6_surf = pygame.image.load('sprites/carrot_stage3.png').convert_alpha()
                    farm6_surf = pygame.transform.scale(farm6_surf, (200, 200))
                    farm6_current_surf = 'sprites/carrot_stage3.png'
                elif farm6_current_surf == 'sprites/potato_stage2.png':
                    farm6_surf = pygame.image.load('sprites/potato_stage3.png').convert_alpha()
                    farm6_surf = pygame.transform.scale(farm6_surf, (200, 200))
                    farm6_current_surf = 'sprites/potato_stage3.png'

            if game_time() % 7 == 0 and farm6_current_surf == 'sprites/used_farm.png':
                farm6_surf = pygame.image.load('sprites/template_farm.png').convert_alpha()
                farm6_surf = pygame.transform.scale(farm6_surf, (200, 200))
                farm6_current_surf = 'sprites/template_farm.png'

        # Store button actions
        if event.type == pygame.MOUSEBUTTONUP and current_screen == 'sprites/store.jpg':
            if pygame.Rect.collidepoint(sell_btn_rect, mouse_x_pos, mouse_y_pos):
                sell_crops()
            elif pygame.Rect.collidepoint(double_button_rect, mouse_x_pos, mouse_y_pos) and player_coins >= 20:
                double_coins()
            elif pygame.Rect.collidepoint(extra_farms_rect, mouse_x_pos, mouse_y_pos) and player_coins >= 20:
                buy_more_farms()
            elif pygame.Rect.collidepoint(unlock_potatos_rect, mouse_x_pos, mouse_y_pos) and player_coins >= 20:
                unlock_potatos()
            elif pygame.Rect.collidepoint(change_name_rect, mouse_x_pos, mouse_y_pos) and player_coins >= 20:
                change_name()
                pygame.time.wait(1000)
            elif pygame.Rect.collidepoint(victory_rectangle, mouse_x_pos, mouse_y_pos) and player_coins >= 100:
                current_screen = 'sprites/you_win.png'
                draw_background()

        draw_background()
        update_score()
        update_crop_count()
        display_time()
        draw_scene()

        # Sets the tick speed and updates the screen
        pygame.display.update()
        clock.tick(60)
