from tkinter import *
import serial
import math
import time
import copy
import sys
import pygame
import random
import numpy as np
import pyttsx3
import speech_recognition

list1=['11','12','18','14','15','16','17']
list2=['21','22','23','24','25','26','27']

robot_ear= speech_recognition.Recognizer()

ser=serial.Serial('COM4', 9600)
state=0
rowX=0
rowY=0
colX=0
colY=0
count=0
roww=0
coll=0

root=Tk()
root.geometry('730x260')
root.configure(background='gray')

tempx=0
tempy=0
tempx1=0
tempy1=0
tempz=0
tempz1=0
a1=235
a2=227.525

def command1():
	string1=entry1.get()
	entry1.delete(0,END)
	string2=entry2.get()
	entry2.delete(0,END)
	string3=entry3.get()
	entry3.delete(0,END)

	if (string1+'d')=='d':
		string1='0000'
	if (string2+'d')=='d':
		string2='0000'
	if (string3+'d')=='d':
		string3='0000'

	string3=int(string3)
	string3=string3*160
	string3=str(string3)

	global tempz
	global tempz1
	tempz=tempz1+int(string3)
	if tempz>=0 and tempz<=16000:
		tempz1=tempz
		if int(string3)>0:
			string3='00000000+'+string3
		else:
			string3='00000000'+string3
		ser.write(string3.encode('utf-8'))
	if tempz<0 and tempz>16000:
		tempz=0
	code=string1+string2
	global tempx
	global tempy
	global tempx1
	global tempy1
	tempx=tempx1+int(code[0:4])
	tempy=tempy1+int(code[4:8])
	if tempx>=-25 and tempx<=205 and tempy<=170 and tempy>=-170 :
		tempx1=tempx
		tempy1=tempy
		ser.write(code.encode('utf-8'))	
		print(code)
	if tempx<-25 or tempx>205 :
		tempx=0
	if tempx>170 or tempx<-170:
		tempx=0
def command2():
	string1=entry11.get()
	entry11.delete(0,END)
	string2=entry22.get()
	entry22.delete(0,END)
	string3=entry33.get()
	entry33.delete(0,END)
	if (string1+'d')=='d':
		string1='0000'
	if (string2+'d')=='d':
		string2='0000'
	if (string3+'d')=='d':
		string3='0000'
	global tempx
	global tempy
	global tempx1
	global tempy1
	global a1
	global a2
	string3=int(string3)
	string3=string3*160
	string3=str(string3)
	global tempz
	global tempz1
	tempz=tempz1+int(string3)
	if tempz>=0 and tempz<=16000:
		tempz1=tempz
		if int(string3)>0:
			string3='00000000+'+string3
		else:
			string3='00000000'+string3
		ser.write(string3.encode('utf-8'))
	if tempz<0 and tempz>16000:
		tempz=0
	x=float(string1)
	y=float(string2)
	t2=math.acos((x*x+y*y-a1*a1-a2*a2)/(2*a1*a2))
	if x>0 and y>0:
		t1=math.atan(y/x)-math.asin((a2*math.sin(t2))/math.sqrt(x*x+y*y))
	if x<0 and y>0:
		t1=math.atan(y/x)-math.asin((a2*math.sin(t2))/math.sqrt(x*x+y*y))+(math.pi)
	if x<0 and y<0:
		t1=-math.atan(y/x)+math.asin((a2*math.sin(t2))/math.sqrt(x*x+y*y))+(math.pi)
	if x>0 and y<0:
		t1=math.atan(y/x)-math.asin((a2*math.sin(t2))/math.sqrt(x*x+y*y))
	if t1<(-25*(math.pi)/180) or t1>(205*(math.pi)/180):
		t2=-t2
		t1=math.atan(y/x)-math.asin((a2*math.sin(t2))/math.sqrt(x*x+y*y))
	t1=t1*180/(math.pi)
	t2=t2*180/(math.pi)
	t1=round(t1)
	t2=round(t2)
	t1=t1-tempx1
	t2=t2-tempy1
	#fix t1:
	#-
	if int(t1)<0 and abs(int(t1))<100 and abs(int(t1))>=10:
		t1=str(t1)
		t1=t1[0]+'0'+t1[1]+t1[2]
	if int(t1)<0 and abs(int(t1))<10:
		t1=str(t1)
		t1=t1[0]+'00'+t1[1]
	#+
	if int(t1)>0 and int(t1)<100 and int(t1)>=10:
		t1=str(t1)
		t1='+0'+t1[0]+t1[1]
	if int(t1)>0 and int(t1)<10:
		t1=str(t1)
		t1='+00'+t1[0]
	if int(t1)>=100:
		t1=str(t1)
		t1='+'+t1[0]+t1[1]+t1[2]

	#fix t2:
	#-
	if int(t2)<0 and abs(int(t2))<100 and abs(int(t2))>=10:
		t2=str(t2)
		t2=t2[0]+'0'+t2[1]+t2[2]
	if int(t2)<0 and abs(int(t2))<10:
		t2=str(t2)
		t2=t2[0]+'00'+t2[1]
	#+
	if int(t2)>0 and int(t2)<100 and int(t2)>=10:
		t2=str(t2)
		t2='+0'+t2[0]+t2[1]
	if int(t2)>0 and int(t2)<10:
		t2=str(t2)
		t2='+00'+t2[0]
	if int(t2)>=100:
		t2=str(t2)
		t2='+'+t2[0]+t2[1]+t2[2]

	t1=str(t1)
	t2=str(t2)
	code=t1+t2
	
	tempx=tempx1+int(code[0:4])
	tempy=tempy1+int(code[4:8])

	if tempx>=-25 and tempx<=205 and tempy<=170 and tempy>=-170 :
		tempx1=tempx
		tempy1=tempy
		print(code)
		ser.write(code.encode('utf-8'))
	if tempx<-25 or tempx>205 :
		tempx=0
	if tempx>170 or tempx<-170:
		tempx=0
