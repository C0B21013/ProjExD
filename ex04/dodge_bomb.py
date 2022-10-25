import pygame as pg
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
    

    #練習２
    clock = pg.time.Clock()
    while True:
        scrn_sfc.blit(bg_sfc,bg_rct)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        scrn_sfc.blit(tori_sfc,tori_rct)
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() #初期化
    main() #ゲーム本体
    pg.quit() #初期化解除
    sys.exit()