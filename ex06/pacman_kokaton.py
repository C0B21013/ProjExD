from os import scandir
from turtle import backward
import pygame as pg
import sys
from random import randint
WINDOW = (1600, 900)
MAP=[ #ステージ通路設定 １は壁０は通路
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1],
    [1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
#BGM設定
class Music:
    def __init__(self,mus):
        pg.mixer.music.load(mus)
        pg.mixer.music.play(-1)


#スクリーン設定
class Screen:
    def __init__(self,titel,wh,bgimg):
        pg.display.set_caption(titel)
        self.sfc = pg.display.set_mode(wh)
        
        self.rct = self.sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.sfc, self.rct) 

#ステージ描画 １なら壁、０なら通路を描画
class map:
    def __init__(self,scr,map):
        x=0
        y=0
        for i in map:
            for j in i:
                if j == 1:
                    pg.draw.rect(scr,(100,100,120),(x*100,y*100,100,100),0)
                    #self.sfc = pg.Surface((100, 100))
                    #pg.draw.rect(self.sfc,(70,70,90),(x*100,y*100,100,100),0)
                    #self.rct = self.sfc.get_rect()
                    #self.rct.centerx = x
                    #self.rct.centery = y

                if j == 0:
                    pg.draw.rect(scr,(0,0,0),(x*100,y*100,100,100),0)

                x +=1
            else:
                x=0
                y+=1

#こうかとん設定
class Bird:
    key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
    }

    def __init__(self,img,zoom,xy):
        sfc = pg.image.load(img)#"fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)#2.0
        self.rct = sfc.get_rect()
        self.rct.center = xy #900, 400

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) # 練習3

    def update(self,scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr)

class item:
    def __init__(self,radius,vxy,scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2))
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, (255,200,0), (radius,radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) # 練習3



def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < (scr_rct.left)+100 or (scr_rct.right)-150 < obj_rct.right: 
        yoko = -1
    if obj_rct.top < (scr_rct.top)+100 or (scr_rct.bottom)-150 < obj_rct.bottom: 
        tate = -1
    return yoko, tate




def main():
    bgm = Music("ex05/data/house_lo.wav")#BGM追加

    scr = Screen("こうかとん",WINDOW,"fig/pg_bg.jpg")

    kkt = Bird("fig/6.png",2.0,(900, 400))


    clock = pg.time.Clock() # 練習1

    while True:
        scr.blit()
        stg=map(scr.sfc,MAP)
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        kkt.update(scr)
        

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()