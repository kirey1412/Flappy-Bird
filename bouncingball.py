import pgzrun
TITLE="Bouncing Ball"
WIDTH=700
HEIGHT=650
gravity=500 #px per/s

class Ball():
    def __init__(self, x, y, vx, vy, clr, r):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.clr=clr
        self.r=r
    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.clr, self.r)

balls= []
a=Ball((85,120), 44, "lightgreen")
b=Ball((30,100), 50, "skyblue")
c=Ball((90, 80), 20, "pink")
d=Ball((50,20), 37, "yellow")

pgzrun.go()