class SetUp:
    def __init__(self):
        self.dfloor=loadImage("floor.jpg")
        self.salsa=loadImage("Salsa.jpg")
        self.bachata=loadImage("Bachata.jpg")
        self.BeginnerBasic=loadImage("Step_1.jpg")
        self.SalsaBasic=loadImage("Step_2.jpg")
        self.Sidesteps=loadImage("Step_3.jpg")
        self.ModernBasic=loadImage("Step_1.jpg")
        self.Traditional=loadImage("Step_2.jpg")
        self.BachataBox=loadImage("Step_3.jpg")
        self.zouk=loadImage("Zouk.jpg")
        self.ZoukBasic=loadImage("Step_1.jpg")
        self.Lateral=loadImage("Step_2.jpg")
        self.Kizomba=loadImage("Kizomba.jpg")
       
    
    def display(self):
        image(self.dfloor,200,0,600,600)
        image(self.salsa,0,0,200,80)
        image(self.BeginnerBasic,00,80,200,35)
        image(self.SalsaBasic,0,115,200,35)
        image(self.Sidesteps,0,150,200,35)
        image(self.bachata,0,185,200,80)  
        image(self.ModernBasic,0,265,200,35)
        image(self.Traditional,0,300,200,35)
        image(self.BachataBox,0,335,200,35)
        image(self.zouk,0,370,200,80)  
        image(self.ZoukBasic,0,450,200,35)
        image(self.Lateral,0,485,200,35)
        image(self.Kizomba,0,520,200,80)
    
class Dance:
    def __init__(self, lblink, lhalf, lx,ly,rblink, rhalf, rx,ry):
    #Coordinates for the position of the left and right foot
        self.lblink=lblink
        self.lhalf=lhalf
        self.lx=lx
        self.ly=ly
        self.rblink=rblink
        self.rhalf=rhalf
        self.rx=rx
        self.ry=ry
        self.rightfoot=loadImage("right_foot.png")
        self.leftfoot=loadImage("left_foot.png")
        if self.lhalf==1:
            self.leftfoot=loadImage("left_foot_half.png")
        elif self.lblink==1:
            self.leftfoot=loadImage("left_blink.png")
        if self.rhalf==1:
            self.rightfoot=loadImage("right_foot_half.png")
        elif self.rblink==1:
            self.rightfoot=loadImage("right_blink.png")
            
        
    def display(self):
        image(self.leftfoot, self.lx, self.ly, 140,140)
        image(self.rightfoot, self.rx,self.ry,140,140)


class Dirr:
    def __init__(self,csv):
        self.csv=csv
        self.dirr=[]
        for i in self.csv:
            row=i.strip().split(',')
            step=[]
            for j in row:
                j=int(j)
                step.append(j)
            self.dirr.append(step)
            
baselineFrameRate = 2
def setup():
    global infrastructure
    global counters
    counters = CurrentCounters()
    counters.fn = open('Start.csv')
    
    size(800, 600)
    # frameRate(0.5)
    infrastructure=SetUp()
       

#The initial coordinates before each move. Feet in teh middle of the screen:
#    feet=Dance(370,210,440,210)


class CurrentCounters:
    def __init__ (self):
        self.j = 0
        self.fn = open('Start.csv')
        self.dirr_dance = Dirr(self.fn)
    def change_dirr(self,fn):
        self.fn = fn
        self.dirr_dance = Dirr(fn)

def mouseClicked():
    if mouseX in range(0,200) and mouseY in range(80,115):
        counters.fn = open('BeginnerBasic.csv')
        counters.change_dirr(counters.fn)
    elif mouseX in range(0,200) and mouseY in range(115,150):
        counters.fn = open('SalsaBasic.csv')
        counters.change_dirr(counters.fn)
    elif mouseX in range(0,200) and mouseY in range(150,185):
        counters.fn = open('Sidesteps.csv')
        counters.change_dirr(counters.fn)
    elif mouseX in range(0,200) and mouseY in range(265,300):
        counters.fn = open('ModernBasic.csv')
        counters.change_dirr(counters.fn)
    elif mouseX in range(0,200) and mouseY in range(300,335):
        counters.fn = open('Traditional.csv')
        counters.change_dirr(counters.fn)
    elif mouseX in range(0,200) and mouseY in range(335,370):
        counters.fn = open('BachataBox.csv')
        counters.change_dirr(counters.fn)
    elif mouseX in range(0,200) and mouseY in range(450,485):
        counters.fn = open('ZoukBasic.csv')
        counters.change_dirr(counters.fn)
    elif mouseX in range(0,200) and mouseY in range(485,520):
        counters.fn = open('Lateral.csv')
        counters.change_dirr(counters.fn)
    elif mouseX in range(0,200) and mouseY in range(520,600):
        counters.fn = open('Kizomba.csv')
        counters.change_dirr(counters.fn)
    
     
def draw():
    background(255,255,255)
    infrastructure.display()
    k = counters.dirr_dance.dirr[counters.j] #error here
    if len(k) == 9:
        frameRate(baselineFrameRate * k[8])
    dance=Dance(k[0],k[1],k[2],k[3],k[4],k[5],k[6],k[7])
    dance.display()
#     print(counters.dirr_dance.dirr)
    while True:
        counters.j = (counters.j + 1) % len(counters.dirr_dance.dirr)
        if counters.j > 0:
            break
