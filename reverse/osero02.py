import pygame
import sys
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

img_banmen = pygame.image.load('image_os/banmen.png')

turn = 1
put_able = 0

banmen_data = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

#代入するx、yが盤面の範囲にあることの確認
def check_banmen_range(x, y):
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    return False

#コインを描くための関数
def draw_coin(scrn, x, y, col):
    pygame.draw.circle(scrn, col, (x, y), 15)

#盤面を更新するための関数
def draw_banmen(scrn):
    for i in range(8):
            for j in range(8):
                if banmen_data[j][i] == 1:
                    draw_coin(scrn, 23+i*42, 23+j*42, BLACK)
                elif banmen_data[j][i] == 2:
                    draw_coin(scrn, 23+i*42, 23+j*42, WHITE)

#マウスの位置を取得し、盤面の座標に変換する関数
def mouse_place():
    mouseX, mouseY = pygame.mouse.get_pos()
    banmen_x = int((mouseX-2)//42)
    banmen_y = int((mouseY-2)//42)
    return banmen_x, banmen_y

#コインを置けるかの判別をする関数
def check_put_coin(x, y):
    global put_able
    put_able = 0
    if banmen_data[y][x] == 0:
        if turn % 2 == 1:
            check_banmen(mouse_place()[0], mouse_place()[1],'black')
        elif turn % 2 == 0:
            check_banmen(mouse_place()[0], mouse_place()[1],'white')
        if put_able == 1:
            return True
    else:
        return False

#コインが置かれた時に、裏返してbanmen_dataを更新
def check_banmen(x, y,col):
    global put_able
    if col=='black':
        pl,de=1,2
    elif col=='white':
        pl,de=2,1
    if 1 <= x <= 7:  # 左のチェック
        i = 1
        while True:
            if check_banmen_range(x-i, y) == False:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break
            if banmen_data[y][x-i] == de:
                banmen_data[y][x-i] = 3
                i += 1
            elif banmen_data[y][x-i] == pl:
                for j in range(8):
                    for k in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = pl
                if i >= 2:
                    put_able = 1
                break
            elif banmen_data[y][x-i] == 0:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break
    if 0 <= x <= 6:  # 右のチェック
        i = 1
        while True:
            if check_banmen_range(x+i, y) == False:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break
            if banmen_data[y][x+i] == de:
                banmen_data[y][x+i] = 3
                i += 1
            elif banmen_data[y][x+i] == pl:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = pl
                if i >= 2:
                    put_able = 1
                break
            elif banmen_data[y][x+i] == 0:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break
    if 1 <= y <= 7:  # 上のチェック
        i = 1
        while True:
            if check_banmen_range(x, y-i) == False:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break
            if banmen_data[y-i][x] == de:
                banmen_data[y-i][x] = 3
                i += 1
            elif banmen_data[y-i][x] == pl:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = pl
                if i >= 2:
                    put_able = 1
                break
            elif banmen_data[y-i][x] == 0:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break
    if 0 <= y <= 6:  # 下
        i = 1
        while True:
            if check_banmen_range(x, y+i) == False:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break
            if banmen_data[y+i][x] == de:
                banmen_data[y+i][x] = 3
                i += 1
            elif banmen_data[y+i][x] == pl:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = pl
                if i >= 2:
                    put_able = 1
                break
            elif banmen_data[y+i][x] == 0:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break
    if 0 <= x <= 6 and 0 <= y <= 6:  # 右下
        i = 1
        while True:
            if check_banmen_range(x+i, y+i) == False:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break
            if banmen_data[y+i][x+i] == de:
                banmen_data[y+i][x+i] = 3
                i += 1
            elif banmen_data[y+i][x+i] == pl:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = pl
                if i >= 2:
                    put_able = 1
                break
            elif banmen_data[y+i][x+i] == 0:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break
    if 1 <= x <= 7 and 1 <= y <= 7:  # 左上
        i = 1
        while True:
            if check_banmen_range(x-i, y-i) == False:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break
            if banmen_data[y-i][x-i] == de:
                banmen_data[y-i][x-i] = 3
                i += 1
            elif banmen_data[y-i][x-i] == pl:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = pl
                if i >= 2:
                    put_able = 1
                break
            elif banmen_data[y-i][x-i] == 0:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break
    if 0 <= x <= 6 and 1 <= y <= 7:  # 右上
        i = 1
        while True:
            if check_banmen_range(x+i, y-i) == False:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break
            if banmen_data[y-i][x+i] == de:
                banmen_data[y-i][x+i] = 3
                i += 1
            elif banmen_data[y-i][x+i] == pl:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = pl
                if i >= 2:
                    put_able = 1
                break
            elif banmen_data[y-i][x+i] == 0:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break
    if 1 <= x <= 7 and 0 <= y <= 6:  # 左下
        i = 1
        while True:
            if check_banmen_range(x-i, y+i) == False:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break
            if banmen_data[y+i][x-i] == de:
                banmen_data[y+i][x-i] = 3
                i += 1
            elif banmen_data[y+i][x-i] == pl:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = pl
                if i >= 2:
                    put_able = 1
                break
            elif banmen_data[y+i][x-i] == 0:
                for k in range(8):
                    for j in range(8):
                        if banmen_data[j][k] == 3:
                            banmen_data[j][k] = de
                break

#メイン処理
def main():
    global turn, put_able

    pygame.init()
    pygame.display.set_caption('osero')
    screen = pygame.display.set_mode((340, 340))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # 画面サイズの変更
                if event.key == K_q:
                    screen = pygame.display.set_mode((340, 340), FULLSCREEN)
                if event.key == K_p or event.key == K_SPACE:
                    screen = pygame.display.set_mode((340, 340))

        screen.blit(img_banmen, [0, 0])
        draw_banmen(screen)

        click1 = pygame.mouse.get_pressed()[0]
        if click1 == 1:  # 盤面がクリックされた時
            if turn % 2 == 1 and check_put_coin(mouse_place()[0], mouse_place()[1]) == True:
                banmen_data[mouse_place()[1]][mouse_place()[0]] = 1  # 黒をおく
                check_banmen(mouse_place()[0], mouse_place()[1],'black')
                put_able = 0
                turn += 1
            if turn % 2 == 0 and check_put_coin(mouse_place()[0], mouse_place()[1]) == True:
                banmen_data[mouse_place()[1]][mouse_place()[0]] = 2  # 白をおく
                check_banmen(mouse_place()[0], mouse_place()[1],'white')
                put_able = 0
                turn += 1
            print(turn)

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
