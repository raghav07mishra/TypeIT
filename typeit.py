from tkinter import *
import random
from tkinter import messagebox

############################################# Words List ###############################################

words = ['Grapes','Mango','Apple','Gun','Fan','TV','Mobile','Laptop']

############################################# Function  ##################################################

def labelSlider():
    global counts,sliderwords
    text = 'Lets GO!'
    if counts>=len(text):
        counts=0
        sliderwords=' '
    sliderwords+=text[counts]
    counts+=1
    fontLabel.configure(text=sliderwords)  
    fontLabel.after(599,labelSlider)  

def timeleft():
    global time,miss,score
    if time<=10:
        timeLabelCount.configure(fg='red')
    else:
        pass    
    if time>0:
        time-=1
        timeLabelCount.configure(text=time)
        timeLabelCount.after(1000,timeleft)
    else:
        gameplayDetail.configure(text='Hit = {} | Miss = {} | Score = {}'.format(score,miss,total))
        rr = messagebox.askyesno('Notification','Play Again?')
        if rr==True:
            score=0
            time=60
            miss=0
            total=0
            timeLabelCount.configure(text=time)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)



def startGame(event):
    global score,miss,total
    if time==60:
        timeleft()
    gameplayDetail.configure(text=' ')
    if wordEntry.get() == wordLabel['text']:
        score+=1
        total+=1
        scoreLabelCount.configure(text=total)
    else:
        total-=1
        miss+=1 
        scoreLabelCount.configure(text=total)
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)              # Here we delete the entered word after enter is pressed



############################################# Root Method #################################################

root = Tk()                              # this will create our screen
root.geometry('800x600+250+30')          # setting the size of window
root.configure(bg='powder blue')
root.title('TypeIt')
root.iconbitmap('typeit.ico')

############################################## Variable  ##################################################

score = 0
time = 60
counts = 0
sliderwords = ' '
miss =0
total = 0





############################################## Label Method ###############################################

fontLabel = Label(root,text=' ',font=('airal',25,'bold'),bg='powder blue',fg='red',width=30)
fontLabel.place(x=90,y=10)
labelSlider()
random.shuffle(words)
wordLabel = Label(root,text=words[0],font=('airal',40,'bold'),bg='powder blue')
wordLabel.place(x=310,y=200)

scoreLabel = Label(root,text='Your Score',font=('airal',25,'bold'),bg='powder blue')
scoreLabel.place(x=40,y=120)

scoreLabelCount = Label(root,text=score,font=('airal',25,'bold'),bg='powder blue',fg='blue')
scoreLabelCount.place(x=90,y=180)

timeLabel = Label(root,text='Time Left',font=('airal',25,'bold'),bg='powder blue')
timeLabel.place(x=600,y=120)

timeLabelCount = Label(root,text=time,font=('airal',25,'bold'),bg='powder blue',fg='blue')
timeLabelCount.place(x=690,y=180)

gameplayDetail = Label(root,text='Type word and hit enter',font=('airal',30,'italic bold'),bg='powder blue',fg='dark grey')
gameplayDetail.place(x=190,y=450)




############################################## Entry Method ###############################################

wordEntry = Entry(root,font=('airal',25,'bold'),justify='center',bd=10)
wordEntry.place(x=220,y=300)
wordEntry.focus_set()


root.bind('<Return>',startGame)   # as we press enter our start func will be called
root.mainloop()