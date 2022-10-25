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
    bomb_sfc = pg.Surface((50,50))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(5,5,5),(25,25),25)
    pg.draw.line(bomb_sfc,(200,180,140),(25,20),(40,0),10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx, bomb_rct.centery, = \
                randint(0,scrn_rct.width),\
                randint(0,scrn_rct.height)

    vx,vy= +1 ,+1

    #アイテム
    item_sfc = pg.Surface((50,50))
    item_sfc.set_colorkey((0,0,0))
    pg.draw.circle(item_sfc,(255,255,0),(25,25),25)
    item_rct = item_sfc.get_rect()
    item_rct.center = randint(0,(scrn_rct.width-100)),randint(0,(scrn_rct.height-100))


    #練習２
    clock = pg.time.Clock()
    while True:
        scrn_sfc.blit(bg_sfc,bg_rct)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        #マウス操作
        mouse_states = pg.mouse.get_pos()
        tori_rct.center = mouse_states
    

        scrn_sfc.blit(tori_sfc,tori_rct)
        scrn_sfc.blit(item_sfc,item_rct)
        
        #練習６
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc,bomb_rct)

        if tori_rct.colliderect(item_rct):
            fonto = pg.font.Font(None,80)
            txt = fonto.render(str("TEST"),True,(255,0,0))
            scrn_sfc.blit(txt,(800,400))
            
            pg.display.update()
            clock = pg.time.Clock()
            clock.tick(1)
            return

        if tori_rct.colliderect(bomb_rct):

            #ゲームオーバー
            scrn_sfc.blit(bg_sfc,bg_rct)
            tori_sfc = pg.image.load("fig/8.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
            scrn_sfc.blit(tori_sfc,tori_rct)
            fonto = pg.font.Font(None,80)
            txt = fonto.render(str("GAMEOVER"),True,(255,0,0))
            scrn_sfc.blit(txt,(800,400))
            pg.display.update()
            clock = pg.time.Clock()
            clock.tick(0.5)
            return
            
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() #初期化
    main() #ゲーム本体
    pg.quit() #初期化解除
    sys.exit()