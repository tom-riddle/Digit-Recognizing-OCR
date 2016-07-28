import os,sys
from Tkinter import *

from Tkinter import Tk
from PIL import ImageTk,Image
from tkFileDialog import askopenfilename
import Tkinter
import tkMessageBox

import numpy as np
from train import train_network
from network import Network
from process import process_vector_im

net = Network([784, 30, 10])
top = Tkinter.Tk()
top.title("Hand written digits recognition");
top.geometry("{0}x{1}+0+0".format(500,500))
filename = None
label = None
prevlabel = None;
def load():
   global filename
   global prevlabel
   global label
   filename = askopenfilename(parent=top)
   print filename
   image=Image.open(filename)
   timage = image.resize((250, 250), Image.ANTIALIAS)
   photo=ImageTk.PhotoImage(timage) 
   label=Label(image=photo)
   label.image=photo
   if prevlabel != None:
   	prevlabel.pack_forget()
   prevlabel = label
   label.pack()

def train():
	tkMessageBox.showinfo("Neural Network Trainer","Press Ok to start training")
	train_network(net)
	tkMessageBox.showinfo("Neural Network Trainer","Training Done")

def load_image(infilename) :
   img = Image.open(infilename)
   img.load()
   data = np.array(img)
   data = data.ravel()
   data = np.reshape(data, (784,1))
   print "Size of vectorized image "+ str(len(data))
   return data

def process():
   a = load_image(filename)
   result = process_vector_im(net,a);
   print "Result : " + str(result)
   var.set("Result : " + str(result))


frame = Frame(top)
frame.pack()

bottomframe = Frame(top)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Train",padx=25,height=3, bd=2,bg='yellow', fg="blue",command=train)
redbutton.pack( side = LEFT)

loadbutton = Button(frame, text="Load Image",padx=25,height=3,bg='yellow' ,fg="blue",command=load)
loadbutton.pack( side = LEFT )

greenbutton = Button(frame, text="Process",padx=25,height=3,fg="blue",bg='yellow' ,command=process)
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Quit",padx=25, height=3,fg="blue",bg='yellow' ,command=frame.quit)
bluebutton.pack( side = LEFT )


var = StringVar()
labelframe = Label(top, textvariable=var, height=6)
var.set("Result : ")
labelframe.pack()

top.mainloop()