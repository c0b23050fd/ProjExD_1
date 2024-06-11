import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_f = pg.image.load("fig/pg_bg.jpg")
    bg_img_f = pg.transform.flip(bg_img_f, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = (300, 200)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-(tmr%3200), 0])
        screen.blit(bg_img_f, [-(tmr%3200) + 1600, 0])
        screen.blit(bg_img, [-(tmr%3200) + 3200, 0])
        screen.blit(kk_img, kk_rct)

        move = [-1,0]
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            move[1] = -1
        if key_lst[pg.K_DOWN]:
            move[1] = 1
        if key_lst[pg.K_RIGHT]:
            move[0] = 1
        
        kk_rct.move_ip(move)

        pg.display.update()
        tmr += 1      
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()