import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import webbrowser



##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Tips")

#####For background Image
#loading the images
# img=ImageTk.PhotoImage(Image.open("8.jpg"))

# img2=ImageTk.PhotoImage(Image.open("8.jpg"))

# img3=ImageTk.PhotoImage(Image.open("8.jpg"))

image2 =Image.open('22.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)


logo_label=tk.Label()
logo_label.place(x=0,y=0)

x=1


# function to change to next image
# def move():
#     global x
#     if x == 4:
#             x = 1
#     if x == 1:
#         logo_label.config(image=img)
#     elif x == 2:
#         logo_label.config(image=img2)
#     elif x == 3:
#         logo_label.config(image=img3)
#     x = x+1
#     root.after(2000, move)
  
# # calling the function
# move()

# calling the function
def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

canvas=tk.Canvas(root,bg="black")
canvas.pack()
canvas.place(x=0, y=0)
text_var="BENEFITS OF YOGA IN DAY TO DAY LIFE"
text=canvas.create_text(0,-2000,text=text_var,font=('ittalian',25,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = 1600
height = 50
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()   #Function Calling


#frame_display = tk.LabelFrame(root, text=" --Display-- ", width=900, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display.grid(row=0, column=0, sticky='nw')
#frame_display.place(x=300, y=100)

#frame_display1 = tk.LabelFrame(root, text=" --Result-- ", width=900, height=200, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display1.grid(row=0, column=0, sticky='nw')
#frame_display1.place(x=300, y=430)

#frame_display2 = tk.LabelFrame(root, text=" --Calaries-- ", width=900, height=50, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display2.grid(row=0, column=0, sticky='nw')
#frame_display2.place(x=300, y=380)



frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=280, height=550, bd=5, font=('times', 14, ' bold '),bg="grey")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=10, y=130)




def update_label1(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=300, y=600)
    
    image2 =Image.open('p2.jpg')
    image2 =image2.resize((w,h), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image

    background_label.place(x=200, y=200)
    
################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
def update_cal(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=350, y=400)
    
    
    
###########################################################################



        
        
        
               
               
               



def Fighting():
    
#     label=tk.Label(root,text='''
# ''',width=80,bg="white",fg="black",height=30)
#     label.place(x=500,y=200)
    image2 =Image.open('use.jpg')
    image2 =image2.resize((700,700), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image
    background_label.place(x=350, y=110)
        
def Accident():

    image2 =Image.open('what.png')
    image2 =image2.resize((550,800), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image
    background_label.place(x=350, y=70)
    
def Robbery():

    image2 =Image.open('types.jpg')
    image2 =image2.resize((700,700), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image
    background_label.place(x=350, y=90)
    
def Theft():

    image2 =Image.open('rou.webp')
    image2 =image2.resize((700,700), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image
    background_label.place(x=350, y=90)
    
def Fraud():

    my_link=tk.Label(root,text='Vajrasan',bg="white",fg="blue",width=20,cursor='hand2',height=2,font=("Times", 20, 'underline'))
    my_link.place(x=350,y=100)
    # grid(padx=400,pady=10)
    
    my_link.bind('<Button-1>',
        lambda x:webbrowser.open_new("https://youtu.be/fSKBk9u9tP8"))


    my_link2=tk.Label(root,text='Sarvangasana',bg="white",fg="blue",cursor='hand2',width=20,height=2,font=("Times", 20, 'underline'))
    my_link2.place(x=350,y=200)
    
    my_link2.bind('<Button-1>',
        lambda x:webbrowser.open_new("https://youtu.be/g3wvIPXZ-Qo"))    
   
    my_link2=tk.Label(root,text='Gomukhasana',bg="white",fg="blue",cursor='hand2',width=20,height=2,font=("Times", 20, 'underline'))
    my_link2.place(x=350,y=300)
    
    my_link2.bind('<Button-1>',
        lambda x:webbrowser.open_new("https://youtu.be/d_dh_DwDr84")) 
    
    
    my_link2=tk.Label(root,text='Bhadrasana',bg="white",fg="blue",cursor='hand2',width=20,height=2,font=("Times", 20, 'underline'))
    my_link2.place(x=350,y=400)
    
    my_link2.bind('<Button-1>',
        lambda x:webbrowser.open_new("https://youtu.be/ndfx530PNuI"))
    
    my_link2=tk.Label(root,text='Shavasana',bg="white",fg="blue",cursor='hand2',width=20,height=2,font=("Times", 20, 'underline'))
    my_link2.place(x=350,y=500)
    
    my_link2.bind('<Button-1>',
        lambda x:webbrowser.open_new("https://youtu.be/SfAoPVt64LE"))
    
    my_link2=tk.Label(root,text='Shavasana',bg="white",fg="blue",cursor='hand2',width=20,height=2,font=("Times", 20, 'underline'))
    my_link2.place(x=350,y=600)
    
    my_link2.bind('<Button-1>',
        lambda x:webbrowser.open_new("https://youtu.be/-pebIpb4dOE"))
    
    my_link2=tk.Label(root,text='Shirsana',bg="white",fg="blue",cursor='hand2',width=20,height=2,font=("Times", 20, 'underline'))
    my_link2.place(x=350,y=600)
    
    my_link2.bind('<Button-1>',
        lambda x:webbrowser.open_new("https://www.youtube.com/shorts/QNTnBisZRP8?feature=share"))
    
def pre():
  
    from subprocess import call
    call(['python','GUI_Master.py'])

 #   label=tk.Label(root,text='''Blood Plates, Crohn's Disease--Swelling of the tissues
#''',width=100,bg="white",fg="black",height=30)
 #   label.place(x=500,y=200)
    
#def Wood_Sorel():

 #   label=tk.Label(root,text='''Liver and Digestive Disorders
#''',width=100,bg="white",fg="black",height=30)
 #   label.place(x=500,y=200)
    

#################################################################################################################
def window():
    root.destroy()




button1 = tk.Button(frame_alpr, text="Yoga Benefits", command= Fighting, width=20, height=2, font=('times', 15, ' bold '),bg="white",fg="black")
button1.place(x=10, y=10)

button2 = tk.Button(frame_alpr, text="What Is Yoga", command=Accident, width=20, height=2, font=('times', 15, ' bold '),bg="white",fg="black")
button2.place(x=10, y=90)

button3 = tk.Button(frame_alpr, text="Types Of Yoga", command=Robbery, width=20, height=2, font=('times', 15, ' bold '),bg="white",fg="black")
button3.place(x=10, y=170)

button4 = tk.Button(frame_alpr, text="Morning Routine", command=Theft, width=20, height=2,bg="white",fg="black", font=('times', 15, ' bold '))
button4.place(x=10, y=250)

button4 = tk.Button(frame_alpr, text="Links Of Videos", command=Fraud,width=20, height=2,bg="white",fg="black", font=('times', 15, ' bold '))
button4.place(x=10, y=330)

# button5 = tk.Button(frame_alpr, text="Prediction", command=pre, width=20, height=2,bg="white",fg="black", font=('times', 15, ' bold '))
# button5.place(x=10, y=420)

#button4 = tk.Button(frame_alpr, text="Wood_sorel", command=Wood_Sorel,width=20, height=1,bg="white",fg="black", font=('times', 15, ' bold '))
#button4.place(x=10, y=430)

exit = tk.Button(frame_alpr, text="Exit", command=window, width=20, height=2, font=('times', 15, ' bold '),bg="black",fg="white")
exit.place(x=10, y=450)



root.mainloop()

