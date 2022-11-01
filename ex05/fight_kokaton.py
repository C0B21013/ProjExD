from os import scandir
from turtle import backward
import pygame as pg
import sys
from random import randint
import time
import math


class Screen:
    def __init__(self,titel,wh,bgimg):
        pg.display.set_caption(titel)#逃げろ！こうかとん
        self.sfc = pg.display.set_mode(wh)#(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg)#"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
    
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


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


class Bomb:
    def __init__(self,color,radius,vxy,scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius,radius), radius) # 爆弾用の円を描く
        pg.draw.line(self.sfc,(200,180,140),(radius,radius),(radius/2,0),10)#導火線追加
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) # 練習3

    def update(self,scr:Screen):
        self.rct.move_ip(self.vx,self.vy) # 練習6
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class Timer:
    def __init__(self,xy):
        self.start = time.time()
        self.font = pg.font.Font(None,70)
        self.font.set_italic(1)
        self.color = "white"
        self.txy = xy
    
    
    def update(self,scr:Screen):
        self.time = time.time() - self.start
        self.img = self.font.render(str(math.floor(self.time)),0,self.color)
        self.rct = self.img.get_rect().move(self.txy)
        scr.sfc.blit(self.img, self.rct)


class Music:
    def __init__(self,mus):
        pg.mixer.music.load(mus)
        pg.mixer.music.play(-1)


class Explosion:
    def __init__(self,file):
        self.img = pg.image.load(file)
        self.rct = self.img.get_rect()

    def update(self,scr:Screen,x,y):
        self.rct = self.img.get_rect().move(x,y)
        scr.sfc.blit(self.img, self.rct)
        pg.time.wait(1000)


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

    scr = Screen("逃げろ！こうかとん",(1600, 900),"fig/pg_bg.jpg")
    
    kkt = Bird("fig/6.png",2.0,(900, 400))

    bkd = Bomb((1,1,1),20,(+1,+1),scr)
    bkd1 = Bomb((1,1,1),20,(+1,+1),scr)

    time = Timer((100,800))

    clock = pg.time.Clock()

    bgm = Music("ex05/data/house_lo.wav")

    exp = Explosion("C:/Users/C0B21013/Documents/ProjExD2022/ex05/data/explosion1.gif")
    while True:
        scr.blit()
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        kkt.update(scr)
        bkd.update(scr)
        bkd1.update(scr)
        time.update(scr)

        if kkt.rct.colliderect(bkd.rct): # こうかとんrctが爆弾rctと重なったら

            return
        if kkt.rct.colliderect(bkd1.rct): # こうかとんrctが爆弾rctと重なったら
            
            return

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()