def home():
	global tempx1
	global tempy1
	global tempz1
	tempx2=-tempx1
	tempy2=-tempy1
	tempz2=-tempz1
	tempx2=int(tempx2)
	tempy2=int(tempy2)
	tempz2=int(tempz2)
	if tempz2>0:
		codez='00000000+'+str(tempz2)
	else:
		codez='00000000'+str(tempz2)
	
	ser.write(codez.encode('utf-8'))
	tempz1=0
	
	#fix string X:
	if int(tempx2)<0 and abs(int(tempx2))<100 and abs(int(tempx2))>=10:
		tempx2=str(tempx2)
		tempx2=tempx2[0]+'0'+tempx2[1]+tempx2[2]
	if int(tempx2)<0 and abs(int(tempx2))<10:
		tempx2=str(tempx2)
		tempx2=tempx2[0]+'00'+tempx2[1]
	if int(tempx2)>0 and int(tempx2)<100 and int(tempx2)>=10:
		tempx2=str(tempx2)
		tempx2='+0'+tempx2[0]+tempx2[1]
	if int(tempx2)>0 and int(tempx2)<10:
		tempx2=str(tempx2)
		tempx2='+00'+tempx2[0]
	#fix string Y:
	if int(tempy2)<0 and abs(int(tempy2))<100 and abs(int(tempy2))>=10:
		tempy2=str(tempy2)
		tempy2=tempy2[0]+'0'+tempy2[1]+tempy2[2]
	if int(tempy2)<0 and abs(int(tempy2))<10:
		tempy2=str(tempy2)
		tempy2=tempy2[0]+'00'+tempy2[1]
	if int(tempy2)>0 and int(tempy2)<100 and int(tempy2)>=10:
		tempy2=str(tempy2)
		tempy2='+0'+tempy2[0]+tempy2[1]
	if int(tempy2)>0 and int(tempy2)<10:
		tempy2=str(tempy2)
		tempy2='+00'+tempy2[0]

	tempx2=str(tempx2)
	if tempx2=='0':
		tempx2='0000'
	tempy2=str(tempy2)
	
	codehome=tempx2+tempy2
	ser.write(str(codehome).encode('utf-8'))
	tempx1=0
	tempy1=0



WIDTH = 750
HEIGHT = 750

global ROWS
ROWS=7
global COLS
COLS = 7
SQSIZE = WIDTH // COLS

LINE_WIDTH = 5
CIRC_WIDTH = 5 
CROSS_WIDTH = 5

RADIUS = SQSIZE // 4

if ROWS==7:
	OFFSET = 30
if ROWS==5:
	OFFSET = 40

