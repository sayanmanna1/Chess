from tkinter import *

root = Tk()
root.geometry("720x720")
root.title("Chess")

myCanvas = Canvas(root,width=720,height=720,bg="green")
myCanvas.pack()

for r in range(8):
    for c in range(8):
        if  (r%2==0 and c%2==0) or (r%2!=0 and c%2!=0):
           myCanvas.create_rectangle(r*90,c*90,r*90+90,c*90+90,fill="white")
           
pawnWImgLoad = PhotoImage(file="resource/pawnW.png")
pawnBImgLoad = PhotoImage(file="resource/pawnB.png")
bishopBImgLoad = PhotoImage(file="resource/bishopB.png")
bishopWImgLoad = PhotoImage(file="resource/bishopW.png")
kingBImgLoad = PhotoImage(file="resource/kingB.png")
kingWImgLoad = PhotoImage(file="resource/kingW.png")
queenBImgLoad = PhotoImage(file="resource/queenB.png")
queenWImgLoad = PhotoImage(file="resource/queenW.png")
knightBImgLoad = PhotoImage(file="resource/knightB.png")
knightWImgLoad = PhotoImage(file="resource/knightW.png")
rooksBImgLoad = PhotoImage(file="resource/rooksB.png")
rooksWImgLoad = PhotoImage(file="resource/rooksW.png")



def setPos(img):
        imgX,imgY = myCanvas.coords(img)
        Xconst=imgX//90
        Yconst=imgY//90
        imgX = 45*(2*Xconst+1)
        imgY = 45*(2*Yconst+1)
        return imgX,imgY


def in_bbox(event, item):# the bbox => Returns a tuple (x1, y1, x2, y2) describing a rectangle that encloses all the objects specified by tagOrId. If the argument is omitted, returns a rectangle enclosing all objects on the canvas. The top left corner of the rectangle is (x1, y1) and the bottom right corner is (x2, y2).
    bbox = myCanvas.bbox(item)
    return bbox[0] < event.x < bbox[2] and bbox[1] < event.y < bbox[3]  #gives true or false

def  get_it(event):
    global cur_item
    cur_item = myCanvas.find_closest(event.x,event.y)#gives the current point where cursor is closest to which item
    
    if not in_bbox(event,cur_item):
        cur_item = None
      
def move(event):
    if cur_item:
        xPos, yPos = event.x, event.y
        xObject, yObject = myCanvas.coords(cur_item)[0],myCanvas.coords(cur_item)[1]
        myCanvas.move(myCanvas.gettags(cur_item)[0],xPos-xObject,yPos-yObject)
     
def set(event):#gettags()[0]=> gives the current item
    if cur_item:
        x,y = event.x,event.y
        myCanvas.move(cur_item,setPos(cur_item)[0]-x,setPos(cur_item)[1]-y)
    print(myCanvas.coords(cur_item))
    print(in_bbox(event,cur_item))

    


 
class pawn:
    def __init__(self,myCanvas,x,y,imgLoad):
        self.myCanvas=myCanvas
        self.x = x
        self.y = y
        self.imgLoad = imgLoad
        pawnImg = self.myCanvas.create_image(x,y,image=self.imgLoad)
    
class king:
    def __init__(self,myCanvas,x,y,imgLoad):
        self.myCanvas=myCanvas
        self.x = x
        self.y = y
        self.imgLoad = imgLoad
        pawnImg = self.myCanvas.create_image(x,y,image=self.imgLoad)
class queen:
    def __init__(self,myCanvas,x,y,imgLoad):
        self.myCanvas=myCanvas
        self.x = x
        self.y = y
        self.imgLoad = imgLoad
        pawnImg = self.myCanvas.create_image(x,y,image=self.imgLoad)
class bishop:
    def __init__(self,myCanvas,x,y,imgLoad):
        self.myCanvas=myCanvas
        self.x = x
        self.y = y
        self.imgLoad = imgLoad
        pawnImg = self.myCanvas.create_image(x,y,image=self.imgLoad)
class knight:
    def __init__(self,myCanvas,x,y,imgLoad):
        self.myCanvas=myCanvas
        self.x = x
        self.y = y
        self.imgLoad = imgLoad
        pawnImg = self.myCanvas.create_image(x,y,image=self.imgLoad)
class rooks:
    def __init__(self,myCanvas,x,y,imgLoad):
        self.myCanvas=myCanvas
        self.x = x
        self.y = y
        self.imgLoad = imgLoad
        pawnImg = self.myCanvas.create_image(x,y,image=self.imgLoad)
pawnW=[]
for i in range(8):
    pawnW.append(pawn(myCanvas,45+90*i,135,pawnWImgLoad))
pawnB=[]
for i in range(8):
    pawnB.append(pawn(myCanvas,45+90*i,585,pawnBImgLoad))
kingW = king(myCanvas,315,45,kingWImgLoad)
kingB = king(myCanvas,315,675,kingBImgLoad)

queenW = king(myCanvas,405,45,queenWImgLoad)
queenB = king(myCanvas,405,675,queenBImgLoad)

bishopW1=bishop(myCanvas,225,45,bishopWImgLoad)
bishopW2=bishop(myCanvas,495,45,bishopWImgLoad)
bishopB1=bishop(myCanvas,225,675,bishopBImgLoad)
bishopB2=bishop(myCanvas,495,675,bishopBImgLoad)

knightW1=knight(myCanvas,135,45,knightWImgLoad)
knightW2=knight(myCanvas,585,45,knightWImgLoad)
knightB1=knight(myCanvas,135,675,knightBImgLoad)
knightB2=knight(myCanvas,585,675,knightBImgLoad)

rooksW1=rooks(myCanvas,45,45,rooksWImgLoad)
rooksW2=rooks(myCanvas,675,45,rooksWImgLoad)
rooksB1=rooks(myCanvas,45,675,rooksBImgLoad)
rooksB2=rooks(myCanvas,675,675,rooksBImgLoad)



myCanvas.bind('<Button-1>', get_it)
myCanvas.bind('<B1-Motion>', move)
myCanvas.bind('<ButtonRelease-1>',set)


    
root.mainloop()






