import pygame as pg
import random
import sys


def main():
    #練習１
    pg.display.set_caption("逃げろこうかとん") #タイトルバー
    scrn_sfc = pg.display.set_mode((1600,800)) #画面を生成
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
    bomb_rct.centerx, bomb_rct.centery, = random.randint(0,1600),random.randint(0,900)

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
            tori_rct.centery -= 1 #こうかとんの座標を
        if key_states[pg.K_DOWN]:
            tori_rct.centery += 1 #こうかとんの座標を
        if key_states[pg.K_LEFT]: 
            tori_rct.centerx -= 1#こうかとんの座標を
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx += 1 #こうかとんの座標を    

        scrn_sfc.blit(tori_sfc,tori_rct)
        scrn_sfc.blit(bomb_sfc,bomb_rct)
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() #初期化
    main() #ゲーム本体
    pg.quit() #初期化解除
    sys.exit()