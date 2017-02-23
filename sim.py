#!/usr/bin/python3

from tkinter import Tk,Canvas
import random,time

class Cell(object):
    """docstring for Cell."""
    def __init__(self, x, y, color):
        super(Cell, self).__init__()
        self.pos = (x,y)
        self.color = color

    def getX(self):
        return self.pos[0]

    def getY(self):
        return self.pos[1]

    def getPos(self):
        return self.pos

class World(object):
    """docstring for World."""
    def __init__(self):
        super(World, self).__init__()
        self.cells = {}

    def createCell(self):
        newPos = (random.randint(-20,20),random.randint(-20,20))
        while str(newPos) in self.cells:
            newPos = (random.randint(-20,20),random.randint(-20,20))
        self.cells[str(newPos)] = Cell(newPos[0],newPos[1],"black")

    def printContents(self):
        for pos,cell in self.cells.items():
            print("Cell at " + pos)

    def update(self):
        surroundCounts = dict()
        for pos,cell in self.cells.items():
            x = cell.getX()
            y = cell.getY()
            for i in [-1,0,1]:
                    if str((x + i, y)) in surroundCounts:
                        surroundCounts[str((x + i, y))] += 1
                    else:
                        surroundCounts[str((x + i, y))] = 1
            for j in [-1,0,1]:
                    if str((x, y + j)) in surroundCounts:
                        surroundCounts[str((x, y + j))] += 1
                    else:
                        surroundCounts[str((x, y + j))] = 1
        self.cells.clear()
        self.printContents()
        for pos,count in surroundCounts.items():
            if count == random.randint(0,3) or count == random.randint(0,3):
                nums = [x for x in list(pos) if x != ',' and x != '(' and x != ')']
                num = ''
                for c in nums:
                    if c == ' ':
                        x = int(num)
                        num = ''
                    else:
                        num += c
                y = int(num)
                color = ""
                if count == 1:
                    color = "#A9A9A9"
                elif count == 2:
                    color = "#696969"
                elif count == 3:
                    color = "#000000"
                else:
                    color = "#DCDCDC"
                self.cells[str((x,y))] = Cell(x,y,color)

class ViewPort(object):
    """docstring for ViewPort."""
    def __init__(self):
        super(ViewPort, self).__init__()
        self.root = Tk()
        self.width = 1000
        self.height = 800
        self.view = Canvas(self.root,width=self.width,height=self.height)
        self.view.grid()
        self.scale = 1
        self.offsetX = self.width / 2
        self.offsetY = self.height / 2
        self.root.bind("<Up>",self.increaseScale)
        self.root.bind("<Down>",self.decreaseScale)

    def increaseScale(self,event):
        self.scale += 1

    def decreaseScale(self,event):
        if self.scale > 1:
            self.scale -= 1

    def drawWorld(self,world):
        for item in self.view.find_all():
            self.view.delete(item)
        for (pos,cell) in world.cells.items():
            x = cell.getX()*self.scale + self.offsetX
            y = cell.getY()*self.scale + self.offsetY
            if x < self.width and x > 0 and y < self.height and y > 0:
                self.view.create_rectangle( x, y, x + self.scale, y + self.scale,
    									  fill = cell.color, width = 0)
        self.root.update()

    def startMainloop(self,callback):
        self.root.after(0,callback)
        self.root.mainloop()

class Simulation(object):
    """docstring for Simulation."""
    def __init__(self):
        super(Simulation, self).__init__()
        self.world = World()
        for i in range(1):
            self.world.createCell()
        self.view = ViewPort()
        self.view.drawWorld(self.world)

    def update(self):
        self.world.update()
        self.view.drawWorld(self.world)

    def start(self):
        self.view.startMainloop(self.loop)

    def loop(self):
        while True:
            self.update()


s = Simulation()
s.start()