# --- COLORS ---

BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRC_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# --- PYGAME SETUP ---

pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill( BG_COLOR )

# --- CLASSES ---

class Board:

    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS) )
        self.empty_sqrs = self.squares # [squares]
        self.marked_sqrs = 0

    
    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append( (row, col) )
        
        return empty_sqrs

    def isfull(self):
        return self.marked_sqrs == 9

    def isempty(self):
        return self.marked_sqrs == 0

class Game:

    def __init__(self):
        self.board = Board()
      
        self.player = 1   #1-cross  #2-circles
        self.gamemode = 'ai' # pvp or ai
        self.running = True
        self.num1=1
        self.num2=2
        self.show_lines()

    # --- DRAW METHODS ---

    def show_lines(self):
        # bg
        screen.fill( BG_COLOR )

        # vertical
        if ROWS==5 and COLS==5:
	        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
	        pygame.draw.line(screen, LINE_COLOR, (WIDTH - 3*SQSIZE, 0), (WIDTH - 3*SQSIZE, HEIGHT), LINE_WIDTH)
	        pygame.draw.line(screen, LINE_COLOR, (WIDTH - 2*SQSIZE, 0), (WIDTH - 2*SQSIZE, HEIGHT), LINE_WIDTH)
	        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

	        # horizontal
	        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
	        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - 3*SQSIZE), (WIDTH, HEIGHT - 3*SQSIZE), LINE_WIDTH)
	        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - 2*SQSIZE), (WIDTH, HEIGHT - 2*SQSIZE), LINE_WIDTH)
	        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)
        if ROWS==7 and COLS==7:
            pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (WIDTH - 5*SQSIZE, 0), (WIDTH - 5*SQSIZE, HEIGHT), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (WIDTH - 4*SQSIZE, 0), (WIDTH - 4*SQSIZE, HEIGHT), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (WIDTH - 3*SQSIZE, 0), (WIDTH - 3*SQSIZE, HEIGHT), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (WIDTH - 2*SQSIZE, 0), (WIDTH - 2*SQSIZE, HEIGHT), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

	        # horizontal
	        
            pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - 5*SQSIZE), (WIDTH, HEIGHT - 5*SQSIZE), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - 4*SQSIZE), (WIDTH, HEIGHT - 4*SQSIZE), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - 3*SQSIZE), (WIDTH, HEIGHT - 3*SQSIZE), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - 2*SQSIZE), (WIDTH, HEIGHT - 2*SQSIZE), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)

    def draw_fig(self, row, col):
        if self.player == self.num1:
            # draw cross
            # desc line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            # asc line
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
        
        elif self.player == self.num2:
            # draw circle
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)

    # --- OTHER METHODS ---

    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        
        self.draw_fig(row, col)
        self.next_turn()
        

    def next_turn(self):
        self.player = self.player % 2 + 1

    def change_gamemode(self):
        self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'

    def reset(self):
        self.__init__()

