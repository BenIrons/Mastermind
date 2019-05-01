import random
import tkinter

root = tkinter.Tk()

c = tkinter.Canvas(root, bg='grey', height=900, width=400)
#purple = "#d896ff" - 0
#blue = "#63b8ff" - 1 
#green = "#9aff9a" - 2
#yellow = "#ffff99" - 3
#red = "#ff4040" - 4
#pink = "#ffaeb9" - 5
RandNum = random.sample(range(1,7),4)
print (RandNum)
def Hidden1():
    if RandNum[0] == 1:
        return "#d896ff"
    elif RandNum[0] == 2:
        return "#63b8ff"
    elif RandNum[0] == 3:
        return "#9aff9a"
    elif RandNum[0] == 4:
        return "#ffff99"
    elif RandNum[0] == 5:
        return "#ff4040"
    elif RandNum[0] == 6:
        return "#ffaeb9"
def Hidden2():
    if RandNum[1] == 1:
        return "#d896ff"
    elif RandNum[1] == 2:
        return "#63b8ff"
    elif RandNum[1] == 3:
        return "#9aff9a"
    elif RandNum[1] == 4:
        return "#ffff99"
    elif RandNum[1] == 5:
        return "#ff4040"
    elif RandNum[1] == 6:
        return "#ffaeb9"
def Hidden3():
    if RandNum[2] == 1:
        return "#d896ff"
    elif RandNum[2] == 2:
        return "#63b8ff"
    elif RandNum[2] == 3:
        return "#9aff9a"
    elif RandNum[2] == 4:
        return "#ffff99"
    elif RandNum[2] == 5:
        return "#ff4040"
    elif RandNum[2] == 6:
        return "#ffaeb9"
def Hidden4():
    if RandNum[3] == 1:
        return "#d896ff"
    elif RandNum[3] == 2:
        return "#63b8ff"
    elif RandNum[3] == 3:
        return "#9aff9a"
    elif RandNum[3] == 4:
        return "#ffff99"
    elif RandNum[3] == 5:
        return "#ff4040"
    elif RandNum[3] == 6:
        return "#ffaeb9"
  
#(top left corner x,y),(bottom right corner x,y)
#Hidden Code BOX + Hidden CODE:
c.create_rectangle(15,10,388,110, fill="#a9a9a9")#hidden code box
c.create_oval(19,17,110,107,  fill= Hidden1())#Purple
c.create_oval(112,17,200,107, fill= Hidden2())#Blue
c.create_oval(202,17,290,107, fill= Hidden3())#Green
c.create_oval(292,17,380,107, fill= Hidden4())#Yellow

#Guess Area:
c.create_rectangle(15,125,296,683, fill="#a9a9a9")#main guess box
c.create_rectangle(302,125,388,683, fill="#a9a9a9")
#Gap in between ovals is 2 gap between oval and edge of box 4 diameter of oval is 67

####check buttons
ticked1 = 0

def tickedColour():
    if ticked1 == 0:
        return c.itemconfig(checkButton1, fill="#a9a9a9")
    elif ticked1 == 1:
        global row1
        row1 = [0,0,0,0]
        row1 = [currentColour1A,currentColour1B,currentColour1C,currentColour1D]
        print(row1)
        feedback()
        return c.itemconfig(checkButton1, fill="#5eff5e")

def ifTicked(self):
    global ticked1
    ticked1 = ticked1 + 1
    if ticked1 > 1:
        ticked1 = 1
    tickedColour()

global currentColour1A
currentColour1A = 0

checkButton1 = "please work"
checkButton1 = c.create_rectangle(355,640,377,660, fill=tickedColour())
c.create_rectangle(355,640,377,660, fill=tickedColour())
c.tag_bind(checkButton1, "<1>", ifTicked)

###Button 1A
def colourChange1A():
    if currentColour1A == 0:
        return "white"
    elif currentColour1A == 1:
        return c.itemconfig(button1a, fill="#d896ff")
    elif currentColour1A == 2:
        return c.itemconfig(button1a,fill="#63b8ff")
    elif currentColour1A == 3:
        return c.itemconfig(button1a ,fill="#9aff9a")
    elif currentColour1A == 4:
        return c.itemconfig(button1a ,fill="#ffff99")
    elif currentColour1A == 5:
        return c.itemconfig(button1a ,fill="#ff4040")
    elif currentColour1A == 6:
        return c.itemconfig(button1a ,fill="#ffaeb9")
    
