from tkinter import *
import random
from tkinter import messagebox
#root method
root=Tk()
root.geometry('800x600+400+100')
root.configure(bg='#EBE4D1')
root.title("Typing Speed Tester")
root.iconbitmap("logotype.ico")

#sliding function
def labelslider():
    global count,sliderwords
    text="Enter the text in the box below and hit enter   "
    if(count>=len(text)):
        count=0
        sliderwords=''
    sliderwords+=text[count]
    count+=1
    slide_label.configure(text=sliderwords)
    slide_label.after(160,labelslider)

def time():
    global score,miss,timeleft
    if(timeleft<11):
        timer_label_count.configure(fg="red")
    if(timeleft>0):
        timeleft-=1
        timer_label_count.configure(text=timeleft)
        timer_label_count.after(1000,time)
    else:
        gameplay_detail_label.configure(text="Correct = {} | Wrong = {} | Total Score = {}".format(score,miss,score-miss))
        accuracy_label.configure(text="Accuracy = {}% | WPM = {}".format(round((score/(score+miss))*100,2),round(no_of_words/2,2)))
        rr=messagebox.askretrycancel("Notification","To Play Again Hit Retry Button")
        if(rr==True):
            score = 0
            timeleft = 120
            miss = 0
            timer_label_count.configure(text=timeleft)
            word_label.configure(text=words[0])
            score_label_count.configure(text=score)
            gameplay_detail_label.configure(text="Typing Practice Makes you a Faster")
            accuracy_label.configure(text="")
            timer_label_count.configure(fg="#26577C")
        else:
            root.destroy()
            exit()

def startgame(event):
    global score,miss,no_of_words
    if(timeleft==120):
        time()
    if(word_entry.get()==word_label['text']):
        score+=1
        no_of_words+=len(word_label['text'].split())
        #print(no_of_words)
        score_label_count.configure(text=score)
    else:
        miss+=1
    random.shuffle(words)
    word_label.configure(text=words[10])
    word_entry.delete(0,END)
    


#variables
score=0
timeleft=120
count=0
sliderwords=''
words=["Brinjal","Apple","Mango","Banana","Grapes","Onion","Car","Cat","Window","Jungle","Water","asia","india","newyork","Earth","river","lake","mountains","africa","lion","dog","tiger","university","institute","forest","dinosaur","ancient","angry","sad","buffer","computer","science","information","technology","intelligence","master","bussiness","books","evil","Python Developer","Village","time","very noisy","water","Failure","Success","Don't overthink","Object oriented programming","Data Structures","algorithms","brown fox","lazy dog","Future","Realization","favourite color","google email","Speed typing","amazon company","service","Hyderabad"," Telangana","horror movies","Very intresting","walking","vitamins and minerals","drinking milk","health","tomatoes","sister","brought","gift","Crying","hope"]
miss=0
no_of_words=0

#label method
font_label = Label(root,text="Typing Speed Tester",bg="#EBE4D1",fg="#952323",font=("arial",25,"bold"))
font_label.place(x=230,y=10)

random.shuffle(words)
word_label=Label(root,text=words[0],bg="#EBE4D1",fg="#4477CE",font=("arial",28,"bold"),justify='center',width=34)
word_label.place(x=10,y=250)

score_label=Label(root,text="Your Score : ",font=("arial",25,"bold"),bg="#EBE4D1",fg="#79155B")
score_label.place(x=10,y=90)

score_label_count=Label(root,text=score,font=("arial",25,"bold"),bg="#EBE4D1",fg="#26577C")
score_label_count.place(x=80,y=140)

timer_label=Label(root,text="Time Left : ",font=("arial",25,"bold"),bg="#EBE4D1",fg="#79155B")
timer_label.place(x=600,y=90)

timer_label_count=Label(root,text=timeleft,font=("arial",25,"bold"),bg="#EBE4D1",fg="#26577C")
timer_label_count.place(x=680,y=140)

slide_label=Label(root,text='',bg="#EBE4D1",fg="#F78CA2",font=("arial",25,"italic bold"),width=40)
slide_label.place(x=10,y=200)
labelslider()

gameplay_detail_label=Label(root,text='Typing Practice Makes you a Faster',bg="#EBE4D1",fg="#D80032",font=("arial",28,"bold"),justify='center',width=34)
gameplay_detail_label.place(x=10,y=420)

accuracy_label=Label(root,text='',bg="#EBE4D1",fg="#D80032",font=("arial",28,"bold"),justify='center',width=34)
accuracy_label.place(x=10,y=500)

#entry method
word_entry = Entry(root,font=("arial",25,"bold"),bd=1,justify='center',bg="#EEEDED",fg="#141E46")
word_entry.place(x=210,y=320)
word_entry.focus_set()#to keep the cursor in the entry box


root.bind('<Return>',startgame)

root.mainloop()
