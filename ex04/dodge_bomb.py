import pygame as pg
import sys


def main():
    #練習１
    pg.display.set_caption("逃げろこうかとん") #タイトルバー
    scrn_sfc = pg.display.set_mode((1600,800)) #画面を生成
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    #練習２
    clock = pg.time.Clock()
    while True:
        scrn_sfc.blit(bg_sfc,bg_rct)
        pg.display.update()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
                
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() #初期化
    main() #ゲーム本体
    pg.quit() #初期化解除
    sys.exit()