from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as mc
import random 
from tkinter import messagebox as mb #for the dialogue boxes

#imports from matplotlib for drawing graphs and for tkinter binding
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
import pygame
pygame.mixer.init()
root= Tk()
root.title('Battleship')

#Home Screen
def firstscreen():
    global canvas1,pic
    canvas1=Canvas(root,width=1000,height=800)
    canvas1.pack()
    image = Image.open('sea2.jpg')
    image = image.resize((1000, 800), Image.ANTIALIAS) 
    pic= ImageTk.PhotoImage(image)
    canvas1.create_image(0,0,anchor=NW,image=pic)

    canvas1.create_text(515,250,text='BATTLESHIP',fill='azure',font=('century schoolbook',60,'bold'))
    canvas1.create_text(800,600,text='Pooja Premnath', fill='white',font=('century schoolbook',15))
    canvas1.create_text(800,630,text='Vaishnaviy S', fill='white',font=('century schoolbook',15))

    #the command=secondscreen takes the control to the function secondscreen()
    button1 =Button(text='PLAY', command=secondscreen, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
    button1.config(height=2,width=23)
    canvas1.create_window(510,370, window=button1)

    #the command=rules takes the control to the function rules()
    button1a=Button(text='RULES', command=rules, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
    button1a.config(height=2,width=23)
    canvas1.create_window(510,430, window=button1a)

    leader=Button(text='LEADERBOARD', command=leaderboardfromfsr, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
    leader.config(height=2,width=23)
    canvas1.create_window(510,490, window=leader)

    endgame=Button(text='QUIT', command=quitgame, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
    endgame.config(height=2,width=23)
    canvas1.create_window(510,550, window=endgame)



    
#Screen with the username entry field
def secondscreen():
    #this erases the picture and the rest of the content on the first screen
    canvas1.pack_forget()

    #making a new canvas for the second screen
    global canvas2
    canvas2=Canvas(root, width = 1000, height = 1000)
    canvas2.pack()
    image2 = Image.open('ship2.jpg')
    image2 = image2.resize((1000, 800), Image.ANTIALIAS)
    

    #inserting the pictures and creating an entry field
    global pic2   
    pic2= ImageTk.PhotoImage(image2)
    canvas2.create_image(0,0,anchor=NW,image=pic2)
    canvas2.create_text(380,140,text="Battleship",fill='black',font=('century schoolbook',55,'bold'))
    global button2
    button2=Button(text='Home', command=fsrfromcanvas2, bg='azure', fg='black', font=('helvetica', 9, 'bold'))
    button2.config(height=2,width=10)
    canvas2.create_window(50,50, window=button2)
    
    signup= Button(text='SIGN  UP', command=signup_entry, bg='azure', fg='black', font=('century schoolbook', 11,'bold'))
    signup.config(height=2,width=30)
    canvas2.create_window(390,410, window=signup)
    signin= Button(text='SIGN  IN', command=signin_entry, bg='azure', fg='black', font=('century schoolbook', 11,'bold'))
    signin.config(height=2,width=30)
    canvas2.create_window(390,330, window=signin)
    bye= Button(text='QUIT', command=quitgame, bg='azure', fg='black', font=('century schoolbook', 11,'bold'))
    bye.config(height=2,width=30)
    canvas2.create_window(390,490, window=bye)
    #accepts username and takes control the db() function
    
def signup_entry():
    global status
    status='signup'
    canvas2.pack_forget()
    global signupscreen
    signupscreen=Canvas(root, width = 1000, height = 1000)
    signupscreen.pack()
    image = Image.open('sea.jpg')
    image = image.resize((1000, 800), Image.ANTIALIAS) 
    global pic5
    pic5= ImageTk.PhotoImage(image)
    signupscreen.create_image(0,0,anchor=NW,image=pic5)
    global button2
    button2=Button(text='Home', command=fsrfromsignup, bg='azure', fg='black', font=('helvetica', 9, 'bold'))
    button2.config(height=2,width=10)
    signupscreen.create_window(50,50, window=button2)
    signupscreen.create_text(450,180,text='Sign Up',fill='azure',font=('century schoolbook',60,'bold'))
    signupscreen.create_text(430,260,text="Let's Get Started! Enter a username and password...",fill='orchid1',font=('Lucida Handwriting',15,'bold'))
    global entry1
    global entry2
    text=StringVar(value=('Times New Roman 30'))
    entry1 =Entry(root,font=text)
    entry2=Entry(root,font=text,show='*')
    entry1.configure(width=25)
    entry2.configure(width=25)
    signupscreen.create_window(500, 380, window=entry1)
    signupscreen.create_window(500,450,window=entry2)
    signupscreen.create_text(300,380,text="Username:",fill='azure',font=('century schoolbook',15,'bold'))
    signupscreen.create_text(300,450,text="Password:",fill='azure',font=('century schoolbook',15,'bold'))
    submit= Button(text='Submit', command=db, bg='azure', fg='black', font=('century schoolbook', 11,'bold'))
    submit.config(height=2,width=23)
    signupscreen.create_window(500,540, window=submit,tag='submitbutton')
    bye= Button(text='Quit', command=quitgame, bg='azure', fg='black', font=('century schoolbook', 11,'bold'))
    bye.config(height=2,width=23)
    signupscreen.create_window(870,660, window=bye)

def signin_entry():
    global status
    status='signin'
    canvas2.pack_forget()
    global signinscreen
    signinscreen=Canvas(root, width = 1000, height = 1000)
    signinscreen.pack()
    image = Image.open('ship6.jpg')
    image = image.resize((1000, 800), Image.ANTIALIAS) 
    global signinpic
    signinpic= ImageTk.PhotoImage(image)
    signinscreen.create_image(0,0,anchor=NW,image=signinpic)
    global button2
    button2=Button(text='Home', command=fsrfromsignin, bg='azure', fg='black', font=('helvetica', 9, 'bold'))
    button2.config(height=2,width=10)
    signinscreen.create_window(50,50, window=button2)
    signinscreen.create_text(310,180,text='Sign In',fill='black',font=('century schoolbook',60,'bold'))
    signinscreen.create_text(280,260,text="Enter your username and password...",fill='navy',font=('Lucida Handwriting',15,'bold'))
    global entry1
    global entry2
    text=StringVar(value=('Times New Roman 30'))
    entry1 =Entry(root,font=text)
    entry2=Entry(root,font=text,show='*')
    entry1.configure(width=25)
    entry2.configure(width=25)
    signinscreen.create_window(300, 380, window=entry1)
    signinscreen.create_window(300,450,window=entry2)
    signinscreen.create_text(100,380,text="Username:",fill='black',font=('century schoolbook',15,'bold'))
    signinscreen.create_text(100,450,text="Password:",fill='black',font=('century schoolbook',15,'bold'))
    submit= Button(text='Submit', command=db, bg='azure', fg='black', font=('century schoolbook', 11,'bold'))
    submit.config(height=2,width=23)
    signinscreen.create_window(300,550, window=submit)
    bye= Button(text='Quit', command=quitgame, bg='azure', fg='black', font=('century schoolbook', 11,'bold'))
    bye.config(height=2,width=23)
    signinscreen.create_window(870,660, window=bye)
    

#the screen with the rules, can be directed to from firstscreen()
def rules():
    #to erase the content of the first screen
    canvas1.pack_forget()

    #making a new canvas for the rules page
    global canvas3
    canvas3=Canvas(root,width=1000,height=800)
    canvas3.pack()
    image = Image.open('ship5.jpg')
    image = image.resize((1000, 800), Image.ANTIALIAS) 
    global pic3
    pic3= ImageTk.PhotoImage(image)
    canvas3.create_image(0,0,anchor=NW,image=pic3)
    
    
    
    #The rules of the game
    canvas3.create_text(450,350,text='''\t\t*The objective of the game is to sink all five of the enemy's ships.
\n\t\t*There are five ships of varying size placed on the grid.
\n\t\t*Take shots on the ships placed by clicking on any of the squares on the grid.
\n\t\t*The positions in which ships have been successfully hit are illuminated in red.
\n\t\t*If you have hit an empty area, the given coordinate is illuminated in white.
\n\t\t*The lesser the number of hits taken to sink all the ships, the better is your score.''',fill='alice blue',font=('Arial',16))

    canvas3.create_text(480,120,text='RULES',fill='gold',font=('century schoolbook',60,'bold'))
    
    #to go back to the first screen
    global button3
    button3=Button(text='Home', command=fsrfromrules, bg='azure', fg='black', font=('helvetica', 9, 'bold'))
    button3.config(height=2,width=10)
    canvas3.create_window(50,50, window=button3)



def db():
    conn=mc.connect(host='localhost',user='root',password='pooja',database='x')
    cur=conn.cursor()
    global f,p, entry1,entry2,submit
    f=entry1.get()
    p=entry2.get()
    def signup_check():
        global status
        cur.execute("select username from score")
        rec=cur.fetchall()
        if f!='' and p!='':
            for i in rec:
                if i==(f,):
                    signupscreen.create_text(450,600,text="Oops..It looks a user of the same name already exists. Enter another username.",fill='azure',font=('century schoolbook',15,'bold'),tag='invaliduser')
                    signupscreen.delete('invalidpass')
                    break

            else:
                if p!='':
                    cur.execute("""insert into score(username,password) values("%s","%s")"""%(f,p))
                    signupscreen.create_text(450,600,text="Yay! You're now ready to play. Click Play to Begin.",fill='azure',font=('century schoolbook',15,'bold'),tag='invalidpass')
                    entry1=Entry(root,state='disabled')
                    entry2=Entry(root,state='disabled')
                    signupscreen.delete('invaliduser')
                    signupscreen.delete('signupbutton')
                    conn.commit()
                    playbutton1=Button(text='PLAY', command=grid, bg='azure', fg='black', font=('century schoolbook', 11, 'bold'))
                    playbutton1.config(height=2,width=23)
                    signupscreen.create_window(500,540, window=playbutton1,tag='play')
    def signin_check():
        global status
        cur.execute('select username,password from score')
        rec=cur.fetchall()
        if f!='' and p!='':
            for i in rec:
                if i[0]==f:
                    if i[1]==p:
                        signinscreen.delete('label4')
                        signinscreen.delete('invalid')
                        signinscreen.create_text(300,650,text="You're Back!..Click Play to Begin",fill='black',font=('century schoolbook',20,'bold'),tag='label3')
                        playbutton2=Button(text='PLAY', command=grid, bg='azure', fg='black', font=('century schoolbook', 11, 'bold'))
                        playbutton2.config(height=2,width=23)
                        signinscreen.create_window(300,550, window=playbutton2,tag='play')
                        break
                
                    else:
                        signinscreen.create_text(300,650,text="Incorrect Password.. Try Again",fill='black',font=('century schoolbook',20,'bold'),tag='label4')
                        break
                    
            else:
                signinscreen.create_text(400,640,text="You might have entered an incorrect username, \nor you're not in our records yet. Try Again or Sign up instead.",fill='black',font=('century schoolbook',15,'bold'),tag='invalid')
                signup= Button(text='Sign Up', command=signupfromsignin, bg='azure', fg='black', font=('century schoolbook', 11,'bold'))
                signup.config(height=2,width=23)
                signinscreen.create_window(560,550, window=signup)
                signinscreen.delete('label3')
                signinscreen.delete('label4')
    if status=='signup':
        signup_check()
    else:
        signin_check()
    conn.close()

def grid():
    #this is the main game screen
   global f,status,signupscreen,signinscreen,origin
   origin='game'
   conn=mc.connect(host='localhost',user='root',password='pooja',database='x')
   cur=conn.cursor()
   cur.execute("""select bestscore from score where username='%s'"""%(f))
   best=cur.fetchone()
   conn.close()
   if status=='signin':
       signinscreen.pack_forget()
   else:
       signupscreen.pack_forget()
   
   global canvas4
   canvas4=Canvas(root,width=1000,height=800)
   canvas4.pack()
   image = Image.open('main2.jpg')
   image = image.resize((1000, 800), Image.ANTIALIAS) 
   global pic  
   pic= ImageTk.PhotoImage(image)
   canvas4.create_image(0,0,anchor=NW,image=pic)

   #the text on the main game screen
   canvas4.create_text(800,50,text='Battleship', fill='white',font=('century schoolbook',30,'bold'))
   canvas4.create_text(750,100,text='Number of ships sunk:', fill='white',font=('Times New Roman',15,'bold'),tag='line1')
   canvas4.create_text(755,130,text='Number of Attempts:', fill='white',font=('Times New Roman',15,'bold'),tag='line2')
   canvas4.create_text(920,120,text='___', fill='white',font=('Times New Roman',15,'bold'),tag='blank')
   canvas4.create_text(770,160,text='Your Best Score:', fill='white',font=('Times New Roman',15,'bold'),tag='line3')
   if best!=None and best[0]!=100:   
       canvas4.create_text(920,160,text='{}'.format(best[0]), fill='white',font=('Times New Roman',15,'bold'),tag='line5')
   else:
       canvas4.create_text(920,160,text='NA', fill='white',font=('Times New Roman',15,'bold'),tag='line5')
   canvas4.create_text(350,30,text='{}, Try to find all the ships hidden in as few attempts as possible...'.format(f), fill='gold',font=('Times New Roman',15))
   

   #image of aircraft carrier
   image = Image.open('aircraftcarrierfinal.png')
   image = image.resize((300, 100), Image.ANTIALIAS) 
   global aircraftcarrier  
   aircraftcarrier= ImageTk.PhotoImage(image)
   canvas4.create_image(750,220,image=aircraftcarrier)
   canvas4.create_text(700,190,text='Aircraft Carrier:5 units', fill='white',font=('Times New Roman',10))

   #image of battleship
   image = Image.open('battleshipfinal.png')
   image = image.resize((250, 100), Image.ANTIALIAS) 
   global battleship
   battleship= ImageTk.PhotoImage(image)
   canvas4.create_image(750,325,image=battleship)
   canvas4.create_text(680,295,text='Battleship:4 units', fill='white',font=('Times New Roman',10))

   #image of submarine
   image = Image.open('submarinefinal.png')
   image = image.resize((200, 100), Image.ANTIALIAS) 
   global submarine
   submarine= ImageTk.PhotoImage(image)
   canvas4.create_image(730,420,image=submarine)
   canvas4.create_text(680,390,text='Submarine:3 units', fill='white',font=('Times New Roman',10))

   #image of cruiser
   image = Image.open('cruiserfinal.png')
   image = image.resize((200, 100), Image.ANTIALIAS) 
   global cruiser
   cruiser= ImageTk.PhotoImage(image)
   canvas4.create_image(730,520,image=cruiser)
   canvas4.create_text(680,475,text='Cruiser:3 units', fill='white',font=('Times New Roman',10))

   #image of destroyer
   image = Image.open('destroyerfinal.png')
   image = image.resize((150, 80), Image.ANTIALIAS) 
   global destroyer
   destroyer= ImageTk.PhotoImage(image)
   canvas4.create_image(710,620,image=destroyer)
   canvas4.create_text(680,585,text='Destroyer:2 units', fill='white',font=('Times New Roman',10))

   # d is a dictionary which contains all the 100 coordinates on the grid
   global d
   d=grid_coordinates()

      #drawing the vertical and horizontal lines on the screen to make the grid
   y=100
   for i in range(11):
       canvas4.create_line(100,y,600,y,fill='white')
       y+=50


   x=100
   for i in range(11):
       canvas4.create_line(x,100,x,600,fill='white')
       x+=50

   #These are the numbers which are present on either side of the board to indicate the x and y coordinates
   txc=130
   yc=80
   for i in range(1,11):
       canvas4.create_text(txc,yc,text=str(i),fill='white',font=('century schoolbook',30,'bold'))
       txc+=50
   lxc=75
   lyc=125
   for i in range(1,11):
       canvas4.create_text(lxc,lyc,text=str(i),fill='white',font=('century schoolbook',30,'bold'))
       lyc+=50
       
   #square is a list with the dictionary coordinates that have been clicked
   global squares
   squares=[]
    
   #these functions take the control to mousepos() which controls all mouse movement of the game
   canvas4.bind("<Button-1>",lambda event, arg=shipdict: mousepos(event, arg))
   canvas4.bind("<Button-1>",lambda event,arg=occupied: mousepos(event,arg))
   canvas4.pack()


   
   quitbutton=Button(text='FORFEIT', command=forfeit, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
   quitbutton.config(height=2,width=23)
   canvas4.create_window(890,680, window=quitbutton,tag='forfeitbutton')

   #the gameover variable makes sure that after forfeiting the game, no more mouse clicks can be made on the board
   global gameover
   gameover=False
   conn.close()

#major game loop
def mousepos(event,arg):
    conn=mc.connect(host='localhost',user='root',password='pooja',database='x')
    cur=conn.cursor()
    global hitdict
    global f
    global squares
    global white
    global red
    global hit
    global miss
    global shipdict
    
    #arg refers to shipdict and occupied, which are a dictionary of ship positions, and a list of the previously occupied positions on the board
    if gameover==True:
        return
    #coordinate takes the x and y coordinates of the mouse click
    coordinate=(event.x,event.y)
    
    
    #iterating through the dictionary to check if a the coordinate entered is occupied or not/within the grid
    for i in d:
        if d[i][0]<coordinate[0]<d[i][2] and d[i][1]<coordinate[1]<d[i][3]:
            
            if i in occupied:
                canvas4.create_rectangle(d[i],fill='red',tag='rect')
                canvas4.delete('outseapos')
                #squares has a list of all the rectangles.. is used later for erasing the colours on the board
                squares.append(d[i])
                if d[i] not in red:
                    boomsound() 
                    red.append(d[i])
                    hit+=1
                    scoretracking()
                    for j in shipdict:
                        for k in shipdict[j]:
                            if k==i:
                                hitdict[j].append(i)
                                
                                
                sink=0
                for i in shipdict:
                    if all(item in hitdict[i] for item in shipdict[i]):
                        if i=='aircraft carrier':
                            global check1
                            image = Image.open('checkfinal.png') 
                            check1= ImageTk.PhotoImage(image)
                            canvas4.create_image(920,230,image=check1)
                            shiponboard(i)
                                
                        elif i=='battleship':
                            
                            global check2
                            image = Image.open('checkfinal.png') 
                            check2= ImageTk.PhotoImage(image)
                            canvas4.create_image(920,330,image=check2)
                            shiponboard(i)
                                   
                        elif i=='submarine':
                            
                            global check3
                            image = Image.open('checkfinal.png') 
                            check3= ImageTk.PhotoImage(image)
                            canvas4.create_image(920,430,image=check3)
                            shiponboard(i)
                                    
                        elif i=='cruiser':
                            
                            global check4
                            image = Image.open('checkfinal.png') 
                            check4= ImageTk.PhotoImage(image)
                            canvas4.create_image(920,530,image=check4)
                            shiponboard(i)
                                    
                        elif i=='destroyer':
                            global check5
                            image = Image.open('checkfinal.png') 
                            check5= ImageTk.PhotoImage(image)
                            canvas4.create_image(920,630,image=check5)
                            shiponboard(i)
                                
                        sink+=1
                        
                        canvas4.delete('sink')
                        canvas4.create_text(920,100,text=sink, fill='white',font=('Times New Roman',15,'bold'),tag='sink')
                       
                if sink==5:
                    win()
                    winsound()
                    cur.execute("""update score set bestscore=("%d") where username=("%s") and bestscore>=("%d")"""%(hit+miss,f,hit+miss))
                    conn.commit()
    
            else:
                canvas4.create_rectangle(d[i],fill='white',tag='rect')
                canvas4.delete('outseapos')
                squares.append(d[i])
                if d[i] not in white:
                    white.append(d[i])
                    miss+=1
                    scoretracking()
            
            
            break
        
    else:
        canvas4.delete('seapos')#what is this?
        canvas4.create_text(350,650,text='Oops..You tried to make a shot outside the sea!',fill='red',font=('Times New Roman',20,'bold'),tag='outseapos')
    

def grid_coordinates():
    #meant to initialize a dictionary full of grid coordinates
    global d
    d={}
    x1=100
    y1=100
    x2=150
    y2=150
    for i in range(1,11):
       for j in range(1,11):
           d[(j,i)]=(x1,y1,x2,y2)
           x1+=50
           x2+=50
       x1=100
       x2=150
       y1+=50
       y2+=50
   
    return d


#assignshippos and shippos are the functions that initally run upon execution of the program to assign coordinates to the ships
occupied=[]
shipdict={}
direction=['horizontal','vertical']
def assignshippos():
    #meant to assign positions for each ship on the board in relation with the shippos function 
    global shipname
    shipname=['aircraft carrier','battleship','cruiser','submarine','destroyer']
    global count
    count=0
    global shiplength
    shiplength=[5,4,3,3,2]
    while count<5:
        shippos()
        
def shippos():
    #assignment of the grid coordinates of each type of ship by checking for empty positions on the board
    global count
    global ship
    global shiplength
    ship=[]
    sc=(random.randrange(1,11),random.randrange(1,11))
    shipdir=random.choice(direction)
    if sc in occupied:
        return
    else:
    
        if shipdir=='horizontal':
            for i in range(sc[0]+1,(sc[0]+shiplength[count])):
                if (i,sc[1]) in occupied or i>10:
                    return
            else:
                occupied.append(sc)
                ship.append(sc)
                for i in range(sc[0]+1,sc[0]+shiplength[count]):
                    ship.append((i,sc[1]))
                    occupied.append((i,sc[1]))
                shipdict[shipname[count]]=ship
                count+=1
        else:
            for i in range(sc[1]+1,(sc[1]+shiplength[count])):
                if (sc[0],i) in occupied or i>10:
                    return
            else:
                occupied.append(sc)
                ship.append(sc)
                for i in range(sc[1]+1,sc[1]+shiplength[count]):
                    ship.append((sc[0],i))
                    occupied.append((sc[0],i))
            
                shipdict[shipname[count]]=ship
                count+=1

def scoretracking():
    global hit
    global miss
    canvas4.delete('blank')
    canvas4.delete('score')
    canvas4.create_text(920,130,text=hit+miss, fill='white',font=('Times New Roman',15,'bold'),tag='score')


def shiponboard(i):
    if i=='aircraft carrier':
        global ac
        if shipdict[i][0][0]==shipdict[i][1][0]:                   
            image = Image.open('aircraftcarrierfinal.png')
            image = image.resize((300, 70), Image.ANTIALIAS) 
            image=image.transpose(Image.ROTATE_90)
            ac= ImageTk.PhotoImage(image)
            canvas4.create_image(d[shipdict[i][0]][0]+20,d[shipdict[i][0]][3]+70,image=ac)
        
        else:                    
            image = Image.open('aircraftcarrierfinal.png')
            image = image.resize((300, 70), Image.ANTIALIAS) 
            ac= ImageTk.PhotoImage(image)
            canvas4.create_image(d[shipdict[i][0]][2]+80,d[shipdict[i][0]][3]-30,image=ac)
    elif i=='battleship':
        global bship
        if shipdict[i][0][0]==shipdict[i][1][0]:
                                
            image = Image.open('battleshipfinal.png')
            image = image.resize((200, 70), Image.ANTIALIAS) 
            image=image.transpose(Image.ROTATE_90)
            bship= ImageTk.PhotoImage(image)
            canvas4.create_image(d[shipdict[i][0]][0]+30,d[shipdict[i][0]][3]+50,image=bship)
        else:
                                
            image = Image.open('battleshipfinal.png')
            image = image.resize((200, 70), Image.ANTIALIAS) 
            bship= ImageTk.PhotoImage(image)
            canvas4.create_image(d[shipdict[i][0]][2]+60,d[shipdict[i][0]][3]-20,image=bship)
    elif i=='submarine':
        global sub
        if shipdict[i][0][0]==shipdict[i][1][0]:
                                
            image = Image.open('submarinefinal.png')
            image = image.resize((160, 70), Image.ANTIALIAS) 
            image=image.transpose(Image.ROTATE_90)
            sub= ImageTk.PhotoImage(image)
            canvas4.create_image(d[shipdict[i][0]][0]+30,d[shipdict[i][0]][3]+30,image=sub)
        else:
                                
            image = Image.open('submarinefinal.png')
            image = image.resize((160, 70), Image.ANTIALIAS) 
            sub= ImageTk.PhotoImage(image)
            canvas4.create_image(d[shipdict[i][0]][2]+25,d[shipdict[i][0]][3]-20,image=sub)
    elif i=='cruiser':
        global cship
        if shipdict[i][0][0]==shipdict[i][1][0]:
                                
            image = Image.open('cruiserfinal.png')
            image = image.resize((160, 70), Image.ANTIALIAS) 
            image=image.transpose(Image.ROTATE_90)
            cship= ImageTk.PhotoImage(image)
            canvas4.create_image(d[shipdict[i][0]][0]+20,d[shipdict[i][0]][3]+25,image=cship)
        else:
                                
            image = Image.open('cruiserfinal.png')
            image = image.resize((160, 70), Image.ANTIALIAS) 
            cship= ImageTk.PhotoImage(image)
            canvas4.create_image(d[shipdict[i][0]][2]+30,d[shipdict[i][0]][3]-30,image=cship)
            
    elif i=='destroyer':
        global dship
        if shipdict[i][0][0]==shipdict[i][1][0]:                   
            image = Image.open('destroyerfinal.png')
            image = image.resize((110, 60), Image.ANTIALIAS) 
            image=image.transpose(Image.ROTATE_90)
            dship= ImageTk.PhotoImage(image)
            canvas4.create_image(d[shipdict[i][0]][0]+20,d[shipdict[i][0]][3]-3,image=dship)
        else:
                                
            image = Image.open('destroyerfinal.png')
            image = image.resize((110, 60), Image.ANTIALIAS) 
            dship= ImageTk.PhotoImage(image)
            canvas4.create_image(d[shipdict[i][0]][2]+3,d[shipdict[i][0]][3]-30,image=dship)
                            

def forfeit():
    global d
    global gameover
    global squares
    global hit
    global miss
    
    #to initiate the forfeit action if the user really wants to quit
    
    if mb.askyesno('Forfeit Game','Do you really want to quit? Your progress will be lost.'):
        #when gameover is True, it will no longer allow mouse clicks on the board
        gameover=True
        hit=miss=0
        
        #iterating through squares to remove any already made attempts on the screen
        for i in squares:
            canvas4.delete('rect')    
        colours=['purple1','gold','magenta2','pale turquoise','SpringGreen2']
        count=0
        for i in shipdict:
            for j in range(len(shipdict[i])):
                canvas4.create_rectangle(d[shipdict[i][j]],fill=colours[count])
                shiponboard(i)
            count+=1
        canvas4.delete('forfeitbutton')
        canvas4.delete('outseapos')
        canvas4.create_text(350,650,text="It's OK... \nBetter luck next time!",fill='red',font=('Times New Roman',20,'bold'))
        #asking the user if he wants to play again
        replay=Button(text='Play Again', command=consolation, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
        replay.config(height=2,width=23)
        canvas4.create_window(890,680, window=replay)
        bye= Button(text='Quit', command=quitgame, bg='floral white', fg='black', font=('century schoolbook', 11,'bold'))
        bye.config(height=2,width=23)
        canvas4.create_window(660,680, window=bye)
        

def consolation():
    #meant to reinitialize all the values back to 0/empty for the new game
    global hitdict
    global squares
    global gameover
    global red
    global white
    global hit
    global miss
    global occupied
    global shipdict
    gameover=True
    canvas4.pack_forget()
    hitdict={'aircraft carrier':[],'battleship':[],'cruiser':[],'submarine':[],'destroyer':[]}
    occupied=[]
    shipdict={}
    assignshippos()
    print("The dictionary of ships is",shipdict)
    squares=[]
    red=[]
    white=[]
    hit=0
    miss=0
    #this rewinds the program to the first screen again
    firstscreen()
    
def win():
    global gameover
    global squares
    print('yay you have won the game')
    canvas4.delete('line1')
    canvas4.delete('line2')
    canvas4.delete('line3')
    canvas4.delete('score')
    canvas4.delete('sink')
    canvas4.delete('line5')
    canvas4.create_text(800,140,text="You Win!",fill='gold',font=('Lucida Handwriting',30))
    gameover=True
    canvas4.delete('forfeitbutton')
    canvas4.delete('outseapos')
    for i in squares:
        canvas4.delete('rect')    
        colours=['purple1','gold','magenta2','pale turquoise','SpringGreen2']
        count=0
        for i in shipdict:
            for j in range(len(shipdict[i])):
                canvas4.create_rectangle(d[shipdict[i][j]],fill=colours[count])
            count+=1
    replay=Button(text='Play Again', command=consolation, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
    replay.config(height=2,width=23)
    canvas4.create_window(890,680, window=replay)
    bye= Button(text='Quit', command=quitgame, bg='floral white', fg='black', font=('helvetica', 11,'bold'))
    bye.config(height=2,width=23)
    canvas4.create_window(430,680, window=bye)
    scorelist=Button(text='Leaderboard', command=leaderboard, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
    scorelist.config(height=2,width=23)
    canvas4.create_window(660,680, window=scorelist)

def leaderboardfromfsr():
    global origin
    canvas1.pack_forget()
    origin='front' 
    leaderboard()
    
def leaderboard():
    global origin
    conn=mc.connect(host='localhost',user='root',password='pooja',database='x')
    if origin!='front':
        canvas4.pack_forget()
    cur=conn.cursor()
    global canvas5
    canvas5=Canvas(root, width = 600, height = 1000)
    canvas5.pack()
    replay=Button(text='Home', command=fsrfromleaderboard, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
    replay.config(height=2,width=20)
    canvas5.create_window(300,650, window=replay)
    image = Image.open('leaderboard2.jpg')
    image = image.resize((1000, 800), Image.ANTIALIAS) 
    global pic5
    pic5= ImageTk.PhotoImage(image)
    canvas5.create_image(0,0,anchor=NW,image=pic5)
    
    #grid drawing
    y=100
    for i in range(7):
       canvas5.create_line(50,y,400,y,fill='black',width=3)
       y+=75
    canvas5.create_line(50,100,50,550,fill='black',width=3)
    canvas5.create_line(125,100,125,550,fill='black',width=3)
    canvas5.create_line(290,100,290,550,fill='black',width=3)
    canvas5.create_line(400,100,400,550,fill='black',width=3)
    canvas5.create_text(300,40,text='Leaderboard', fill='black',font=('century schoolbook',30,'bold'))
    canvas5.create_text(80,130,text='Rank', fill='black',font=('century schoolbook',15,'bold'))
    canvas5.create_text(210,130,text='Username', fill='black',font=('century schoolbook',15,'bold'))
    canvas5.create_text(345,130,text='Best Score', fill='black',font=('century schoolbook',15,'bold'))
    
    cur.execute('select username,bestscore from score order by bestscore')
    global top
    top=cur.fetchall()
    xcoordinate=80
    ycoordinate=200
    if len(top)>=5:
        for i in range(0,5):
            canvas5.create_text(xcoordinate,ycoordinate,text='{}'.format(i+1), fill='black',font=('century schoolbook',16,'bold'))
            canvas5.create_text(xcoordinate+120,ycoordinate,text='{}'.format(top[i][0]), fill='black',font=('century schoolbook',16,'bold'))
            canvas5.create_text(xcoordinate+260,ycoordinate,text='{}'.format(top[i][1]), fill='black',font=('century schoolbook',16,'bold'))
            ycoordinate+=80        
    else:
        for i in range(5):
            if i<len(top):
                canvas5.create_text(xcoordinate,ycoordinate,text='{}'.format(i+1), fill='black',font=('century schoolbook',16,'bold'))
                canvas5.create_text(xcoordinate+120,ycoordinate,text='{}'.format(top[i][0]), fill='black',font=('century schoolbook',16,'bold'))
                canvas5.create_text(xcoordinate+260,ycoordinate,text='{}'.format(top[i][1]), fill='black',font=('century schoolbook',16,'bold'))
                ycoordinate+=80        
            else:
                canvas5.create_text(xcoordinate,ycoordinate,text='{}'.format(i+1), fill='black',font=('century schoolbook',16,'bold'))
                canvas5.create_text(xcoordinate+120,ycoordinate,text='NA', fill='black',font=('century schoolbook',16,'bold'))
                canvas5.create_text(xcoordinate+260,ycoordinate,text='NA', fill='black',font=('century schoolbook',16,'bold'))
                ycoordinate+=80      
                
    print(top)
    graph=Button(text='View Bar Graph of Statistics', command=plot, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
    graph.config(height=2,width=50)
    canvas5.create_window(300,600, window=graph)
    

def plot():
    global top
    top_win = Toplevel(root)
    if len(top)>=5:
        x =[top[4][1],top[3][1],top[2][1],top[1][1],top[0][1]]
    else:
        x=[]
        for i in range(5):
            if i<len(top):
                x.insert(0,top[i][1])
            else:
                x.insert(0,0)
            
    y=[top[4][0],top[3][0],top[2][0],top[1][0],top[0][0]]
    c=['deeppink','mediumorchid','slateblue','turquoise','lime']
    fig = plt.figure(figsize=(8,8))
    plt.barh(y,x,0.5,color=c)
    plt.title('Leaderboard Rankings')
    plt.xlabel('Number of Attempts')
    plt.ylabel('Username')
    for x,y in zip(x,y):
        label="{:.2f}".format(x)
        
        plt.annotate(label,
                     (x,y),
                     textcoords="offset points",
                     xytext=(13,0),
                     ha='center')
    
    canvas = FigureCanvasTkAgg(fig, master=top_win)
    canvas.draw()
    canvas.get_tk_widget().pack()

    
def boomsound():
    pygame.mixer.music.load('C:\\Users\\Pooja\\Documents\\Pooja\\Class XII\\Computer Science\\Computer Science Project\\Boom.mp3')
    pygame.mixer.music.play(loops=0)

def winsound():
    pygame.mixer.music.load('C:\\Users\\Pooja\\Documents\\Pooja\\Class XII\\Computer Science\\Computer Science Project\\Victory2.mp3')
    pygame.mixer.music.play(loops=0)

#these two functions are responsible for moving between screens
def fsrfromcanvas2():
    canvas2.pack_forget()
    firstscreen()    

def fsrfromrules():
    canvas3.pack_forget()
    firstscreen()

def fsrfromsignup():
    signupscreen.pack_forget()
    firstscreen()

def fsrfromsignin():
    signinscreen.pack_forget()
    firstscreen()

def signupfromsignin():
    signinscreen.pack_forget()
    signup_entry()


    
def fsrfromleaderboard():
    global hitdict
    global squares
    global gameover
    global red
    global white
    global hit
    global miss
    global occupied
    global shipdict
    
    canvas5.pack_forget()
    occupied=[]
    shipdict={}
    assignshippos()
    print("The dictionary of ships is",shipdict)
    squares=[]
    red=[]
    white=[]
    hit=0
    miss=0
    firstscreen()
    

       
def quitgame():
    if mb.askyesno('Quit Game','Do you really want to quit the game?'):
        root.destroy()
#main body
red=[]
white=[]
hit=0
miss=0
hitdict={'aircraft carrier':[],'battleship':[],'cruiser':[],'submarine':[],'destroyer':[]}
firstscreen()
assignshippos()
#These are the answers to the ship positions
print("The dictionary of ships is",shipdict)






