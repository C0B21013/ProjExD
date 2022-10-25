import pygame as pg
from random import randint 
import sys


def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate

def main():
    #練習１
    pg.display.set_caption("逃げろこうかとん") #タイトルバー
    scrn_sfc = pg.display.set_mode((1600,800)) #画面を生成
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    #練習３
    tori_sfc = pg.image.load("fig/6.png") #Surface
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect() #rect
    tori_rct.center = 900,400

    #練習５
    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx, bomb_rct.centery, = randint(0,scrn_rct.width),randint(0,scrn_rct.height)

    vx,vy= +1 ,+1

    #練習２
    clock = pg.time.Clock()
    while True:
        scrn_sfc.blit(bg_sfc,bg_rct)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        #練習４
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:
            tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:
            tori_rct.centery += 1 
        if key_states[pg.K_LEFT]: 
            tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx += 1
        
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]: 
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_states[pg.K_UP]: 
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1

        scrn_sfc.blit(tori_sfc,tori_rct)
        
        #練習６
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc,bomb_rct)

        if tori_rct.colliderect(bomb_rct):
            return
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() #初期化
    main() #ゲーム本体
    pg.quit() #初期化解除
    sys.exit()