def main():

    # --- OBJECTS ---

    game = Game()
    board = game.board
   

    # --- MAINLOOP ---

    while True:
    	global roww
    	global coll
    	pygame.display.update()
    	# with speech_recognition.Microphone() as mic:
    	# 	audio =robot_ear.listen(mic)
    	# try:
    	# 	you = robot_ear.recognize_google(audio)
    	# except:
    	# 	you='none'
    	# for i in range(len(list1)):
    	# 	if you in list1[i]:
    	# 		roww=i
    	# 	if you in list2[i]:
    	# 		coll=i
    	# engine = pyttsx3.init()
    	# engine.say(you)
    	# engine.runAndWait()
    	# print(roww)
    	# print(coll)
    	# if 'go' in you:
    	# 	game.make_move(roww, coll)

    	global count
    	for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            # quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # keydown event
            if event.type == pygame.KEYDOWN:

                # r-restart
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP] and keys[pygame.K_SPACE]:
                    count=0
                    game.reset()
                    codee='0001'
                    
                    board = game.board
                if keys[pygame.K_UP] and keys[pygame.K_r]:
                    codee='0001'
 					ser.write(codee.encode('utf-8'))
            # click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE
                
                # human mark sqr
                if board.empty_sqr(row, col) and game.running:
                	game.make_move(row, col)
                	count=count +1
                	if game.num1==1 and game.player==2:
                		if count%2==1:
                			code='1'+str(col)+str(row)+str(ROWS)
                			ser.write(code.encode('utf-8'))
                			print(code)
                			print('11')
	                if game.num1==2 and game.player==2:
                		if count%2==1:
	                		code='2'+str(col)+str(row)+str(ROWS)
	                		ser.write(code.encode('utf-8'))
	                		print(code)
	                		print('12')

	                if game.num2==2 and game.player==2:
                		if count%2==0:
                			code='1'+str(col)+str(row)+str(ROWS)
                			ser.write(code.encode('utf-8'))
                			print(code)
                			print('21')
	                if game.num2==1 and game.player==2:
                		if count%2==0:
	                		code='2'+str(col)+str(row)+str(ROWS)
	                		ser.write(code.encode('utf-8'))
	                		print(code)
	                		print('22')
	                	
                	if keys[pygame.K_UP] and keys[pygame.K_i]:
                		game.running = False

            if keys[pygame.K_UP] and keys[pygame.K_e]:
                game.player = 2
                state=2
                print('enemy firt')
            if keys[pygame.K_UP] and keys[pygame.K_p]:   
                game.player = 1
                state=1
                print('player firt')
              
            if keys[pygame.K_UP] and keys[pygame.K_o]:	
                    game.num1 = 2
                    game.num2 = 1
                    print('you choose O,enemy X')
            if keys[pygame.K_UP] and keys[pygame.K_x]:
                    game.num1 = 1
                    game.num2 = 2 
                    print('you choose X,enemy O')
def tictactoe():
	main()
def fivexfive():
	
	global ROWS
	global COLS
	print(ROWS)
	print(COLS)
	ROWS=5
	COLS=5
def sevenxseven():
	global ROWS
	global COLS
	print(ROWS)
	print(COLS)
	ROWS=7
	COLS=7

#FORWARD:
lable0=Label(root,text="FORWARD", font=('Comic Sans MS',15,'bold'),fg='black',bg='gray').place(x=15,y=2)

lable1=Label(root,text="X", font=('Comic Sans MS',15,'bold'),fg='black',bg='gray').place(x=15,y=52)
entry1=Entry(root,width=20)
entry1.place(x=40,y=60)

lable2=Label(root,text="Y", font=('Comic Sans MS',15,'bold'),fg='black',bg='gray').place(x=15,y=102)
entry2=Entry(root,width=20)
entry2.place(x=40,y=110)

lable3=Label(root,text="Z", font=('Comic Sans MS',15,'bold'),fg='black',bg='gray').place(x=15,y=152)
entry3=Entry(root,width=20)
entry3.place(x=40,y=160)

button1 =Button(root,text="run", font=('Comic Sans MS',15,'bold'),fg='black',bg='gray',width=10,command=fivexfive).place(x=200,y=70)
button1 =Button(root,text="Home", font=('Comic Sans MS',15,'bold'),fg='black',bg='gray',width=10,command=home).place(x=200,y=125)

#INVERSE:
lable00=Label(root,text="INVERSE", font=('Comic Sans MS',15,'bold'),fg='black',bg='gray').place(x=400,y=2)

lable11=Label(root,text="X", font=('Comic Sans MS',15,'bold'),fg='black',bg='gray').place(x=400,y=52)
entry11=Entry(root,width=20)
entry11.place(x=425,y=60)

lable22=Label(root,text="Y", font=('Comic Sans MS',15,'bold'),fg='black',bg='gray').place(x=400,y=102)
entry22=Entry(root,width=20)
entry22.place(x=425,y=110)

lable33=Label(root,text="Z", font=('Comic Sans MS',15,'bold'),fg='black',bg='gray').place(x=400,y=152)
entry33=Entry(root,width=20)
entry33.place(x=425,y=160)

button11 =Button(root,text="run", font=('Comic Sans MS',15,'bold'),fg='black',bg='gray',width=10,command=sevenxseven).place(x=585,y=70)
button11 =Button(root,text="Home", font=('Comic Sans MS',15,'bold'),fg='black',bg='gray',width=10,command=home).place(x=585,y=125)

button2 =Button(root,text="tic tac toe", font=('Comic Sans MS',15,'bold'),fg='black',bg='gray',width=10,command=tictactoe).place(x=300,y=200)
root.mainloop()