def command1A(self):
    global currentColour1A
    currentColour1A = currentColour1A + 1
    if currentColour1A > 6:
        currentColour1A = 0
    colourChange1A()
###Button 1B    
currentColour1B = 0
def colourChange1B():
    if currentColour1B == 0:
        return "white"
    elif currentColour1B == 1:
        return c.itemconfig(button1b, fill="#d896ff")
    elif currentColour1B == 2:
        return c.itemconfig(button1b,fill="#63b8ff")
    elif currentColour1B == 3:
        return c.itemconfig(button1b ,fill="#9aff9a")
    elif currentColour1B == 4:
        return c.itemconfig(button1b ,fill="#ffff99")
    elif currentColour1B == 5:
        return c.itemconfig(button1b ,fill="#ff4040")
    elif currentColour1B == 6:
        return c.itemconfig(button1b ,fill="#ffaeb9")
    
def command1B(self):
    global currentColour1B
    currentColour1B = currentColour1B + 1
    if currentColour1B > 6:
        currentColour1B = 0
    colourChange1B()
###Button 1C
currentColour1C = 0
def colourChange1C():
    if currentColour1C == 0:
        return "white"
    elif currentColour1C == 1:
        return c.itemconfig(button1c, fill="#d896ff")
    elif currentColour1C == 2:
        return c.itemconfig(button1c,fill="#63b8ff")
    elif currentColour1C == 3:
        return c.itemconfig(button1c ,fill="#9aff9a")
    elif currentColour1C == 4:
        return c.itemconfig(button1c ,fill="#ffff99")
    elif currentColour1C == 5:
        return c.itemconfig(button1c ,fill="#ff4040")
    elif currentColour1C == 6:
        return c.itemconfig(button1c ,fill="#ffaeb9")
    
def command1C(self):
    global currentColour1C
    currentColour1C = currentColour1C + 1
    if currentColour1C > 6:
        currentColour1C = 0
    colourChange1C()
###Button 1D
currentColour1D = 0
def colourChange1D():
    if currentColour1D == 0:
        return "white"
    elif currentColour1D == 1:
        return c.itemconfig(button1d, fill="#d896ff")
    elif currentColour1D == 2:
        return c.itemconfig(button1d,fill="#63b8ff")
    elif currentColour1D == 3:
        return c.itemconfig(button1d ,fill="#9aff9a")
    elif currentColour1D == 4:
        return c.itemconfig(button1d ,fill="#ffff99")
    elif currentColour1D == 5:
        return c.itemconfig(button1d ,fill="#ff4040")
    elif currentColour1D == 6:
        return c.itemconfig(button1d ,fill="#ffaeb9")
    
def command1D(self):
    global currentColour1D
    currentColour1D = currentColour1D + 1
    if currentColour1D > 6:
        currentColour1D = 0
    colourChange1D()
#row 1
button1a = c.create_oval(19,614,84,679, fill= colourChange1A())
c.tag_bind(button1a, "<Button 1>", command1A)
button1b = c.create_oval(88,614,153,679, fill= colourChange1B())
c.tag_bind(button1b, "<Button 1>", command1B)
button1c = c.create_oval(157,614,222,679, fill= colourChange1C())
c.tag_bind(button1c, "<Button 1>", command1C)
button1d = c.create_oval(226,614,292,679, fill= colourChange1D())
c.tag_bind(button1d, "<Button 1>", command1D)


#row 2
c.create_oval(19,545,84,610, fill="white")
c.create_oval(88,545,153,610, fill="white")
c.create_oval(157,545,222,610, fill="white")
c.create_oval(226,545,292,610, fill="white")
#row 3
c.create_oval(19,476,84,541, fill="white")
c.create_oval(88,476,153,541, fill="white")
c.create_oval(157,476,222,541, fill="white")
c.create_oval(226,476,292,541, fill="white")
#row 4
c.create_oval(19,407,84,472, fill="white")
c.create_oval(88,407,153,472, fill="white")
c.create_oval(157,407,222,472, fill="white")
c.create_oval(226,407,292,472, fill="white")
#row 5
c.create_oval(19,338,84,403, fill="white")
c.create_oval(88,338,153,403, fill="white")
c.create_oval(157,338,222,403, fill="white")
c.create_oval(226,338,292,403, fill="white")
#row 6
c.create_oval(19,269,84,334, fill="white")
c.create_oval(88,269,153,334, fill="white")
c.create_oval(157,269,222,334, fill="white")
c.create_oval(226,269,292,334, fill="white")
#row 7
c.create_oval(19,200,84,265, fill="white")
c.create_oval(88,200,153,265, fill="white")
c.create_oval(157,200,222,265, fill="white")
c.create_oval(226,200,292,265, fill="white")
#row 8
c.create_oval(19,131,84,196, fill="white")
c.create_oval(88,131,153,196, fill="white")
c.create_oval(157,131,222,196, fill="white")
c.create_oval(226,131,292,196, fill="white")
#Feedback pegs
def feedback():
    global redPeg
    global whitePeg
    row1 = [currentColour1A,currentColour1B,currentColour1C,currentColour1D]
    redPeg = 0
    whitePeg = 0
    x = 0

    for x in range(0,4):
        if row1[x] == RandNum[x]:
            redPeg = redPeg + 1
            continue
        if row1[x] in RandNum:
            whitePeg = whitePeg + 1
            continue

    if redPeg == 1:
        return c.itemconfig(feed1, fill="red")
    elif redPeg == 2:
        return c.itemconfig(feed1, fill="red")
        return c.itemconfig(feed2, fill="red")####sort this out will only output one red peg
        
        
    elif redPeg == 3:
        return c.itemconfig(feed3, fill="red")
#row 1
feed1 = c.create_rectangle(310,650,326,666, fill= feedback())#bottom left
feed2 = c.create_rectangle(310,630,326,646, fill="white")#top left
feed3 = c.create_rectangle(330,650,346,666, fill="white")#bottom right
feed4 = c.create_rectangle(330,630,346,646, fill="white")#top right
#row 2
c.create_rectangle(310,580,326,596, fill="white")#bottom left
c.create_rectangle(310,560,326,576, fill="white")#top left
c.create_rectangle(330,580,346,596, fill="white")#bottom right
c.create_rectangle(330,560,346,576, fill="white")#top right
#row 3
c.create_rectangle(310,510,326,526, fill="white")#bottom left
c.create_rectangle(310,490,326,506, fill="white")#top left
c.create_rectangle(330,510,346,526, fill="white")#bottom right
c.create_rectangle(330,490,346,506, fill="white")#top right
#row 4
c.create_rectangle(310,440,326,456, fill="white")#bottom left
c.create_rectangle(310,420,326,436, fill="white")#top left
c.create_rectangle(330,440,346,456, fill="white")#bottom right
c.create_rectangle(330,420,346,436, fill="white")#top right
#row 5
c.create_rectangle(310,370,326,386, fill="white")#bottom left
c.create_rectangle(310,350,326,366, fill="white")#top left
c.create_rectangle(330,370,346,386, fill="white")#bottom right
c.create_rectangle(330,350,346,366, fill="white")#top right
#row 6
c.create_rectangle(310,300,326,316, fill="white")#bottom left
c.create_rectangle(310,280,326,296, fill="white")#top left
c.create_rectangle(330,300,346,316, fill="white")#bottom right
c.create_rectangle(330,280,346,296, fill="white")#top right
#row 7
c.create_rectangle(310,230,326,246, fill="white")#bottom left
c.create_rectangle(310,210,326,226, fill="white")#top left
c.create_rectangle(330,230,346,246, fill="white")#bottom right
c.create_rectangle(330,210,346,226, fill="white")#top right
#row 8
c.create_rectangle(310,160,326,176, fill="white")#bottom left
c.create_rectangle(310,140,326,156, fill="white")#top left
c.create_rectangle(330,160,346,176, fill="white")#bottom right
c.create_rectangle(330,140,346,156, fill="white")#top right

    


c.pack()
root.geometry("400x700")
root.mainloop()



